const LOCALE = 'pt-BR';

const mediumDateFormat = new Intl.DateTimeFormat(LOCALE, { dateStyle: 'medium' });
const shortWeekdayFormat = new Intl.DateTimeFormat(LOCALE, { weekday: 'short', timeZone: 'UTC' });

export function formatDate(value: string): string {
  return mediumDateFormat.format(new Date(value));
}

export function formatWeekday(day: string): string {
  return shortWeekdayFormat.format(new Date(`${day}T00:00:00Z`));
}