import { createApp } from 'vue';
import App from '@/App.vue';
import { VueQueryPlugin } from '@tanstack/vue-query';
import { queryClient } from '@/plugins/queryClient';
import { router } from '@/routes/index.ts';

import '@/style.css';
const app = createApp(App);

app.use(router).use(VueQueryPlugin, { queryClient });
app.mount('#app');
