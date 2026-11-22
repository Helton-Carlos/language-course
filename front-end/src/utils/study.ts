export const STUDY_AREAS = [
  {
    key: 'biblioteca',
    label: 'Biblioteca',
    description: 'Leia textos por tema ou importe o seu próprio texto em inglês e clique nas palavras novas.',
    path: 'biblioteca',
    routeName: 'dashboard-biblioteca',
    icon: 'M4 4h4v16H4V4Zm6 0h4v16h-4V4Zm6.3.6 3.8-1 3.1 15.6-3.9.8-3-15.4Z',
  },
  {
    key: 'vocabulario',
    label: 'Vocabulário',
    description: 'Veja todas as palavras salvas, filtre por nível de conhecimento e edite os significados.',
    path: 'vocabulario',
    routeName: 'dashboard-vocabulario',
    icon: 'M3 5h18v2H3V5Zm0 6h18v2H3v-2Zm0 6h12v2H3v-2Z',
  },
  {
    key: 'revisar',
    label: 'Revisar',
    description: 'Cartões de memorização com repetição espaçada para fixar as palavras salvas.',
    path: 'revisar',
    routeName: 'dashboard-revisar',
    icon: 'M12 5V2L7 6l5 4V7a5 5 0 1 1-5 5H5a7 7 0 1 0 7-7Z',
  },
  {
    key: 'estatisticas',
    label: 'Estatísticas',
    description: 'Acompanhe sua sequência de dias, a meta diária, palavras lidas e conhecidas.',
    path: 'estatisticas',
    routeName: 'dashboard-estatisticas',
    icon: 'M5 20V10h4v10H5Zm5 0V4h4v16h-4Zm5 0v-7h4v7h-4Z',
  },
] as const;

export type StudyArea = (typeof STUDY_AREAS)[number];
