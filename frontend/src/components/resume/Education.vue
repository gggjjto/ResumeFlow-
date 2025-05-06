<template>
  <div>
    <h2>教育经历</h2>
    <div v-for="(edu, index) in education" :key="index">
      <a-form-item label="学校">
        <a-input v-model:value="edu.school" />
      </a-form-item>
      <a-form-item label="专业">
        <a-input v-model:value="edu.major" />
      </a-form-item>
      <a-form-item label="学位">
        <a-input v-model:value="edu.degree" />
      </a-form-item>
      <a-form-item label="毕业年份">
        <a-input v-model:value="edu.graduationYear" />
      </a-form-item>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import type { Education } from '@/types/resume';

const props = defineProps<{
  modelValue: Education[];
}>();

const emit = defineEmits(['update:modelValue']);

const education = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value)
});
</script>
