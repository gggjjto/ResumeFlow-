import { createApp } from 'vue';
import Antd from 'ant-design-vue';
import App from './App.vue';
import router from './router';
import 'ant-design-vue/dist/reset.css';
import './assets/global.css';

const app = createApp(App);
app.use(Antd);
app.use(router);
app.mount('#app');
