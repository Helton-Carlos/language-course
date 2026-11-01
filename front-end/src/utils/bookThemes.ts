export const BOOK_THEMES = [
  {
    key: 'trabalho',
    label: 'Trabalho',
    description: 'Carreira, negócios e o vocabulário do dia a dia profissional.',
  },
  {
    key: 'cultura',
    label: 'Cultura',
    description: 'Arte, história, música e as tradições de quem fala o idioma.',
  },
  {
    key: 'tecnologia',
    label: 'Tecnologia',
    description: 'Inovação, ciência e o mundo digital.',
  },
  {
    key: 'noticias',
    label: 'Notícias',
    description: 'Atualidades e a linguagem usada no jornalismo.',
  },
  {
    key: 'viagem',
    label: 'Viagem',
    description: 'Destinos, roteiros e situações que você vai encontrar viajando.',
  },
  {
    key: 'nativos',
    label: 'Nativos',
    description: 'Leituras escritas para falantes nativos, sem adaptação.',
  },
] as const;

export type BookTheme = (typeof BOOK_THEMES)[number];
export type BookThemeKey = BookTheme['key'];

export function isBookTheme(value: unknown): value is BookThemeKey {
  return BOOK_THEMES.some((theme) => theme.key === value);
}
