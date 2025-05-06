import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { message } from 'ant-design-vue';
import type { ResumeForm } from '@/types/resume';
import { generateResumeContent } from '@/api/openai';

export function useResume() {
  const router = useRouter();
  const currentStep = ref(0);
  const loading = ref(false);
  const skillText = ref('');

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

  const formatDate = (date: string) => {
    if (!date) return '至今';
    return date;
  };

  return {
    resumeForm,
    currentStep,
    loading,
    skillText,
    addExperience,
    removeExperience,
    nextStep,
    prevStep,
    goToStep,
    generateResume,
    formatDate
  };
}