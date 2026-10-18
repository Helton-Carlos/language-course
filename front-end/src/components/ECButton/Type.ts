export type ECButtonColor = 'primary' | 'secondary' | 'border';

export interface ECButton {
  color?: ECButtonColor;
  type?: 'button' | 'submit' | 'reset';
  disabled?: boolean;
}
