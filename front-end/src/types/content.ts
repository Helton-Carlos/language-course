export interface PodcastEpisode {
  id: string;
  title: string;
  youtube_id: string;
}

export type PhraseKind = 'phrase' | 'slang';

export interface Phrase {
  id: string;
  kind: PhraseKind;
  text: string;
  translation: string;
}
