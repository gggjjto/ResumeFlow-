<template>
  <div class="register-container">
    <div class="register-box">
      <h2>注册</h2>
      <a-form @submit.prevent="handleRegister">
        <a-form-item label="用户名">
          <a-input v-model="username" placeholder="请输入用户名" />
        </a-form-item>
        <a-form-item label="密码">
          <a-input type="password" v-model="password" placeholder="请输入密码" />
        </a-form-item>
        <a-form-item label="确认密码">
          <a-input type="password" v-model="confirmPassword" placeholder="请再次输入密码" />
        </a-form-item>
        <a-form-item>
          <a-button type="primary" html-type="submit" block>注册</a-button>
        </a-form-item>
        <a-form-item>
          <a-button type="link" @click="goLogin" block>已有账号？去登录</a-button>
        </a-form-item>
      </a-form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const username = ref('');
const password = ref('');
const confirmPassword = ref('');
const router = useRouter();

const handleRegister = () => {
  if (!username.value || !password.value || !confirmPassword.value) {
    alert('请填写所有字段');
    return;
  }
  if (password.value !== confirmPassword.value) {
    alert('两次输入的密码不一致');
    return;
  }
  // 实际应调用后端API进行注册
  alert('注册成功！请登录');
  router.push('/login');
};

const goLogin = () => {
  router.push('/login');
};
</script>

<style scoped lang="scss">
.register-container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f5f6fa;
}
.register-box {
  width: 350px;
  padding: 40px 30px;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.08);
}
h2 {
  text-align: center;
  margin-bottom: 24px;
}
</style>