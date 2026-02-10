#!/usr/bin/env node

import { readFileSync, writeFileSync, mkdirSync, existsSync, readdirSync, unlinkSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const ROOT = join(__dirname, '..');
const README_PATH = join(ROOT, 'README.md');
const DOCS_OUTPUT = join(ROOT, 'docs-site', 'src', 'content', 'docs', 'apis');
const INDEX_OUTPUT = join(ROOT, 'docs-site', 'src', 'content', 'docs', 'index.mdx');
const GUIDE_OUTPUT = join(ROOT, 'docs-site', 'src', 'content', 'docs', 'guide', 'getting-started.mdx');
const EXAMPLES_OUTPUT = join(ROOT, 'docs-site', 'src', 'content', 'docs', 'examples', 'index.mdx');

const CATEGORY_ORDER = [
  'animals', 'anime', 'anti-malware', 'books', 'cryptocurrency',
  'development', 'dictionaries', 'education', 'public-data', 'email-sms',
  'entertainment', 'finance', 'food-drink', 'games-comics', 'geocoding',
  'health', 'machine-learning', 'mock-data-testing', 'music', 'news',
  'photography', 'science', 'security-validation', 'shopping', 'utilities-tools',
  'social', 'sports', 'design-colors', 'geography-countries', 'transportation',
  'unofficial-community', 'memes-fun', 'jobs-career', 'weather'
];

function parseReadme() {
  const content = readFileSync(README_PATH, 'utf-8').replace(/\r\n/g, '\n');
  const categories = [];
  const categoryRegex = /^## <a id="([^"]+)"><\/a>\s*(.+)$/gm;

  let match;
  const matches = [];
  while ((match = categoryRegex.exec(content)) !== null) {
    matches.push({ id: match[1], title: match[2].trim(), index: match.index });
  }

  for (let i = 0; i < matches.length; i++) {
    if (matches[i].id === 'general-api-usage-guide') continue;

    const start = matches[i].index;
    const end = i + 1 < matches.length ? matches[i + 1].index : content.length;
    const section = content.substring(start, end);

    const apis = parseApiTable(section);
    const extraContent = parseExtraContent(section);

    categories.push({
      id: matches[i].id,
      title: matches[i].title,
      apis,
      extraContent,
    });
  }

  return categories;
}

function parseApiTable(section) {
  const apis = [];
  const lines = section.split('\n');

  for (const line of lines) {
    const rowMatch = line.match(
      /^\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*\[Link\]\((.+?)\)\s*\|/
    );
    if (rowMatch) {
      const [, name, description, auth, https, url] = rowMatch;
      apis.push({
        name: name.trim(),
        description: description.trim(),
        auth: normalizeAuth(auth.trim()),
        authRaw: auth.trim(),
        https: https.trim() === '✅',
        url: url.trim(),
      });
    }
  }

  return apis;
}

function parseExtraContent(section) {
  const lines = section.split('\n');
  const extras = [];

  let inDisclaimer = false;
  for (const line of lines) {
    if (line.startsWith('> **⚠️ Important Disclaimer:**')) {
      inDisclaimer = true;
    }
    if (inDisclaimer) {
      extras.push(line);
      if (line.trim() === '' && extras.length > 2) {
        const nextIdx = lines.indexOf(line) + 1;
        if (nextIdx < lines.length && !lines[nextIdx].startsWith('>')) {
          inDisclaimer = false;
        }
      }
    }
    if (line.startsWith('**🔍 How to find instances:**') || line.startsWith('**💡 Self-hosting recommended:**')) {
      extras.push(line);
    }
  }

  return extras.length > 0 ? extras.join('\n').trim() : null;
}

function normalizeAuth(auth) {
  if (auth === 'No') return 'none';
  if (auth.includes('ApiKey')) return 'apikey';
  if (auth.includes('OAuth')) return 'oauth';
  return 'none';
}

function getAuthBadge(auth, authRaw) {
  switch (auth) {
    case 'none':
      return '<span class="auth-badge auth-badge--none">🌐 No Auth</span>';
    case 'apikey':
      return '<span class="auth-badge auth-badge--apikey">🔑 API Key</span>';
    case 'oauth':
      return '<span class="auth-badge auth-badge--oauth">🔐 OAuth</span>';
    default:
      return authRaw;
  }
}

function getHttpsBadge(https) {
  return https
    ? '<span class="https-yes">✅ Yes</span>'
    : '<span class="https-no">❌ No</span>';
}

function getEmojiFromTitle(title) {
  const emojiMatch = title.match(/^(\p{Emoji_Presentation}|\p{Extended_Pictographic})/u);
  return emojiMatch ? emojiMatch[0] : '📦';
}

function getCleanTitle(title) {
  return title.replace(/^(\p{Emoji_Presentation}|\p{Extended_Pictographic})\s*/u, '').trim();
}

function slugify(id) {
  return id.toLowerCase().replace(/[^a-z0-9-]/g, '-');
}

function generateCategoryMdx(category, sortOrder) {
  const emoji = getEmojiFromTitle(category.title);
  const cleanTitle = getCleanTitle(category.title);
  const authStats = {
    none: category.apis.filter(a => a.auth === 'none').length,
    apikey: category.apis.filter(a => a.auth === 'apikey').length,
    oauth: category.apis.filter(a => a.auth === 'oauth').length,
  };

  let mdx = `---
title: "${emoji} ${cleanTitle}"
description: "Browse ${category.apis.length} free ${cleanTitle} APIs - ${cleanTitle.toLowerCase()} APIs for developers."
sidebar:
  order: ${sortOrder}
  badge:
    text: "${category.apis.length}"
    variant: tip
---

`;

  if (category.extraContent) {
    mdx += category.extraContent + '\n\n';
  }

  mdx += `<div class="stats-grid">
  <div class="stat-card">
    <span class="stat-number">${category.apis.length}</span>
    <span class="stat-label">Total APIs</span>
  </div>
  <div class="stat-card">
    <span class="stat-number">${authStats.none}</span>
    <span class="stat-label">No Auth</span>
  </div>
  <div class="stat-card">
    <span class="stat-number">${authStats.apikey}</span>
    <span class="stat-label">API Key</span>
  </div>
  <div class="stat-card">
    <span class="stat-number">${authStats.oauth}</span>
    <span class="stat-label">OAuth</span>
  </div>
</div>

`;

  mdx += `| API Name | Description | Auth | HTTPS | Link |\n`;
  mdx += `| :--- | :--- | :---: | :---: | :---: |\n`;

  for (const api of category.apis) {
    const authBadge = getAuthBadge(api.auth, api.authRaw);
    const httpsBadge = getHttpsBadge(api.https);
    const desc = api.description.replace(/\|/g, '\\|');
    mdx += `| **${api.name}** | ${desc} | ${authBadge} | ${httpsBadge} | [Docs →](${api.url}) |\n`;
  }

  mdx += `\n---\n\n`;
  mdx += `<p style="text-align: center; opacity: 0.7; font-size: 0.85rem;">`;
  mdx += `Data sourced from <a href="https://github.com/ThanhNguyxn/awesome-free-apis">awesome-free-apis</a> README`;
  mdx += `</p>\n`;

  return mdx;
}

function generateLandingPage(categories) {
  const totalApis = categories.reduce((sum, c) => sum + c.apis.length, 0);
  const noAuthApis = categories.reduce((sum, c) => sum + c.apis.filter(a => a.auth === 'none').length, 0);
  const httpsApis = categories.reduce((sum, c) => sum + c.apis.filter(a => a.https).length, 0);

  let mdx = `---
title: Awesome Free APIs
description: A curated collection of ${totalApis}+ free APIs across ${categories.length} categories for developers.
template: splash
hero:
  tagline: "A curated collection of ${totalApis}+ free APIs across ${categories.length} categories. Open source & community-driven."
  image:
    html: '<div style="font-size:6rem;line-height:1">🚀</div>'
  actions:
    - text: Browse APIs
      link: /awesome-free-apis/apis/animals/
      icon: right-arrow
      variant: primary
    - text: API Guide
      link: /awesome-free-apis/guide/getting-started/
      icon: open-book
      variant: minimal
    - text: GitHub
      link: https://github.com/ThanhNguyxn/awesome-free-apis
      icon: github
      variant: minimal
---

<div class="stats-grid">
  <div class="stat-card">
    <span class="stat-number">${totalApis}+</span>
    <span class="stat-label">Free APIs</span>
  </div>
  <div class="stat-card">
    <span class="stat-number">${categories.length}</span>
    <span class="stat-label">Categories</span>
  </div>
  <div class="stat-card">
    <span class="stat-number">${noAuthApis}</span>
    <span class="stat-label">No Auth Needed</span>
  </div>
  <div class="stat-card">
    <span class="stat-number">${Math.round((httpsApis / totalApis) * 100)}%</span>
    <span class="stat-label">HTTPS</span>
  </div>
</div>

## Browse by Category

<div class="category-grid">
`;

  for (const cat of categories) {
    const emoji = getEmojiFromTitle(cat.title);
    const cleanTitle = getCleanTitle(cat.title);
    const slug = slugify(cat.id);
    mdx += `  <a href="/awesome-free-apis/apis/${slug}/" class="category-card">
    <span class="cat-emoji">${emoji}</span>
    <span>${cleanTitle}</span>
    <span class="cat-count">${cat.apis.length}</span>
  </a>\n`;
  }

  mdx += `</div>

---

<p style="text-align: center; opacity: 0.6; font-size: 0.85rem;">
  Built with ❤️ by <a href="https://github.com/ThanhNguyxn">ThanhNguyxn</a> · 
  Auto-generated from <a href="https://github.com/ThanhNguyxn/awesome-free-apis/blob/main/README.md">README.md</a>
</p>
`;

  return mdx;
}

function generateGuidePage(readmeContent) {
  const guideStart = readmeContent.indexOf('## <a id="general-api-usage-guide">');
  const guideEnd = readmeContent.indexOf('## 📖 Table of Contents');

  if (guideStart === -1 || guideEnd === -1) {
    console.warn('Could not find guide section in README');
    return null;
  }

  let guide = readmeContent.substring(guideStart, guideEnd).trim();
  guide = guide.replace(/^## <a id="general-api-usage-guide"><\/a>\s*📘\s*General API Usage Guide\s*\n*/m, '');
  guide = guide.replace(/\r\n/g, '\n');

  let mdx = `---
title: "📘 API Usage Guide"
description: "Learn the basics of working with APIs - authentication, HTTP methods, status codes, and essential tools."
---

`;
  mdx += guide;
  return mdx;
}

function generateExamplesPage() {
  return `---
title: "📚 Code Examples"
description: "Practical code examples showing how to use popular APIs from the collection."
---

Check out practical code examples in the [examples/ folder on GitHub](https://github.com/ThanhNguyxn/awesome-free-apis/tree/main/examples).

## Available Examples

| Example | Language | API Used |
| :--- | :--- | :--- |
| **Pokemon API** | Python, JavaScript | [PokéAPI](https://pokeapi.co/) |
| **Cryptocurrency** | Python, JavaScript | [CoinGecko](https://www.coingecko.com/en/api) |
| **AI Chat** | Python, JavaScript | [OpenAI](https://platform.openai.com/) |

Each example includes both **Python** and **JavaScript** implementations with comments explaining the code.

### Quick Start

\`\`\`bash
# Clone the repo
git clone https://github.com/ThanhNguyxn/awesome-free-apis.git
cd awesome-free-apis/examples

# Run a Python example
python pokemon/pokemon_example.py

# Run a JavaScript example
node pokemon/pokemon_example.js
\`\`\`

---

> Want to contribute an example? Check out the [Contributing Guide](https://github.com/ThanhNguyxn/awesome-free-apis/blob/main/CONTRIBUTING.md).
`;
}

function cleanOutputDir(dir) {
  if (!existsSync(dir)) {
    mkdirSync(dir, { recursive: true });
    return;
  }
  const files = readdirSync(dir);
  for (const file of files) {
    if (file.endsWith('.mdx')) {
      unlinkSync(join(dir, file));
    }
  }
}

function main() {
  console.log('📖 Reading README.md...');
  const readmeContent = readFileSync(README_PATH, 'utf-8').replace(/\r\n/g, '\n');

  console.log('🔍 Parsing categories...');
  const categories = parseReadme();
  console.log(`   Found ${categories.length} categories`);

  const totalApis = categories.reduce((sum, c) => sum + c.apis.length, 0);
  console.log(`   Found ${totalApis} total APIs`);

  cleanOutputDir(DOCS_OUTPUT);

  console.log('📝 Generating category MDX files...');
  for (const cat of categories) {
    const orderIndex = CATEGORY_ORDER.indexOf(cat.id);
    const order = orderIndex >= 0 ? orderIndex + 1 : 99;
    const slug = slugify(cat.id);
    const mdx = generateCategoryMdx(cat, order);
    const outPath = join(DOCS_OUTPUT, `${slug}.mdx`);
    writeFileSync(outPath, mdx);
    console.log(`   ✅ ${slug}.mdx (${cat.apis.length} APIs)`);
  }

  console.log('🏠 Generating landing page...');
  const landingPage = generateLandingPage(categories);
  writeFileSync(INDEX_OUTPUT, landingPage);
  console.log('   ✅ index.mdx');

  console.log('📘 Generating guide page...');
  const guideMdx = generateGuidePage(readmeContent);
  if (guideMdx) {
    mkdirSync(dirname(GUIDE_OUTPUT), { recursive: true });
    writeFileSync(GUIDE_OUTPUT, guideMdx);
    console.log('   ✅ guide/getting-started.mdx');
  }

  console.log('📚 Generating examples page...');
  mkdirSync(dirname(EXAMPLES_OUTPUT), { recursive: true });
  writeFileSync(EXAMPLES_OUTPUT, generateExamplesPage());
  console.log('   ✅ examples/index.mdx');

  console.log(`\n🎉 Done! Generated ${categories.length} category pages + 3 static pages.`);
  console.log(`   Total APIs: ${totalApis}`);
}

main();
