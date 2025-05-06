<template>
  <div>
    <h2>技能专长</h2>
    <div class="skill-tips">
      <p class="tip-text">技能描述示例：</p>
      <ul>
        <li>熟练掌握 Vue3、React 等主流前端框架，有3年以上开发经验</li>
        <li>精通 TypeScript，具备良好的工程化思维</li>
        <li>深入理解浏览器原理和网络协议，能够进行性能优化</li>
      </ul>
    </div>
    <a-form-item>
      <a-textarea
        v-model:value="localSkillText"
        :rows="8"
        placeholder="请输入您的技能专长描述，每行一项"
        :auto-size="{ minRows: 8, maxRows: 15 }"
      />
    </a-form-item>
    <div class="form-tips">
      <p>* 每行将作为一项技能描述</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';

const props = defineProps<{
  modelValue: string[];
}>();

const emit = defineEmits(['update:modelValue']);

const localSkillText = ref(props.modelValue.join('\n'));

watch(localSkillText, (newValue) => {
  const skills = newValue.split('\n').filter(skill => skill.trim());
  emit('update:modelValue', skills);
});
</script>

<style scoped>
.skill-tips {
  margin-bottom: 16px;
  padding: 20px;
  background: #f5f5f5;
  border-radius: 4px;
}

.tip-text {
  color: #666;
  margin-bottom: 8px;
}
</style>
