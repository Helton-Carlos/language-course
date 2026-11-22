import { BookText, MessageSquareQuote, Podcast } from 'lucide-vue-next';

export const CONTENTS = [
  {
    key: 'livros',
    label: 'Ler um livro',
    description: 'Escolha um tema e leia no ritmo que combina com você.',
    routeName: 'dashboard-livros',
    path: 'livros',
    icon: BookText,
  },
  {
    key: 'podcast',
    label: 'Podcast',
    description: 'Vídeos de conversas reais para treinar o ouvido no seu idioma.',
    routeName: 'dashboard-podcast',
    path: 'podcast',
    icon: Podcast,
  },
  {
    key: 'frases',
    label: 'Frases e gírias',
    description: 'Expressões do dia a dia no idioma, com a tradução logo abaixo.',
    routeName: 'dashboard-frases',
    path: 'frases',
    icon: MessageSquareQuote,
  },
] as const;
