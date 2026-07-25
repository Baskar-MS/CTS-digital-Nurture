import { useEffect, useState } from "react";

import Header from "./components/Header";
import Footer from "./components/Footer";
import CourseCard from "./components/CourseCard";
import StudentProfile from "./components/StudentProfile";

import "./App.css";

function App() {
  const [courses, setCourses] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [enrolledCourses, setEnrolledCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  // Fetch courses from API
  useEffect(() => {
    async function fetchCourses() {
      try {
        const response = await fetch(
          "https://jsonplaceholder.typicode.com/posts?_limit=5"
        );

        if (!response.ok) {
          throw new Error("Failed to fetch courses");
        }

        const data = await response.json();

        const courseNames = [
          "HTML",
          "CSS",
          "JavaScript",
          "React",
          "Python",
        ];

        const mappedCourses = data.map((post, index) => ({
          id: post.id,
          name: courseNames[index],
          code: `CS10${index + 1}`,
          credits: index % 2 === 0 ? 4 : 3,
          grade: "A",
        }));

        setCourses(mappedCourses);
      } catch (err) {
        setError("Unable to fetch courses.");
      } finally {
        setLoading(false);
      }
    }

    fetchCourses();
  }, []);

  // Runs whenever courses change
  // Dependency array ensures this effect runs only when
  // the courses state changes.
  useEffect(() => {
    console.log("Courses updated");
  }, [courses]);

  // Enroll handler
  function handleEnroll(course) {
    const alreadyEnrolled = enrolledCourses.find(
      (c) => c.id === course.id
    );

    if (!alreadyEnrolled) {
      setEnrolledCourses([...enrolledCourses, course]);
    }
  }

  // Search filter
  const filteredCourses = courses.filter((course) =>
    course.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <>
      <Header
        siteName="Student Portal"
        enrolledCount={enrolledCourses.length}
      />

      <main className="container">
        <h2>Available Courses</h2>

        <input
          type="text"
          placeholder="Search Courses..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />

        {loading && <h2>Loading...</h2>}

        {error && <h2>{error}</h2>}

        {!loading && !error && (
          <div className="course-grid">
            {filteredCourses.map((course) => (
              <CourseCard
                key={course.id}
                {...course}
                onEnroll={handleEnroll}
              />
            ))}
          </div>
        )}

        <StudentProfile />
      </main>

      <Footer />
    </>
  );
}

export default App;