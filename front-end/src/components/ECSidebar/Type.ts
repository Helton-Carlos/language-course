import type { RouteLocationRaw } from 'vue-router';

export interface ECSidebarItem {
  key: string;
  label: string;
  to?: RouteLocationRaw;
  icon?: string;
  exact?: boolean;
  children?: ECSidebarItem[];
}

export interface ECSidebar {
  items: ECSidebarItem[];
  title?: string;
}
