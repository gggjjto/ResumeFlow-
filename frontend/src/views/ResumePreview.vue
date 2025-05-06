<template>
  <div class="resume-preview">
    <div class="preview-actions">
      <a-button type="primary" @click="$router.push('/')">返回编辑</a-button>
      <a-button type="primary" @click="printResume">打印简历</a-button>
    </div>
    
    <div class="resume-content" ref="resumeContent">
      <h1>{{ resumeData.basicInfo.name }}</h1>
      <div class="contact-info">
        <p>{{ resumeData.basicInfo.email }} | {{ resumeData.basicInfo.phone }}</p>
        <p>{{ resumeData.basicInfo.title }}</p>
      </div>

      <div class="section">
        <h2>教育背景</h2>
        <div v-for="(edu, index) in resumeData.education" :key="index">
          <h3>{{ edu.school }}</h3>
          <p>{{ edu.major }} - {{ edu.degree }}</p>
          <p>毕业年份: {{ edu.graduationYear }}</p>
        </div>
      </div>

      <div class="section">
        <h2>工作经验</h2>
        <div v-for="(exp, index) in resumeData.experience" :key="index">
          <h3>{{ exp.company }} - {{ exp.position }}</h3>
          <p>{{ exp.startDate }} - {{ exp.endDate }}</p>
          <p>{{ exp.description }}</p>
        </div>
      </div>

      <div class="section">
        <h2>技能专长</h2>
        <div class="skills">
          <a-tag v-for="skill in resumeData.skills" :key="skill">
            {{ skill }}
          </a-tag>
        </div>
      </div>

      <div class="ai-content" v-if="resumeData.aiContent">
        <h2>AI优化建议</h2>
        <div v-html="formattedAiContent"></div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';
import type { ResumeForm } from '../types/resume';

const resumeData = ref<ResumeForm>(JSON.parse(localStorage.getItem('resumeData') || '{}'));
const resumeContent = ref<HTMLElement | null>(null);

const printResume = () => {
  window.print();
};

const formattedAiContent = computed(() => {
  return resumeData.value.aiContent?.replace(/\n/g, '<br>') || '';
});
</script>

<style scoped>
.resume-preview {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.preview-actions {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.resume-content {
  background: white;
  padding: 40px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.section {
  margin: 20px 0;
}

.skills {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

@media print {
  .preview-actions {
    display: none;
  }
  
  .resume-content {
    box-shadow: none;
  }
}
</style>
