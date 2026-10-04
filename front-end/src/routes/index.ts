import { createMemoryHistory, createRouter } from 'vue-router';

import Init from '../view/Init.vue';

const routes = [{ path: '/', component: Init }];

export const router = createRouter({
  history: createMemoryHistory(),
  routes,
});
