import type { RouteLocationRaw } from 'vue-router';

export type ECBackButtonVariant = 'link' | 'button';

export interface ECBackButton {
  to?: RouteLocationRaw;
  variant?: ECBackButtonVariant;
}
