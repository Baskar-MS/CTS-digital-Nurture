import { Link } from "react-router-dom";
import { useSelector } from "react-redux";

function Header({ siteName }) {
  const enrolledCourses = useSelector(
    (state) => state.enrollment.enrolledCourses
  );

  return (
    <header>
      <h1>{siteName}</h1>

      <nav>
        <Link to="/">Home</Link>{" | "}
        <Link to="/courses">Courses</Link>{" | "}
        <Link to="/profile">Profile</Link>
      </nav>

      <h3>Enrolled : {enrolledCourses.length}</h3>
    </header>
  );
}

export default Header;