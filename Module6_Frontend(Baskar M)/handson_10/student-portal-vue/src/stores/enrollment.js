import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { getCourseById } from "../api/courseApi";
export const useEnrollmentStore = defineStore('enrollment', () => {

  const enrolledCourses = ref([])

  const totalCredits = computed(() => {
    return enrolledCourses.value.reduce(
      (total, course) => total + course.credits,
      0
    )
  })

  async function fetchAndEnroll(courseId) {
  try {
    const data = await getCourseById(courseId);

    enroll({
      id: data.id,
      name: data.title,
      credits: 4,
      grade: "A"
    });

  } catch (error) {
    console.error(error.message);
  }
}

function clearEnrollments() {
  enrolledCourses.value = [];
}


  function enroll(course) {

    const exists = enrolledCourses.value.find(
      c => c.id === course.id
    )

    if (!exists) {
      enrolledCourses.value.push(course)
    }
  }

  function unenroll(courseId) {

    enrolledCourses.value =
      enrolledCourses.value.filter(
        course => course.id !== courseId
      )
  }

 return {
  enrolledCourses,
  totalCredits,
  enroll,
  unenroll,
  fetchAndEnroll,
  clearEnrollments
}

})