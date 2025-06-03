import { createRouter, createWebHistory } from 'vue-router';
import ResumeBuilder from '../views/ResumeBuilder.vue';
const routes = [
  {
    path: '/',
    name: 'ResumeBuilder',
    component: ResumeBuilder
  },
  {
    path: '/preview',
    name: 'ResumePreview',
    component: () => import('../views/ResumePreview.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('../views/Register.vue')
  },
  {
    path: '/templates',
    name: 'TemplateManager',
    component: () => import('../views/TemplateManager.vue')
  },
  {
    path: '/add-template',
    name: 'AddTemplate',
    component: () => import('../views/AddTemplate.vue')
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;

