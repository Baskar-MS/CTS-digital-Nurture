import apiClient from "./apiClient";

export function getAllCourses() {
  return apiClient.get("/posts?_limit=5");
}

export function getCourseById(id) {
  return apiClient.get(`/posts/${id}`);
}

export function enrollStudent(studentId, courseId) {
  return apiClient.post("/posts", {
    studentId,
    courseId,
  });
}