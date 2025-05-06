<template>
  <div>
    <h2>工作经验</h2>
    <div v-for="(exp, index) in experiences" :key="index" class="experience-item">
      <div class="form-header">
        <h3>工作经历 #{{index + 1}}</h3>
        <a-button danger size="small" @click="removeExperience(index)">
          <template #icon><delete-outlined /></template>
          删除
        </a-button>
      </div>
      <a-form-item label="公司名称">
        <a-input v-model:value="exp.company" />
      </a-form-item>
      <a-form-item label="职位">
        <a-input v-model:value="exp.position" />
      </a-form-item>
      <a-row :gutter="16">
        <a-col :span="12">
          <a-form-item label="开始时间">
            <a-date-picker 
              v-model:value="exp.startDate" 
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
              v-model:value="exp.endDate" 
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
      <a-form-item label="工作描述">
        <a-textarea v-model:value="exp.description" :rows="4" />
      </a-form-item>
    </div>
    <a-button type="dashed" block @click="addExperience">+ 添加工作经验</a-button>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { DeleteOutlined } from '@ant-design/icons-vue';
import zhCN from 'ant-design-vue/es/locale/zh_CN';
import type { Experience } from '@/types/resume';

const props = defineProps<{
  modelValue: Experience[];
}>();

const emit = defineEmits(['update:modelValue']);

const experiences = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value)
});

const addExperience = () => {
  experiences.value.push({
    company: '',
    position: '',
    startDate: '',
    endDate: '',
    description: ''
  });
};

const removeExperience = (index: number) => {
  experiences.value.splice(index, 1);
};
</script>
