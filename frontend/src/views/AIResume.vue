<template>
  <div class="ai-resume-page">
    <h2>AI 优化简历</h2>
    <a-form @submit.prevent="handleOptimize">
      <a-form-item label="原始简历内容">
        <a-textarea
          v-model:value="originContent"
          placeholder="请输入需要优化的简历内容"
          :rows="8"
        />
      </a-form-item>
      <a-form-item>
        <a-button type="primary" html-type="submit" :loading="loading">AI 优化</a-button>
      </a-form-item>
    </a-form>
    <div class="result-block" v-if="optimizedContent">
      <h3>优化后内容</h3>
      <div class="optimized-content" v-html="optimizedContent"></div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const originContent = ref('');
const optimizedContent = ref('');
const loading = ref(false);

const handleOptimize = async () => {
  if (!originContent.value) {
    alert('请输入简历内容');
    return;
  }
  loading.value = true;
  // 模拟AI优化，实际应调用后端API
  await new Promise(r => setTimeout(r, 1200));
  optimizedContent.value = originContent.value
    .replace(/(\S)/g, '$1✨') // 示例：每个字后加✨，实际应为AI返回内容
    .replace(/\n/g, '<br>');
  loading.value = false;
};
</script>

<style scoped lang="scss">
.ai-resume-page {
  max-width: 700px;
  margin: 40px auto;
  background: #fff;
  border-radius: 8px;
  padding: 32px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.08);
}
.result-block {
  margin-top: 32px;
  background: #f6faff;
  border-radius: 6px;
  padding: 20px;
  border: 1px solid #e6f7ff;
}
.optimized-content {
  color: #222;
  font-size: 16px;
  line-height: 1.8;
  word-break: break-all;
}
</style>