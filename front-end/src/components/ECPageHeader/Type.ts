import type { LucideIcon } from 'lucide-vue-next';
import type { RouteLocationRaw } from 'vue-router';

export interface ECPageHeader {
  title?: string;
  description?: string;
  backTo?: RouteLocationRaw;
  icon?: LucideIcon;
}