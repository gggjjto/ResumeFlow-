<template>
  <div>
    <h2>基本信息</h2>
    <a-form-item label="姓名">
      <a-input v-model:value="basicInfo.name" />
    </a-form-item>
    <a-form-item label="邮箱">
      <a-input v-model:value="basicInfo.email" />
    </a-form-item>
    <a-form-item label="电话">
      <a-input v-model:value="basicInfo.phone" />
    </a-form-item>
    <a-form-item label="座右铭/职位/其他">
      <a-input v-model:value="basicInfo.title" />
    </a-form-item>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import type { BasicInfo } from '@/types/resume';

const props = defineProps<{
  modelValue: BasicInfo;
}>();

const emit = defineEmits(['update:modelValue']);

const basicInfo = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value)
});
</script>
