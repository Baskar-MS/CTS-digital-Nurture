import { useEffect, useState } from "react";

import Header from "./components/Header";
import Footer from "./components/Footer";

import HomePage from "./pages/HomePage";
import CoursesPage from "./pages/CoursesPage";
import ProfilePage from "./pages/ProfilePage";
import CourseDetailPage from "./pages/CourseDetailPage";

import { Routes, Route } from "react-router-dom";

import "./App.css";

function App() {


  const [courses, setCourses] = useState([]);

  useEffect(() => {

    async function loadCourses() {

      const response = await fetch(
        "https://jsonplaceholder.typicode.com/posts?_limit=5"
      );

      const data = await response.json();

      const courseNames = [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Python"
      ];

      const mapped = data.map((post, index) => ({

        id: post.id,

        name: courseNames[index],

        code: `CS10${index + 1}`,

        credits: index % 2 === 0 ? 4 : 3,

        grade: "A"

      }));

      setCourses(mapped);

    }

    loadCourses();

  }, []);


  return (

    <>

      <Header

        siteName="Student Portal"


      />

      <Routes>

        <Route

          path="/"

          element={<HomePage />}

        />

        <Route
           path="/courses"
          element={<CoursesPage courses={courses} />}
        />

        <Route

          path="/profile"

          element={<ProfilePage />}

        />

        <Route

          path="/courses/:courseId"

          element={

            <CourseDetailPage

              courses={courses}

            />

          }

        />

      </Routes>

      <Footer />

    </>

  );

}

export default App;