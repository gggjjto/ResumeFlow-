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
            <div class="preview-content">
              <h1>{{ resumeForm.basicInfo.name }}</h1>
              <p class="title">{{ resumeForm.basicInfo.title }}</p>
              
              <div class="contact-info">
                <p>{{ resumeForm.basicInfo.email }} | {{ resumeForm.basicInfo.phone }}</p>
              </div>

              <template v-if="resumeForm.education.length">
                <h2>教育背景</h2>
                <div v-for="(edu, index) in resumeForm.education" :key="index">
                  <h3>{{ edu.school }}</h3>
                  <p>{{ edu.major }} - {{ edu.degree }}</p>
                  <p>毕业年份: {{ edu.graduationYear }}</p>
                </div>
              </template>

              <template v-if="resumeForm.experience.length">
                <h2>工作经验</h2>
                <div v-for="(exp, index) in resumeForm.experience" :key="index">
                  <h3>{{ exp.company }} - {{ exp.position }}</h3>
                  <p>{{ formatDate(exp.startDate) }} - {{ formatDate(exp.endDate) }}</p>
                  <p class="description">{{ exp.description }}</p>
                </div>
              </template>

              <template v-if="resumeForm.skills.length">
                <h2>技能专长</h2>
                <ul class="skills-text">
                  <li v-for="(skill, index) in resumeForm.skills" :key="index">
                    {{ skill }}
                  </li>
                </ul>
              </template>
            </div>
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
import { generateResumeContent } from '../api/openai';
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
    graduationYear: ''
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
    const aiContent = await generateResumeContent(resumeForm.value);
    // 保存AI生成的内容和原始表单数据
    localStorage.setItem('resumeData', JSON.stringify({
      ...resumeForm.value,
      aiContent
    }));
    message.success('简历生成成功！');
    router.push('/preview');
  } catch (error) {
    message.error('生成简历失败，请重试');
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

<style scoped>
.resume-builder {
  padding: 24px;
  max-width: 1600px;
  margin: 0 auto;
}

.steps-nav {
  margin-bottom: 32px;
}

.form-container {
  max-width: 100%;
  margin: 0 auto;
}

.form-actions {
  display: flex;
  justify-content: space-between;
  margin-top: 24px;
  padding-top: 24px;
  border-top: 1px solid #f0f0f0;
}

:deep(.ant-form-item) {
  margin-bottom: 24px;
}

:deep(.ant-input),
:deep(.ant-select-selector) {
  border-radius: var(--border-radius-base);
}

.experience-item {
  background: #fafafa;
  border-radius: var(--border-radius-base);
  padding: 24px;
  margin-bottom: 16px;
  transition: all 0.3s;
}

.experience-item:hover {
  box-shadow: var(--box-shadow);
}

.preview-card {
  position: sticky;
  top: 24px;
  height: calc(100vh - 48px);
  overflow-y: auto;
}

.preview-content {
  min-height: 800px;
  padding: 40px;
  background: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  max-width: 900px;
  margin: 0 auto;
  font-size: 16px;
}

.title {
  color: #666;
  font-size: 1.2em;
  margin: 8px 0;
}

.contact-info {
  margin: 16px 0;
  color: #333;
}

h2 {
  border-bottom: 2px solid #1890ff;
  padding-bottom: 8px;
  margin: 24px 0 16px;
}

.description {
  white-space: pre-wrap;
  color: #666;
}

.skills {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.skills-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.skill-item {
  background: #f9f9f9;
  transition: all 0.3s;
  margin-bottom: 8px;
}

.skill-item:hover {
  background: #f0f0f0;
}

.skill-item p {
  margin: 0;
  white-space: pre-wrap;
}

.suggested-skills {
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px dashed #d9d9d9;
}

.suggested-skills h4 {
  margin-bottom: 8px;
  color: #666;
}

.step-item {
  cursor: pointer;
}

:deep(.ant-steps-item) {
  cursor: pointer;
}

:deep(.ant-steps-item-container) {
  padding: 4px 8px;
  border-radius: 4px;
  transition: background-color 0.3s;
}

:deep(.ant-steps-item-container:hover) {
  background-color: rgba(0, 0, 0, 0.04);
}

.skill-card {
  width: 100%;
  margin-bottom: 8px;
}

.skill-card h4 {
  margin: 0;
  color: #1890ff;
}

.skill-card p {
  margin: 4px 0 0;
  color: #666;
  font-size: 14px;
}

.skill-tips {
  margin-bottom: 16px;
  padding: 12px;
  background: #f5f5f5;
  border-radius: 4px;
}

.tip-text {
  color: #666;
  margin-bottom: 8px;
}

.skill-tips ul {
  padding-left: 20px;
  margin: 0;
}

.skill-tips li {
  color: #888;
  margin-bottom: 4px;
}

.form-tips {
  color: #888;
  font-size: 12px;
  margin-top: 4px;
}

.skills-text {
  list-style: none;
  padding: 0;
  margin: 0;
}

.skills-text li {
  position: relative;
  padding-left: 12px;
  margin-bottom: 12px;
  line-height: 1.6;
  color: #333;
}

.skills-text li::before {
  content: "•";
  position: absolute;
  left: 0;
  color: #1890ff;
}

.skills-preview,
.skill-item-preview,
.skill-number {
  display: none;
}

.form-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
  padding-bottom: 8px;
  border-bottom: 1px solid #f0f0f0;
}

.form-header h3 {
  margin: 0;
  color: #1890ff;
}

@media (max-width: 768px) {
  .preview-card {
    position: static;
    height: auto;
    margin-top: 24px;
  }
  
  .preview-content {
    padding: 20px;
  }
}
</style>
