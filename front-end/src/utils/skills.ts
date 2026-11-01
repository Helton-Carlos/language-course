export const SKILLS = [
  {
    key: 'ler',
    label: 'Ler',
    description: 'Textos curtos e longos para ampliar o vocabulário e entender o idioma escrito.',
    path: 'ler',
    routeName: 'dashboard-ler',
    icon: 'M12 6.5C10.5 5.3 8.5 4.7 6 4.7H3v13h3c2.5 0 4.5.6 6 1.8 1.5-1.2 3.5-1.8 6-1.8h3v-13h-3c-2.5 0-4.5.6-6 1.8Z',
  },
  {
    key: 'escrever',
    label: 'Escrever',
    description: 'Monte frases e pequenos textos para fixar a gramática e a ortografia.',
    path: 'escrever',
    routeName: 'dashboard-escrever',
    icon: 'M3 17.25V21h3.75L17.8 9.94l-3.75-3.75L3 17.25Zm17.7-10.2a1 1 0 0 0 0-1.4l-2.35-2.35a1 1 0 0 0-1.4 0l-1.83 1.83 3.75 3.75 1.83-1.83Z',
  },
  {
    key: 'escutar',
    label: 'Escutar',
    description: 'Áudios e diálogos para treinar o ouvido e entender o idioma falado.',
    path: 'escutar',
    routeName: 'dashboard-escutar',
    icon: 'M12 1a9 9 0 0 0-9 9v7a3 3 0 0 0 3 3h3v-8H5v-2a7 7 0 0 1 14 0v2h-4v8h3a3 3 0 0 0 3-3v-7a9 9 0 0 0-9-9Z',
  },
  {
    key: 'falar',
    label: 'Falar',
    description: 'Pratique a pronúncia e a conversação com situações do dia a dia.',
    path: 'falar',
    routeName: 'dashboard-falar',
    icon: 'M12 14a3 3 0 0 0 3-3V5a3 3 0 0 0-6 0v6a3 3 0 0 0 3 3Zm5-3a5 5 0 0 1-10 0H5a7 7 0 0 0 6 6.9V21h2v-3.1A7 7 0 0 0 19 11h-2Z',
  },
] as const;

export type Skill = (typeof SKILLS)[number];
export type SkillKey = Skill['key'];
