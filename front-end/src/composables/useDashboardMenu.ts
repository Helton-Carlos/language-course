import { computed } from 'vue';
import { useLanguages } from '@/composables/useLanguages';
import type { ECSidebarItem } from '@/components/ECSidebar/Type';

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
      key: 'languages',
      label: 'Idiomas',
      to: { name: 'dashboard-idiomas' },
      children: languages.value.map((language) => ({
        key: `language-${language.id}`,
        label: language.name_pt,
        to: { name: 'escolher-nivel', params: { id: language.id } },
        icon: `https://flagcdn.com/${language.prefix.toLowerCase()}.svg`,
      })),
    },
    {
      key: 'docs',
      label: 'Documentação',
      to: { name: 'dashboard-documentacao' },
    },
  ]);
}
