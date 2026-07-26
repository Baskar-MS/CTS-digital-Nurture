import { Link } from "react-router-dom";
import CourseCard from "../components/CourseCard";

function CoursesPage({ courses }) {
  return (
    <div>
      <h2>Courses</h2>

      <div className="course-grid">
        {courses.map((course) => (
          <div key={course.id}>
            <Link to={`/courses/${course.id}`}>
              <CourseCard {...course} />
            </Link>
          </div>
        ))}
      </div>
    </div>
  );
}

export default CoursesPage;