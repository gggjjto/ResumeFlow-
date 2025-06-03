<template>
  <div class="resume-preview">
    <div class="preview-actions">
      <a-button type="primary" @click="$router.push('/')">返回编辑</a-button>
      <a-button type="primary" @click="downloadPDF">下载PDF</a-button>
      <a-button type="primary" @click="downloadWord">下载Word</a-button>
      <!-- <a-button type="primary" @click="printResume">打印简历</a-button> -->
      <a-button type="primary" @click="showAiModal = true">AI 优化</a-button>
    </div>
    
    <div ref="resumeContent">
      <resume-layout
        :basic-info="resumeData.basicInfo"
        :education="resumeData.education"
        :experience="resumeData.experience"
        :skills="resumeData.skills"
      />
    </div>

    <!-- AI 优化弹窗 -->
    <a-modal
      v-model:open="showAiModal"
      title="AI 优化简历"
      @ok="handleAiOptimize"
      :confirm-loading="aiLoading"
      ok-text="确定"
      cancel-text="取消"
    >
      <a-form>
        <a-form-item label="优化提示词">
          <a-input
            v-model:value="aiPrompt"
            placeholder="如：突出项目经验、精简描述等"
          />
        </a-form-item>
      </a-form>
      <div v-if="aiResult" class="ai-preview-title">优化后预览：</div>
      <div v-if="aiResult" class="ai-preview-content" v-html="aiResult"></div>
    </a-modal>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import html2pdf from 'html2pdf.js';
import { saveAs } from 'file-saver';
import { Document, Packer, Paragraph } from 'docx';
import ResumeLayout from '@/components/resume/ResumeLayout.vue';
import type { ResumeForm } from '../types/resume';
import '@/styles/resume.scss';

const resumeData = ref<ResumeForm>(JSON.parse(localStorage.getItem('resumeData') || '{}'));
const resumeContent = ref<HTMLElement | null>(null);

// AI 优化相关
const showAiModal = ref(false);
const aiPrompt = ref('');
const aiResult = ref('');
const aiLoading = ref(false);

const handleAiOptimize = async () => {
  if (!aiPrompt.value) {
    aiResult.value = '';
    return;
  }
  aiLoading.value = true;
  // 模拟AI优化，实际应调用后端API
  await new Promise(r => setTimeout(r, 1200));
  // 简单模拟：将提示词和简历内容拼接
  aiResult.value = `<div style="color:#1890ff;">【AI优化】${aiPrompt.value}</div><div style="margin-top:8px;">${formatResumeHtml(resumeData.value)}</div>`;
  aiLoading.value = false;
};

// 简单格式化简历内容为HTML
function formatResumeHtml(data: ResumeForm) {
  return `
    <strong>${data.basicInfo?.name || ''}</strong> - ${data.basicInfo?.position || ''}<br>
    <span>${data.basicInfo?.email || ''} | ${data.basicInfo?.phone || ''}</span><br>
    <br>
    <strong>教育经历：</strong><br>
    ${(data.education || []).map(e => `${e.school} ${e.major} (${e.startDate}~${e.endDate})`).join('<br>')}
    <br><br>
    <strong>工作经历：</strong><br>
    ${(data.experience || []).map(e => `${e.company} - ${e.position} (${e.startDate}~${e.endDate})<br>${e.description}`).join('<br>')}
    <br><br>
    <strong>技能：</strong> ${(data.skills || []).join('、')}
  `;
}

const printResume = () => {
  window.print();
};

const downloadPDF = () => {
  const element = resumeContent.value;
  if (!element) return;
  
  const opt = {
    margin: 1,
    filename: '我的简历.pdf',
    image: { type: 'jpeg', quality: 0.98 },
    html2canvas: { scale: 2 },
    jsPDF: { unit: 'in', format: 'a4', orientation: 'portrait' }
  };

  html2pdf().set(opt).from(element).save();
};

const downloadWord = async () => {
  // 创建Word文档
  const doc = new Document({
    sections: [{
      properties: {},
      children: [
        new Paragraph({ text: resumeData.value.basicInfo.name }),
        // 可以根据需要添加更多内容
      ]
    }]
  });

  // 生成Word文件并下载
  const buffer = await Packer.toBlob(doc);
  saveAs(buffer, '我的简历.docx');
};

const formattedAiContent = computed(() => {
  return resumeData.value.aiContent?.replace(/\n/g, '<br>') || '';
});
</script>

<style lang="scss" scoped>
.preview-actions {
  position: sticky;
  top: 0;
  z-index: 100;
  background: white;
  padding: 20px 0;
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}
.ai-preview-title {
  margin-top: 16px;
  font-weight: bold;
  color: #1890ff;
}
.ai-preview-content {
  margin-top: 8px;
  background: #f6faff;
  border-radius: 6px;
  padding: 16px;
  border: 1px solid #e6f7ff;
  color: #222;
  font-size: 15px;
  line-height: 1.8;
  word-break: break-all;
}
@media print {
  .preview-actions {
    display: none;
  }
}
</style>