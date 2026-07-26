import { useSelector, useDispatch } from "react-redux";
import { unenroll } from "../redux/enrollmentSlice";
import StudentProfile from "../components/StudentProfile";

function ProfilePage() {
  const dispatch = useDispatch();

  const enrolledCourses = useSelector(
    (state) => state.enrollment.enrolledCourses
  );

  return (
    <div>
      <h2>Profile</h2>

      <StudentProfile />

      <h3>Enrolled Courses</h3>

      {enrolledCourses.length === 0 ? (
        <p>No enrolled courses.</p>
      ) : (
        enrolledCourses.map((course) => (
          <div key={course.id}>
            <strong>{course.name}</strong>

            <button
              onClick={() =>
                dispatch(unenroll(course.id))
              }
              style={{ marginLeft: "10px" }}
            >
              Remove
            </button>
          </div>
        ))
      )}
    </div>
  );
}

export default ProfilePage;