import { computed } from 'vue';
import { useLanguages } from '@/composables/useLanguages';
import { CONTENTS } from '@/utils/contents';
import { SKILLS } from '@/utils/skills';
import type { ECSidebarItem } from '@/components/ECSidebar/Type';

function capitalize(text: string): string {
  return text.charAt(0).toUpperCase() + text.slice(1);
}

export function useDashboardMenu() {
  const { languages } = useLanguages();

  return computed<ECSidebarItem[]>(() => [
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
    {
      key: 'languages',
      label: 'Idiomas',
      to: { name: 'dashboard-idiomas' },
      children: languages.value.map((language) => ({
        key: `language-${language.id}`,
        label: capitalize(language.name_pt),
        to: { name: 'escolher-nivel', params: { id: language.id } },
        icon: `https://flagcdn.com/${language.prefix.toLowerCase()}.svg`,
      })),
    },
  ]);
}
