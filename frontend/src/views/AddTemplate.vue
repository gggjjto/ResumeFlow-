<template>
  <div class="add-template-page">
    <h2>添加新模板</h2>
    <a-form @submit.prevent="handleAdd">
      <a-form-item label="模板名称">
        <a-input v-model="templateName" placeholder="请输入模板名称" />
      </a-form-item>
      <a-form-item label="模板HTML代码">
        <a-textarea
          v-model:value="templateHtml"
          placeholder="请输入或粘贴模板HTML代码"
          :rows="8"
        />
      </a-form-item>
      <a-form-item>
        <a-button type="primary" html-type="submit">添加模板</a-button>
      </a-form-item>
    </a-form>
    <div class="preview-title">模板实时预览</div>
    <div class="template-preview" v-html="templateHtml">

    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const templateName = ref('');
const templateHtml = ref('');
const router = useRouter();

const handleAdd = () => {
  if (!templateName.value || !templateHtml.value) {
    alert('请填写模板名称和HTML代码');
    return;
  }
  // 实际项目中这里应上传到后端或存储到本地
  alert('模板添加成功（仅本地预览，未真正保存）');
  router.push('/templates');
};
</script>

<style scoped lang="scss">
.add-template-page {
  max-width: 600px;
  margin: 40px auto;
  background: #fff;
  border-radius: 8px;
  padding: 32px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.08);
}
.preview-title {
  margin: 24px 0 8px 0;
  font-weight: bold;
  color: #333;
}
.template-preview {
  min-height: 120px;
  border: 1px solid red;
  color: #000;
  font-size: 18px;
  background: #fff !important;
}
</style>