<template>
  <div class="login-container">
    <div class="login-box">
      <h2>登录</h2>
      <a-form @submit.prevent="handleLogin">
        <a-form-item label="用户名">
          <a-input v-model="username" placeholder="请输入用户名" />
        </a-form-item>
        <a-form-item label="密码">
          <a-input type="password" v-model="password" placeholder="请输入密码" />
        </a-form-item>
        <a-form-item>
          <a-button type="primary" html-type="submit" block>登录</a-button>
        </a-form-item>
      </a-form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios'; // 新增

const username = ref('');
const password = ref('');
const router = useRouter();

const handleLogin = async () => {
  if (!username.value || !password.value) {
    alert('请输入用户名和密码');
    return;
  }
  try {
    await axios.post('/api/auth/login', {
      username: username.value,
      password: password.value
    });
    router.push('/');
  } catch (e: any) {
    alert(e?.response?.data?.message || '登录失败，请重试');
  }
};
</script>

<style scoped lang="scss">
.login-container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f5f6fa;
}
.login-box {
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