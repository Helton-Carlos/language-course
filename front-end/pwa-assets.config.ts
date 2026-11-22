import { defineConfig, minimal2023Preset } from '@vite-pwa/assets-generator/config';

const BACKGROUND = '#f9cf45';

export default defineConfig({
  preset: {
    ...minimal2023Preset,
    transparent: {
      ...minimal2023Preset.transparent,
      padding: 0,
    },
    maskable: {
      ...minimal2023Preset.maskable,
      padding: 0.2,
      resizeOptions: { background: BACKGROUND, fit: 'contain' },
    },
    apple: {
      ...minimal2023Preset.apple,
      padding: 0,
    },
  },
  images: ['public/pwa-icon-source.svg'],
});