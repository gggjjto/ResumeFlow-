<template>
  <a-config-provider :locale="zhCN">
    <div class="resume-builder page-container">
      <a-row :gutter="24">
        <!-- 左侧表单 -->
        <a-col :xs="24" :sm="24" :md="10" :lg="10">
          <a-card title="编辑简历">
            <a-spin :spinning="loading">
              <a-steps :current="currentStep" class="steps-nav">
                <a-step title="基本信息" @click="() => goToStep(0)" class="step-item" />
                <a-step title="教育经历" @click="() => goToStep(1)" class="step-item" />
                <a-step title="工作经验" @click="() => goToStep(2)" class="step-item" />
                <a-step title="技能特长" @click="() => goToStep(3)" class="step-item" />
              </a-steps>

              <div class="form-container">
                <a-form :model="resumeForm" layout="vertical">
                  <basic-info
                    v-if="currentStep === 0"
                    v-model="resumeForm.basicInfo"
                  />
                  <education
                    v-if="currentStep === 1"
                    v-model="resumeForm.education"
                  />
                  <experience
                    v-if="currentStep === 2"
                    v-model="resumeForm.experience"
                  />
                  <skills
                    v-if="currentStep === 3"
                    v-model="resumeForm.skills"
                  />
                </a-form>
              </div>

              <div class="form-actions">
                <a-button 
                  v-if="currentStep > 0" 
                  @click="prevStep"
                >上一步</a-button>
                <a-button 
                  type="primary" 
                  @click="nextStep"
                  :loading="loading"
                >
                  {{ currentStep === 3 ? '生成简历' : '下一步' }}
                </a-button>
              </div>
            </a-spin>
          </a-card>
        </a-col>

        <!-- 右侧预览 -->
        <a-col :xs="24" :sm="24" :md="14" :lg="14">
          <a-card title="实时预览" :loading="loading" class="preview-card">
            <resume-layout
              :basic-info="resumeForm.basicInfo"
              :education="resumeForm.education"
              :experience="resumeForm.experience"
              :skills="resumeForm.skills"
            />
          </a-card>
        </a-col>
      </a-row>
    </div>
  </a-config-provider>
</template>

<script setup lang="ts">
import { ref, watch, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { message } from 'ant-design-vue';
import zhCN from 'ant-design-vue/es/locale/zh_CN';
import BasicInfo from '@/components/resume/BasicInfo.vue';
import Education from '@/components/resume/Education.vue';
import Experience from '@/components/resume/Experience.vue';
import Skills from '@/components/resume/Skills.vue';
import ResumeLayout from '@/components/resume/ResumeLayout.vue';
import type { ResumeForm } from 'src/types/resume';
import '@/styles/resume.scss';

const resumeForm = ref<ResumeForm>({
  basicInfo: {
    name: '',
    email: '',
    phone: '',
    title: ''
  },
  education: [{
    school: '',
    major: '',
    degree: '',
    startDate: '',
    endDate: ''
  }],
  experience: [],
  skills: []
});

const router = useRouter();
const currentStep = ref(0);
const loading = ref(false);
const skillText = ref('');

const addExperience = () => {
  resumeForm.value.experience.push({
    company: '',
    position: '',
    startDate: '',
    endDate: '',
    description: ''
  });
};

const removeExperience = (index: number) => {
  resumeForm.value.experience.splice(index, 1);
};

const nextStep = async () => {
  if (currentStep.value === 3) {
    await generateResume();
  } else {
    currentStep.value++;
  }
};

const prevStep = () => {
  currentStep.value--;
};

const goToStep = (step: number) => {
  currentStep.value = step;
};

const generateResume = async () => {
  loading.value = true;
  try {
    // 直接保存表单数据
    localStorage.setItem('resumeData', JSON.stringify(resumeForm.value));
    message.success('简历生成成功！');
    await router.push('/preview');
  } catch (error) {
    message.error('生成失败，请重试');
    console.error(error);
  } finally {
    loading.value = false;
  }
};

// 监听技能文本变化，自动更新技能列表
watch(skillText, (newValue) => {
  const skills = newValue.split('\n').filter(skill => skill.trim());
  resumeForm.value.skills = skills;
});

// 组件挂载时，如果已有技能，则填充文本框
onMounted(() => {
  if (resumeForm.value.skills.length > 0) {
    skillText.value = resumeForm.value.skills.join('\n');
  }
});

// 在工作经验预览部分格式化日期显示
const formatDate = (date: string) => {
  if (!date) return '至今';
  return date;
};
</script>

<style lang="scss" scoped>
.resume-builder {
  padding: 24px;
  max-width: 1600px;
  margin: 0 auto;
}

// ...rest of the unique styles...
</style>
