import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  site: 'https://thanhnguyxn.github.io',
  base: '/awesome-free-apis',
  integrations: [
    starlight({
      title: 'Awesome Free APIs',
      description: 'A curated collection of awesome free APIs for developers. Find the perfect API for your next project.',
      logo: {
        src: './public/logo.png',
        alt: 'Awesome Free APIs Logo',
      },
      favicon: '/favicon.png',
      social: [
        { icon: 'github', label: 'GitHub', href: 'https://github.com/ThanhNguyxn/awesome-free-apis' },
      ],
      editLink: {
        baseUrl: 'https://github.com/ThanhNguyxn/awesome-free-apis/edit/main/docs-site/',
      },
      head: [
        {
          tag: 'meta',
          attrs: { property: 'og:image', content: 'https://thanhnguyxn.github.io/awesome-free-apis/og-image.png' },
        },
        {
          tag: 'meta',
          attrs: { name: 'twitter:card', content: 'summary_large_image' },
        },
      ],
      customCss: ['./src/styles/custom.css'],
      sidebar: [
        {
          label: 'Getting Started',
          items: [
            { label: 'API Usage Guide', link: '/guide/getting-started/' },
            { label: 'Code Examples', link: '/examples/' },
          ],
        },
        {
          label: 'API Categories',
          autogenerate: { directory: 'apis' },
        },
      ],
      lastUpdated: true,
      pagination: true,
      tableOfContents: { minHeadingLevel: 2, maxHeadingLevel: 3 },
    }),
  ],
});
