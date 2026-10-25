import { createWebHistory, createRouter } from 'vue-router';

import Index from '@/view/Index.vue';

const routes = [
  {
    path: '/',
    name: 'index',
    component: Index,
  },
  {
    path: '/documentacao',
    name: 'documentacao',
    component: () => import('@/view/Documentacao.vue'),
  },
  {
    path: '/criar-conta',
    name: 'criar-conta',
    component: () => import('@/view/CreateAccount.vue'),
  },
  {
    path: '/idiomas',
    name: 'idiomas',
    component: () => import('@/view/Languages.vue'),
  },
  {
    path: '/init/:id',
    name: 'init',
    component: () => import('@/view/Init.vue'),
  },
   {
    path: '/login',
    name: 'login',
    component: () => import('@/view/Login.vue'),
    meta: {
      title: 'Login'
    }
  },
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});
