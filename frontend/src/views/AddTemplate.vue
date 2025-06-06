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
import axios from 'axios'; // 新增

const templateName = ref('');
const templateHtml = ref('');
const router = useRouter();

const handleAdd = async () => {
  if (!templateName.value || !templateHtml.value) {
    alert('请填写模板名称和HTML代码');
    return;
  }
  try {
    await axios.post('/api/template/add', {
      name: templateName.value,
      html: templateHtml.value
    });
    alert('模板添加成功');
    router.push('/templates');
  } catch (e: any) {
    alert(e?.response?.data?.message || '模板添加失败，请重试');
  }
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