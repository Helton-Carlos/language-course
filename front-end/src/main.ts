import { createApp } from 'vue';
import App from '@/App.vue';
import { createPinia } from 'pinia'
import { VueQueryPlugin } from '@tanstack/vue-query';
import { router } from '@/routes/index.ts';

import '@/style.css';
const pinia = createPinia()
const app = createApp(App);

app.use(router).use(pinia).use(VueQueryPlugin);
app.mount('#app');
