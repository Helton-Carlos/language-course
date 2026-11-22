import { BookMarked, ChartColumn, Library, Repeat } from 'lucide-vue-next';

export const STUDY_AREAS = [
  {
    key: 'biblioteca',
    label: 'Biblioteca',
    description: 'Leia textos por tema ou importe o seu próprio texto em inglês e clique nas palavras novas.',
    path: 'biblioteca',
    routeName: 'dashboard-biblioteca',
    icon: Library,
  },
  {
    key: 'vocabulario',
    label: 'Vocabulário',
    description: 'Veja todas as palavras salvas, filtre por nível de conhecimento e edite os significados.',
    path: 'vocabulario',
    routeName: 'dashboard-vocabulario',
    icon: BookMarked,
  },
  {
    key: 'revisar',
    label: 'Revisar',
    description: 'Cartões de memorização com repetição espaçada para fixar as palavras salvas.',
    path: 'revisar',
    routeName: 'dashboard-revisar',
    icon: Repeat,
  },
  {
    key: 'estatisticas',
    label: 'Estatísticas',
    description: 'Acompanhe sua sequência de dias, a meta diária, palavras lidas e conhecidas.',
    path: 'estatisticas',
    routeName: 'dashboard-estatisticas',
    icon: ChartColumn,
  },
] as const;

export type StudyArea = (typeof STUDY_AREAS)[number];
