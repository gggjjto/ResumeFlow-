<script setup lang="ts">
</script>

<template>
  <div class="app-container">
    <header class="app-header">
      <h1>AI智能简历生成器</h1>
    </header>
    <main class="app-main">
      <router-view></router-view>
    </main>
    <footer class="app-footer">
      <p>© 2023 AI Resume Generator</p>
    </footer>
  </div>
</template>

<style scoped>
.app-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.app-header {
  background: #001529;
  padding: 1rem;
  text-align: center;
  color: white;
}

.app-main {
  flex: 1;
  background: #f0f2f5;
  padding: 2rem 0;
}

.app-footer {
  background: #001529;
  color: white;
  text-align: center;
  padding: 1rem;
}
</style>