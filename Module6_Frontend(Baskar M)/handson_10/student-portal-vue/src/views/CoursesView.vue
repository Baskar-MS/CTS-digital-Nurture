<template>
  <div>
    <h2>Courses</h2>

    <input
      type="text"
      v-model="searchTerm"
      placeholder="Search Course"
    />

    <br /><br />

  <RouterLink
  v-for="course in filteredCourses"
  :key="course.id"
  :to="'/courses/' + course.id"
  class="course-link"
>
  <CourseCard
    :name="course.name"
    :code="course.code"
    :credits="course.credits"
    :grade="course.grade"
  />

  <button
    @click.prevent="store.enroll(course)"
  >
    Enroll
  </button>

</RouterLink>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import CourseCard from '../components/CourseCard.vue'
import { useEnrollmentStore } from '../stores/enrollment'
import { getAllCourses } from "../api/courseApi";

const store = useEnrollmentStore()

const searchTerm = ref('')

const courses = ref([])

onMounted(async () => {
  try {
    const data = await getAllCourses();

    courses.value = data.map((item) => ({
      id: item.id,
      name: item.title,
      code: `CS${item.id}`,
      credits: item.id % 2 === 0 ? 3 : 4,
      grade: "A",
    }));
  } catch (error) {
    console.error(error.message);
  }
});

const filteredCourses = computed(() => {
  return courses.value.filter(course =>
    course.name.toLowerCase().includes(searchTerm.value.toLowerCase())
  )
})
</script>

<style scoped>
input {
  padding: 10px;
  width: 300px;
  margin-bottom: 20px;
}

.course-link {
  text-decoration: none;
  color: inherit;
  display: block;
}
</style>