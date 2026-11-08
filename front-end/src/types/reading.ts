export interface ReadingTheme {
  key: string;
  label: string;
  description: string;
}

export interface ReadingSituation {
  key: string;
  title: string;
  description: string;
}

export interface ReadingText {
  theme: string;
  situation: string;
  title: string;
  body: string;
}
