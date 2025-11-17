<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <p>{{ description }}</p>
    <button @click="count++">Count: {{ count }}</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const message = ref('Welcome to Vue 3!')
const description = ref('Edit src/App.vue to get started')
const count = ref(0)
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

button {
  margin-top: 20px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}
</style>
