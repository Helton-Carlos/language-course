import { createWebHistory, createRouter } from 'vue-router';

import Index from '../view/Index.vue';

const routes = [
  {
    path: '/',
    name: 'index',
    component: Index
  },
  {
    path: '/init',
    name: 'init',
    component: () => import('../view/Init.vue')
  }
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});
