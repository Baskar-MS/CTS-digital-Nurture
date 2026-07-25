from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    status,
    BackgroundTasks,
    Response
)

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional

from database import engine, Base, get_db
from models import Course, Student, Enrollment

from schemas import (
    CourseCreate,
    CourseUpdate,
     CoursePatch,
    CourseResponse,
    StudentCreate,
    StudentUpdate,
    StudentResponse,
    EnrollmentCreate,
    EnrollmentResponse  
)

app = FastAPI(
    title="Course Management API",
    description="Course Management System built using FastAPI",
    version="1.0",
    contact={
        "name": "Baskar M",
        "email": "baskar@example.com"
    }
)

from fastapi.responses import JSONResponse
from fastapi.requests import Request

# -----------------------------
# Custom HTTP Exception Handler
# -----------------------------
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "error",
            "status_code": exc.status_code,
            "message": exc.detail
        }
    )

# -----------------------------
# Create Database Tables
# -----------------------------
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# -----------------------------
# Background Task Function
# -----------------------------
def send_confirmation_email(student_email: str):
    print(f"Sending confirmation to {student_email}")


# -----------------------------
# Root Endpoint
# -----------------------------
@app.get("/")
async def root():
    return {"message": "Course Management API is running"}
# API Versioning
# URL Versioning: /api/v1/courses/ (easy to understand and test)
# Header Versioning: Accept: application/vnd.api+json;version=1
# Header versioning keeps URLs clean but requires clients to send custom headers.

# -----------------------------
# Create Course
# -----------------------------
@app.post(
    "/api/v1/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Courses"],
    summary="Create a new course",
    response_description="Returns the created course"
)
async def create_course(
    response: Response,
    course: CourseCreate,
    db: AsyncSession = Depends(get_db)
):
    new_course = Course(
        name=course.name,
        code=course.code,
        credits=course.credits,
        department_id=course.department_id
    )

    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)
    response.headers["Location"] = f"/api/v1/courses/{new_course.id}/"

    return new_course


# -----------------------------
# Get All Courses
# -----------------------------
@app.get(
    "/api/v1/courses/",
    tags=["Courses"]
)
async def get_courses(
    page: int = 1,
    page_size: int = 10,
    department_id: Optional[int] = None,
    db: AsyncSession = Depends(get_db)
):
    query = select(Course)

    if department_id is not None:
        query = query.where(Course.department_id == department_id)

    # Count total results
    total_result = await db.execute(query)
    total_courses = len(total_result.scalars().all())

    # Pagination
    skip = (page - 1) * page_size

    query = query.offset(skip).limit(page_size)

    result = await db.execute(query)
    courses = result.scalars().all()

    next_page = (
        f"/api/v1/courses/?page={page + 1}&page_size={page_size}"
        if skip + page_size < total_courses
        else None
    )

    previous_page = (
        f"/api/v1/courses/?page={page - 1}&page_size={page_size}"
        if page > 1
        else None
    )

    return {
        "count": total_courses,
        "next": next_page,
        "previous": previous_page,
        "results": courses
    }

# -----------------------------
# Get Course by ID
# -----------------------------
@app.get(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse,
    tags=["Courses"]
)
async def get_course(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course


# -----------------------------
# Update Course
# -----------------------------
@app.put(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse,
    tags=["Courses"]
)
async def update_course(
    course_id: int,
    updated: CourseUpdate,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    if updated.name is not None:
        course.name = updated.name

    if updated.code is not None:
        course.code = updated.code

    if updated.credits is not None:
        course.credits = updated.credits

    if updated.department_id is not None:
        course.department_id = updated.department_id

    await db.commit()
    await db.refresh(course)

    return course
# -----------------------------
# patch Course
# -----------------------------

@app.patch(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse,
    tags=["Courses"]
)
async def patch_course(
    course_id: int,
    updated: CoursePatch,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    updates = updated.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(course, key, value)

    await db.commit()
    await db.refresh(course)

    return course


# -----------------------------
# Delete Course
# -----------------------------
@app.delete(
    "/api/v1/courses/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Courses"]
)
async def delete_course(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    await db.delete(course)
    await db.commit()


@app.post(
    "/api/v1/students/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Students"]
)
async def create_student(
    student: StudentCreate,
    db: AsyncSession = Depends(get_db)
):

    new_student = Student(
        name=student.name,
        email=student.email
    )

    db.add(new_student)

    await db.commit()

    await db.refresh(new_student)

    return new_student


@app.get(
    "/api/v1/students/",
    response_model=list[StudentResponse],
    tags=["Students"]
)
async def get_students(
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Student)
    )

    return result.scalars().all()

@app.get(
    "/api/v1/students/{student_id}",
    response_model=StudentResponse,
    tags=["Students"]
)
async def get_student(
    student_id:int,
    db:AsyncSession=Depends(get_db)
):

    result=await db.execute(
        select(Student).where(Student.id==student_id)
    )

    student=result.scalar_one_or_none()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student

@app.put(
    "/api/v1/students/{student_id}",
    response_model=StudentResponse,
    tags=["Students"]
)
async def update_student(
    student_id:int,
    updated:StudentUpdate,
    db:AsyncSession=Depends(get_db)
):

    result=await db.execute(
        select(Student).where(Student.id==student_id)
    )

    student=result.scalar_one_or_none()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    if updated.name is not None:
        student.name=updated.name

    if updated.email is not None:
        student.email=updated.email

    await db.commit()

    await db.refresh(student)

    return student


@app.delete(
    "/api/v1/students/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Students"]
)
async def delete_student(
    student_id:int,
    db:AsyncSession=Depends(get_db)
):

    result=await db.execute(
        select(Student).where(Student.id==student_id)
    )

    student=result.scalar_one_or_none()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    await db.delete(student)

    await db.commit()



@app.post(
    "/api/v1/enrollments/",
    response_model=EnrollmentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Enrollments"]
)
async def create_enrollment(
    enrollment: EnrollmentCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):

    # Check if student exists
    student_result = await db.execute(
        select(Student).where(Student.id == enrollment.student_id)
    )
    student = student_result.scalar_one_or_none()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # Check if course exists
    course_result = await db.execute(
        select(Course).where(Course.id == enrollment.course_id)
    )
    course = course_result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    new_enrollment = Enrollment(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id
    )

    db.add(new_enrollment)

    await db.commit()

    await db.refresh(new_enrollment)

    background_tasks.add_task(
        send_confirmation_email,
        student.email
    )

    return new_enrollment


@app.get(
    "/api/v1/enrollments/",
    response_model=list[EnrollmentResponse],
    tags=["Enrollments"]
)
async def get_enrollments(
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Enrollment)
    )

    return result.scalars().all()

@app.get(
    "/api/v1/enrollments/{enrollment_id}",
    response_model=EnrollmentResponse,
    tags=["Enrollments"]
)
async def get_enrollment(
    enrollment_id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Enrollment).where(
            Enrollment.id == enrollment_id
        )
    )

    enrollment = result.scalar_one_or_none()

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    return enrollment


@app.delete(
    "/api/v1/enrollments/{enrollment_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Enrollments"]
)
async def delete_enrollment(
    enrollment_id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Enrollment).where(
            Enrollment.id == enrollment_id
        )
    )

    enrollment = result.scalar_one_or_none()

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    await db.delete(enrollment)

    await db.commit()



@app.get(
    "/api/v1/courses/{course_id}/students/",
    response_model=list[StudentResponse],
    tags=["Courses"]
)
async def get_students_in_course(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):

    # Check if the course exists
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    # JOIN Student -> Enrollment
    result = await db.execute(
        select(Student)
        .join(Enrollment)
        .where(Enrollment.course_id == course_id)
    )

    students = result.scalars().all()

    return students