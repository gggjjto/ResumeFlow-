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
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;

