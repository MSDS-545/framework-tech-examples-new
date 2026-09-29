<script setup>
// ref() creates reactive state. When its value changes, Vue updates the UI.
import { ref } from 'vue'
const message = ref('Hello from Vue!')
const clicks = ref(0)

function handleClick() {
  // In JavaScript code, a ref's current value is accessed through .value.
  clicks.value += 1
  message.value = `Button clicked ${clicks.value} time(s)`
}
</script>

<template>
  <main>
    <!-- {{ }} displays reactive data in a Vue template. -->
    <h1>{{ message }}</h1>
    <!-- @click is shorthand for v-on:click and attaches an event handler. -->
    <button @click="handleClick">Click Me</button>
  </main>
</template>

<style scoped>
/* scoped limits these styles to this component. */
main { font-family: sans-serif; max-width: 700px; margin: 3rem auto; }
button { padding: 0.6rem 1rem; }
</style>
