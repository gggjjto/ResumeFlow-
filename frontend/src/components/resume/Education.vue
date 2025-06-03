<template>
  <div>
    <h2>教育经历</h2>
    <div v-for="(edu, index) in education" :key="index" class="education-item">
      <a-row :gutter="16">
        <a-col :span="12">
          <a-form-item label="学校">
            <a-input v-model:value="edu.school" />
          </a-form-item>
        </a-col>
        <a-col :span="12">
          <a-form-item label="专业">
            <a-input v-model:value="edu.major" />
          </a-form-item>
        </a-col>
      </a-row>
      <a-form-item label="学位">
        <a-input v-model:value="edu.degree" />
      </a-form-item>
      <a-row :gutter="16">
        <a-col :span="12">
          <a-form-item label="开始时间">
            <a-date-picker 
              v-model:value="edu.startDate" 
              style="width: 100%" 
              value-format="YYYY年MM月"
              format="YYYY年MM月"
              picker="month"
              :placeholder="'请选择开始时间'"
              :locale="zhCN"
            />
          </a-form-item>
        </a-col>
        <a-col :span="12">
          <a-form-item label="结束时间">
            <a-date-picker 
              v-model:value="edu.endDate" 
              style="width: 100%" 
              value-format="YYYY年MM月"
              format="YYYY年MM月"
              picker="month"
              :placeholder="'请选择结束时间'"
              :locale="zhCN"
            />
          </a-form-item>
        </a-col>
      </a-row>
      <a-button type="danger" @click="removeEducation(index)">删除</a-button>
    </div>
    <a-button type="primary" @click="addEducation">添加教育经历</a-button>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import type { Education } from '@/types/resume';
import zhCN from 'ant-design-vue/es/locale/zh_CN';

const props = defineProps<{
  modelValue: Education[];
}>();

const emit = defineEmits(['update:modelValue']);

const education = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value)
});

const addEducation = () => {
  education.value.push({
    school: '',
    major: '',
    degree: '',
    startDate: '',
    endDate: ''
  });
};

const removeEducation = (index: number) => {
  education.value.splice(index, 1);
};
</script>

<style scoped>
.education-item {
  margin-bottom: 16px;
  padding: 16px;
  border: 1px solid #f0f0f0;
  border-radius: 4px;
  background: #fafafa;
}
</style>
