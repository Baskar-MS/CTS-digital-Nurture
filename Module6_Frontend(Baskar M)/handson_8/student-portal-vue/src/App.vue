<template>
  <div>

    <Header />

    <nav>
      <RouterLink to="/">Home</RouterLink> |
      <RouterLink to="/courses">Courses</RouterLink> |
      <RouterLink to="/profile">Profile</RouterLink>
    </nav>

    <hr>

    <RouterView />

  </div>
</template>

<script setup>
import Header from './components/Header.vue'
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
nav {
  padding: 15px;
}

nav a {
  margin-right: 15px;
  text-decoration: none;
}
</style>