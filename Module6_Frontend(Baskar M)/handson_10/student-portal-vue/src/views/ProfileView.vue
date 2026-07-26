<template>

  <div>

    <h2>Student Profile</h2>

    <h3>Enrolled Courses</h3>

    <div
      v-for="course in enrolledCourses"
      :key="course.id"
    >

      {{ course.name }}
      ({{ course.credits }} Credits)

      <button
        @click="store.unenroll(course.id)"
      >
        Remove
      </button>

    </div>

    <hr>

    <h3>
      Total Credits:
      {{ totalCredits }}
    </h3>

  </div>

</template>

<script setup>
import { storeToRefs } from "pinia";
import { useEnrollmentStore } from "../stores/enrollment";

const store = useEnrollmentStore();

const {
  enrolledCourses,
  totalCredits
} = storeToRefs(store);
</script>