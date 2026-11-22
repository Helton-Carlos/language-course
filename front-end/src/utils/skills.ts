import { BookOpen, Headphones, Mic, PenLine } from 'lucide-vue-next';

export const SKILLS = [
  {
    key: 'ler',
    label: 'Ler',
    description: 'Textos curtos e longos para ampliar o vocabulário e entender o idioma escrito.',
    path: 'ler',
    routeName: 'dashboard-ler',
    icon: BookOpen,
  },
  {
    key: 'escrever',
    label: 'Escrever',
    description: 'Monte frases e pequenos textos para fixar a gramática e a ortografia.',
    path: 'escrever',
    routeName: 'dashboard-escrever',
    icon: PenLine,
  },
  {
    key: 'escutar',
    label: 'Escutar',
    description: 'Áudios e diálogos para treinar o ouvido e entender o idioma falado.',
    path: 'escutar',
    routeName: 'dashboard-escutar',
    icon: Headphones,
  },
  {
    key: 'falar',
    label: 'Falar',
    description: 'Pratique a pronúncia e a conversação com situações do dia a dia.',
    path: 'falar',
    routeName: 'dashboard-falar',
    icon: Mic,
  },
] as const;

export type Skill = (typeof SKILLS)[number];
export type SkillKey = Skill['key'];
