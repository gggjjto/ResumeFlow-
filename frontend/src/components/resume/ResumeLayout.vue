<template>
  <div class="resume-content">
    <h1>{{ basicInfo.name }}</h1>
    <p class="title">{{ basicInfo.title }}</p>
    
    <div class="contact-info">
      <p>{{ basicInfo.email }} | {{ basicInfo.phone }}</p>
    </div>

    <template v-if="education?.length">
      <h2>教育背景</h2>
      <div v-for="(edu, index) in education" :key="index">
        <div class="education-row">
          <span class="school">{{ edu.school }}</span>
          <span class="major">{{ edu.major }}</span>
          <span class="degree-date">
            {{ edu.degree }} | {{ edu.startDate }} - {{ edu.endDate }}
          </span>
        </div>
      </div>
    </template>

    <template v-if="experience?.length">
      <h2>工作经验</h2>
      <div v-for="(exp, index) in experience" :key="index">
        <h3>{{ exp.company }} - {{ exp.position }}</h3>
        <p>{{ formatDate(exp.startDate) }} - {{ formatDate(exp.endDate) }}</p>
        <p class="description">{{ exp.description }}</p>
      </div>
    </template>

    <template v-if="skills?.length">
      <h2>技能特长</h2>
      <ul class="skills-text">
        <li v-for="(skill, index) in skills" :key="index">
          {{ skill }}
        </li>
      </ul>
    </template>

    <slot></slot>
  </div>
</template>

<script setup lang="ts">
import type { BasicInfo, Education, Experience } from '@/types/resume';

defineProps<{
  basicInfo: BasicInfo;
  education: Education[];
  experience: Experience[];
  skills: string[];
}>();

const formatDate = (date: string) => {
  if (!date) return '至今';
  return date;
};
</script>

<style lang="scss" scoped>
@use '@/styles/resume.scss';

.description {
  white-space: pre-wrap;
  color: #666;
}

.skills-text {
  list-style: none;
  padding: 0;
  margin: 0;
  
  li {
    position: relative;
    padding-left: 12px;
    margin-bottom: 12px;
    line-height: 1.6;
    color: #333;
    
    &::before {
      content: "•";
      position: absolute;
      left: 0;
      color: #1890ff;
    }
  }
}
</style>
