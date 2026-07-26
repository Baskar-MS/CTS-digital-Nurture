import { useParams } from "react-router-dom";

function CourseDetailPage({ courses }) {

  const { courseId } = useParams();

  const course = courses.find(
    (c) => c.id === Number(courseId)
  );

  if (!course) {
    return <h2>Course Not Found</h2>;
  }

  return (
    <div>

      <h2>{course.name}</h2>

      <p>Course Code : {course.code}</p>

      <p>Credits : {course.credits}</p>

      <p>Grade : {course.grade}</p>

    </div>
  );
}

export default CourseDetailPage;