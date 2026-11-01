import type { RouteLocationRaw } from 'vue-router';

export interface ECFeatureCard {
  to: RouteLocationRaw;
  title: string;
  description: string;
  icon?: string;
}
