import { useDispatch } from "react-redux";
import { enroll } from "../redux/enrollmentSlice";
import { useNavigate } from "react-router-dom";

function CourseCard({ id, name, code, credits, grade }) {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  function handleEnroll() {
    dispatch(
      enroll({
        id,
        name,
        code,
        credits,
        grade,
      })
    );

    navigate("/profile");
  }

  return (
    <div className="course-card">
      <h3>{name}</h3>

      <p>Code: {code}</p>

      <p>Credits: {credits}</p>

      <p>Grade: {grade}</p>

      <button onClick={handleEnroll}>
        Enroll
      </button>
    </div>
  );
}

export default CourseCard;