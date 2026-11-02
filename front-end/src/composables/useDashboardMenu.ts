import { computed } from 'vue';
import { hasCompleteProfile, useCurrentUser } from '@/composables/useCurrentUser';
import { CONTENTS } from '@/utils/contents';
import { SKILLS } from '@/utils/skills';
import type { ECSidebarItem } from '@/components/ECSidebar/Type';

const cancelAccountItem: ECSidebarItem = {
  key: 'cancel-account',
  label: 'Cancelar conta',
  to: { name: 'dashboard-cancelar-conta' },
};

export function useDashboardMenu() {
  const { data: user } = useCurrentUser();

  return computed<ECSidebarItem[]>(() => {
    if (user.value && !hasCompleteProfile(user.value)) {
      return [
        { key: 'level', label: 'Definir nível', to: { name: 'dashboard-nivel' } },
        cancelAccountItem,
      ];
    }

    return [
      {
        key: 'home',
        label: 'Visão geral',
        to: { name: 'dashboard' },
        exact: true,
      },
      {
        key: 'practice',
        label: 'Praticar',
        children: SKILLS.map((skill) => ({
          key: `skill-${skill.key}`,
          label: skill.label,
          to: { name: skill.routeName },
        })),
      },
      {
        key: 'contents',
        label: 'Conteúdos',
        children: CONTENTS.map((content) => ({
          key: `content-${content.key}`,
          label: content.label,
          to: { name: content.routeName },
        })),
      },
      {
        key: 'docs',
        label: 'Documentação',
        to: { name: 'dashboard-documentacao' },
      },
      cancelAccountItem,
    ];
  });
}
