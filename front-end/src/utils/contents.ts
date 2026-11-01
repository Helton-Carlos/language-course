export const CONTENTS = [
  {
    key: 'livros',
    label: 'Ler um livro',
    description: 'Escolha um tema e leia no ritmo que combina com você.',
    routeName: 'dashboard-livros',
    path: 'livros',
    icon: 'M6 2h12a2 2 0 0 1 2 2v16a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2Zm1 2v9l2.5-1.8L12 13V4H7Z',
  },
  {
    key: 'podcast',
    label: 'Podcast',
    description: 'Vídeos de conversas reais para treinar o ouvido no seu idioma.',
    routeName: 'dashboard-podcast',
    path: 'podcast',
    icon: 'M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20Zm-2 5.5 7 4.5-7 4.5v-9Z',
  },
  {
    key: 'frases',
    label: 'Frases e gírias',
    description: 'Expressões do dia a dia no idioma, com a tradução logo abaixo.',
    routeName: 'dashboard-frases',
    path: 'frases',
    icon: 'M4 4h16a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H9l-5 4v-4H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2Z',
  },
] as const;
