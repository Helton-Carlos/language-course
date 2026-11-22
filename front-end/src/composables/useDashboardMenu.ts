import { Dumbbell, FileText, Gauge, GraduationCap, LayoutDashboard, Shapes, UserX } from 'lucide-vue-next';
import { computed } from 'vue';
import { hasCompleteProfile, useCurrentUser } from '@/composables/useCurrentUser';
import { CONTENTS } from '@/utils/contents';
import { SKILLS } from '@/utils/skills';
import { STUDY_AREAS } from '@/utils/study';
import type { ECSidebarItem } from '@/components/ECSidebar/Type';

const cancelAccountItem: ECSidebarItem = {
  key: 'cancel-account',
  label: 'Cancelar conta',
  icon: UserX,
  to: { name: 'dashboard-cancelar-conta' },
};

export function useDashboardMenu() {
  const { data: user } = useCurrentUser();

  return computed<ECSidebarItem[]>(() => {
    if (user.value && !hasCompleteProfile(user.value)) {
      return [
        { key: 'level', label: 'Definir nível', icon: Gauge, to: { name: 'dashboard-nivel' } },
        cancelAccountItem,
      ];
    }

    return [
      {
        key: 'home',
        label: 'Visão geral',
        icon: LayoutDashboard,
        to: { name: 'dashboard' },
        exact: true,
      },
      {
        key: 'study',
        label: 'Estudo',
        icon: GraduationCap,
        children: STUDY_AREAS.map((area) => ({
          key: `study-${area.key}`,
          label: area.label,
          icon: area.icon,
          to: { name: area.routeName },
        })),
      },
      {
        key: 'practice',
        label: 'Praticar',
        icon: Dumbbell,
        children: SKILLS.map((skill) => ({
          key: `skill-${skill.key}`,
          label: skill.label,
          icon: skill.icon,
          to: { name: skill.routeName },
        })),
      },
      {
        key: 'contents',
        label: 'Conteúdos',
        icon: Shapes,
        children: CONTENTS.map((content) => ({
          key: `content-${content.key}`,
          label: content.label,
          icon: content.icon,
          to: { name: content.routeName },
        })),
      },
      {
        key: 'docs',
        label: 'Documentação',
        icon: FileText,
        to: { name: 'dashboard-documentacao' },
      },
      cancelAccountItem,
    ];
  });
}
