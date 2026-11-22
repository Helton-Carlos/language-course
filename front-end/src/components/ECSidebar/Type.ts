import type { LucideIcon } from 'lucide-vue-next';
import type { RouteLocationRaw } from 'vue-router';

export interface ECSidebarItem {
  key: string;
  label: string;
  to?: RouteLocationRaw;
  icon?: LucideIcon;
  exact?: boolean;
  children?: ECSidebarItem[];
}

export interface ECSidebar {
  items: ECSidebarItem[];
  title?: string;
}
