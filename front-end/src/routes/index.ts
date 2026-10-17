import { createWebHistory, createRouter } from 'vue-router';

import Index from '@/view/Index.vue';

const routes = [
  {
    path: '/',
    name: 'index',
    component: Index,
    meta: {
      title: 'Escolha o idioma que você quer aprender'
    }
  },
  {
    path: '/init',
    name: 'init',
    component: () => import('@/view/Init.vue'),
  }
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});
