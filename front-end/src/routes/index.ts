import { createWebHistory, createRouter, type RouteRecordRaw } from 'vue-router';

import Index from '@/view/Index.vue';
import { currentUserQuery, hasCompleteProfile } from '@/composables/useCurrentUser';
import { queryClient } from '@/plugins/queryClient';

declare module 'vue-router' {
  interface RouteMeta {
    title?: string;
    requiresAuth?: boolean;
    requiresProfile?: boolean;
    guestOnly?: boolean;
  }
}

const routes: RouteRecordRaw[] = [
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
    meta: { guestOnly: true },
  },
  {
    path: '/idiomas',
    name: 'idiomas',
    component: () => import('@/view/Languages.vue'),
  },
  {
    path: '/escolher-idioma',
    name: 'escolher-idioma',
    component: () => import('@/view/ChooseLanguage.vue'),
    meta: { requiresAuth: true },
  },
  {
    path: '/escolher-idioma/:id/nivel',
    name: 'escolher-nivel',
    component: () => import('@/view/Init.vue'),
    meta: { requiresAuth: true },
  },
  {
    path: '/escolher-idioma/:id/teste',
    name: 'teste-nivel',
    component: () => import('@/view/PlacementTest.vue'),
    meta: { requiresAuth: true },
  },
  {
    path: '/dashboard',
    component: () => import('@/view/Dashboard.vue'),
    meta: { requiresAuth: true, requiresProfile: true },
    children: [
      {
        path: '',
        name: 'dashboard',
        component: () => import('@/view/DashboardHome.vue'),
      },
      {
        path: 'idiomas',
        name: 'dashboard-idiomas',
        component: () => import('@/view/Languages.vue'),
      },
      {
        path: 'documentacao',
        name: 'dashboard-documentacao',
        component: () => import('@/view/Documentacao.vue'),
      },
    ],
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/view/Login.vue'),
    meta: {
      title: 'Login',
      guestOnly: true,
    },
  },
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach(async (to) => {
  const requiresAuth = to.matched.some((record) => record.meta.requiresAuth);
  const requiresProfile = to.matched.some((record) => record.meta.requiresProfile);
  const guestOnly = to.matched.some((record) => record.meta.guestOnly);

  if (!requiresAuth && !guestOnly) return true;

  const user = await queryClient.fetchQuery(currentUserQuery).catch(() => null);

  if (requiresAuth && !user) return { name: 'login' };
  if (guestOnly && user) return { name: 'dashboard' };
  if (requiresProfile && user && !hasCompleteProfile(user)) return { name: 'escolher-idioma' };

  return true;
});
