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

const store = useEnrollmentStore()

const searchTerm = ref('')

const courses = ref([])

onMounted(() => {
  courses.value = [
    {
      id: 1,
      name: 'Vue.js',
      code: 'CS301',
      credits: 4,
      grade: 'A'
    },
    {
      id: 2,
      name: 'React',
      code: 'CS302',
      credits: 3,
      grade: 'A+'
    },
    {
      id: 3,
      name: 'Angular',
      code: 'CS303',
      credits: 4,
      grade: 'B+'
    },
    {
      id: 4,
      name: 'Python',
      code: 'CS304',
      credits: 5,
      grade: 'A'
    },
    {
      id: 5,
      name: 'Java',
      code: 'CS305',
      credits: 4,
      grade: 'A'
    }
  ]
})

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