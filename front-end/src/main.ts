import { createApp } from 'vue';
import { registerSW } from 'virtual:pwa-register';
import App from '@/App.vue';
import { VueQueryPlugin } from '@tanstack/vue-query';
import { toast } from '@/composables/useToast';
import { queryClient } from '@/plugins/queryClient';
import { router } from '@/routes/index.ts';

import { MESSAGES } from '@/utils/message';
import '@/style.css';
const app = createApp(App);

app.use(router).use(VueQueryPlugin, { queryClient });
app.mount('#app');

registerSW({
  immediate: true,
  onOfflineReady() {
    toast.info(MESSAGES.success.pwaOfflineReady);
  },
});
