import { createWebHistory, createRouter, type RouteRecordRaw } from 'vue-router';

import Index from '@/view/Index.vue';
import { isBookTheme } from '@/utils/bookThemes';
import { SKILLS, type SkillKey } from '@/utils/skills';
import { currentUserQuery, hasCompleteProfile } from '@/composables/useCurrentUser';
import { queryClient } from '@/plugins/queryClient';

declare module 'vue-router' {
  interface RouteMeta {
    title?: string;
    requiresAuth?: boolean;
    requiresProfile?: boolean;
    guestOnly?: boolean;
    skill?: SkillKey;
  }
}

const PROFILE_REQUIRED = { requiresProfile: true } as const;

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
    path: '/dashboard',
    component: () => import('@/view/Dashboard.vue'),
    meta: { requiresAuth: true },
    children: [
      {
        path: 'escolher-idioma',
        name: 'escolher-idioma',
        component: () => import('@/view/ChooseLanguage.vue'),
      },
      {
        path: 'escolher-idioma/:id/nivel',
        name: 'escolher-nivel',
        component: () => import('@/view/Init.vue'),
      },
      {
        path: 'escolher-idioma/:id/teste',
        name: 'teste-nivel',
        component: () => import('@/view/PlacementTest.vue'),
      },
      {
        path: '',
        name: 'dashboard',
        component: () => import('@/view/DashboardHome.vue'),
        meta: PROFILE_REQUIRED,
      },
      {
        path: 'idiomas',
        name: 'dashboard-idiomas',
        component: () => import('@/view/Languages.vue'),
        meta: PROFILE_REQUIRED,
      },
      {
        path: 'documentacao',
        name: 'dashboard-documentacao',
        component: () => import('@/view/Documentacao.vue'),
        meta: PROFILE_REQUIRED,
      },
      ...SKILLS.map((skill): RouteRecordRaw => ({
        path: skill.path,
        name: skill.routeName,
        component: () => import('@/view/SkillPage.vue'),
        meta: { ...PROFILE_REQUIRED, skill: skill.key },
      })),
      {
        path: 'livros',
        name: 'dashboard-livros',
        component: () => import('@/view/BooksPage.vue'),
        meta: PROFILE_REQUIRED,
      },
      {
        path: 'livros/:tema',
        name: 'dashboard-livros-tema',
        component: () => import('@/view/BookThemePage.vue'),
        meta: PROFILE_REQUIRED,
        beforeEnter: (to) => isBookTheme(to.params.tema) || { name: 'dashboard-livros' },
      },
      {
        path: 'podcast',
        name: 'dashboard-podcast',
        component: () => import('@/view/PodcastPage.vue'),
        meta: PROFILE_REQUIRED,
      },
      {
        path: 'frases',
        name: 'dashboard-frases',
        component: () => import('@/view/PhrasesPage.vue'),
        meta: PROFILE_REQUIRED,
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
