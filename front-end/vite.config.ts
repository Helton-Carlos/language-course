import vue from '@vitejs/plugin-vue';
import { fileURLToPath, URL } from 'node:url';
import { defineConfig } from 'vite';
import { VitePWA } from 'vite-plugin-pwa';
import tailwindcss from '@tailwindcss/vite';

const THEME_COLOR = '#f9cf45';
const BACKGROUND_COLOR = '#ebebeb';
const FLAGS_CACHE_MAX_ENTRIES = 60;
const FLAGS_CACHE_MAX_AGE_SECONDS = 60 * 60 * 24 * 30;

export default defineConfig({
  plugins: [
    vue(),
    tailwindcss(),
    VitePWA({
      registerType: 'autoUpdate',
      includeAssets: ['favicon.ico', 'apple-touch-icon-180x180.png', 'icon-logo.svg'],
      manifest: {
        name: 'Language Course',
        short_name: 'Language',
        description: 'Aprenda inglês com leitura interativa, vocabulário e revisão.',
        lang: 'pt-BR',
        start_url: '/',
        scope: '/',
        display: 'standalone',
        orientation: 'portrait',
        categories: ['education'],
        theme_color: THEME_COLOR,
        background_color: BACKGROUND_COLOR,
        icons: [
          { src: 'pwa-64x64.png', sizes: '64x64', type: 'image/png' },
          { src: 'pwa-192x192.png', sizes: '192x192', type: 'image/png' },
          { src: 'pwa-512x512.png', sizes: '512x512', type: 'image/png' },
          { src: 'maskable-icon-512x512.png', sizes: '512x512', type: 'image/png', purpose: 'maskable' },
        ],
      },
      workbox: {
        globPatterns: ['**/*.{js,css,html,svg,png,ico}'],
        globIgnores: ['**/pwa-icon-source.svg'],
        navigateFallback: '/index.html',
        navigateFallbackDenylist: [/^\/api\//],
        cleanupOutdatedCaches: true,
        runtimeCaching: [
          {
            urlPattern: /^https:\/\/flagcdn\.com\/.*/,
            handler: 'CacheFirst',
            options: {
              cacheName: 'flags',
              expiration: {
                maxEntries: FLAGS_CACHE_MAX_ENTRIES,
                maxAgeSeconds: FLAGS_CACHE_MAX_AGE_SECONDS,
              },
              cacheableResponse: { statuses: [0, 200] },
            },
          },
        ],
      },
    }),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
  server: {
    open: true,
    port: 3001,
  },
});