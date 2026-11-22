import type { LucideIcon } from 'lucide-vue-next';
import type { RouteLocationRaw } from 'vue-router';

export interface ECFeatureCard {
  to: RouteLocationRaw;
  title: string;
  description: string;
  icon?: LucideIcon;
}
