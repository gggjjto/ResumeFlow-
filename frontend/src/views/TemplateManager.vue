<template>
  <div class="template-manager">
    <h2>简历模板管理</h2>
    <div class="template-main">
      <!-- 左侧模板列表 -->
      <div class="template-list">
        <div
          v-for="(template, index) in templates"
          :key="template.id"
          class="template-item"
          :class="{ selected: selectedTemplateId === template.id }"
          @click="selectTemplate(template.id)"
        >
          <span
            class="delete-btn"
            @click.stop="removeTemplate(index)"
            title="删除"
          >&#10005;</span>
          <div class="template-name">{{ template.name }}</div>
        </div>
        <div class="add-template">
          <a-input
            v-model="newTemplateName"
            placeholder="新模板名称"
            style="width: 200px; margin-right: 10px;"
          />
          <a-button type="primary" @click="addTemplate">添加模板</a-button>
        </div>
      </div>
      <!-- 右侧预览区域 -->
      <div class="template-preview-panel">
        <div v-if="selectedTemplate">
          <h3>模板预览：{{ selectedTemplate.name }}</h3>
<div class="preview-box">
  <div class="preview-inner" :style="{ background: previewColor(selectedTemplate.name) }">
    <img
      v-if="selectedTemplate.name === '简约风格'"
      src="/t.png"
      alt="简约风格预览"
      class="template-img"
    />
    <img
      v-else-if="selectedTemplate.name === '商务风格'"
      src="/t.png"
      alt="商务风格预览"
      class="template-img"
    />
    <div v-else class="other-template">
      暂无预览
    </div>
  </div>
</div>
        </div>
        <div v-else class="preview-placeholder">
          请选择左侧模板进行预览
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import axios from 'axios'; // 新增

interface Template {
  id: number;
  name: string;
}

const templates = ref<Template[]>([]);
const newTemplateName = ref('');
const selectedTemplateId = ref<number | null>(null);

// 获取模板列表
const fetchTemplates = async () => {
  try {
    const res = await axios.get('/api/template/list');
    templates.value = res.data || [];
  } catch (e) {
    templates.value = [];
  }
};

onMounted(() => {
  fetchTemplates();
});

const addTemplate = async () => {
  if (!newTemplateName.value.trim()) {
    alert('请输入模板名称');
    return;
  }
  try {
    const res = await axios.post('/api/template/add', {
      name: newTemplateName.value
    });
    // 假设返回新模板对象
    templates.value.push(res.data);
    newTemplateName.value = '';
  } catch (e: any) {
    alert(e?.response?.data?.message || '添加模板失败');
  }
};

const removeTemplate = async (index: number) => {
  const template = templates.value[index];
  try {
    await axios.delete(`/api/template/delete/${template.id}`);
    templates.value.splice(index, 1);
    if (
      selectedTemplateId.value &&
      !templates.value.find(t => t.id === selectedTemplateId.value)
    ) {
      selectedTemplateId.value = null;
    }
  } catch (e: any) {
    alert(e?.response?.data?.message || '删除模板失败');
  }
};

const selectTemplate = (id: number) => {
  selectedTemplateId.value = id;
};

const selectedTemplate = computed(() =>
  templates.value.find(t => t.id === selectedTemplateId.value) || null
);

// 示例：根据模板名返回不同预览色
const previewColor = (name: string) => {
  if (name.includes('简约')) return '#f0f0f0';
  if (name.includes('商务')) return '#e6f7ff';
  return '#fffbe6';
};
</script>

<style scoped lang="scss">
.template-manager {
  max-width: 900px;
  margin: 40px auto;
  background: #fff;
  border-radius: 8px;
  padding: 32px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.08);
}
.template-main {
  display: flex;
  gap: 32px;
}
.template-list {
  width: 260px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.template-item {
  border: 2px solid #eee;
  border-radius: 6px;
  padding: 16px 24px;
  cursor: pointer;
  background: #fafbfc;
  display: flex;
  align-items: center;
  min-width: 180px;
  position: relative;
  transition: border-color 0.2s, background 0.2s;
  margin-bottom: 8px;
  &.selected {
    border-color: #1890ff;
    background: #e6f7ff;
  }
  .delete-btn {
    position: absolute;
    top: 8px;
    right: 8px;
    color: #ff4d4f;
    font-size: 18px;
    cursor: pointer;
    z-index: 2;
    transition: color 0.2s;
    &:hover {
      color: #cf1322;
    }
  }
  .template-name {
    font-size: 16px;
    font-weight: 500;
  }
}
.add-template {
  display: flex;
  align-items: center;
  margin-top: 16px;
}
.template-preview-panel {
  flex: 1;
  min-width: 320px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  .preview-box {
    margin-top: 16px;
    width: 550px;
    height: 550px;
    border: 1px dashed #bbb;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #fafbfc;
    .preview-inner {
      width: 90%;
      height: 90%;
      border-radius: 6px;
      border: 1px solid #e0e0e0;
        display: flex;
        align-items: center;
        justify-content: center;
        background: transparent;

        .template-img {
            max-width: 100%;
            max-height: 100%;
            width: auto;
            height: auto;
            object-fit: contain;
            display: block;
            margin: 0 auto;
            border-radius: 4px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
            background: #fff;
        }
    }
  }
  .preview-placeholder {
    color: #aaa;
    font-size: 16px;
    margin-top: 60px;
  }
}
</style>