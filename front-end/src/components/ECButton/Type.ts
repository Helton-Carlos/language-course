export type ECButtonColor = 'primary' | 'secondary';

export interface ECButton {
  title?: string;
  color?: ECButtonColor;
  type?: 'button' | 'submit' | 'reset';
  disabled?: boolean;
}
