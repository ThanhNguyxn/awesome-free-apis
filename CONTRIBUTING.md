# Contributing to Awesome Free APIs

Thanks for helping improve this project.

This repository is a curated list of **free/freemium APIs**. We prioritize quality, reliability, and clean formatting.

## What You Can Contribute

- Add new APIs
- Fix broken links
- Improve descriptions and formatting
- Improve tooling/workflows/docs

## Requirements for New API Entries

An API should meet all of the following:

- Be publicly documented
- Be free or provide a meaningful free tier
- Be active and reachable
- Fit an existing category (or justify a new category)

## Entry Format

Follow this exact table format in `README.md`:

```md
| **API Name** | Short description. | No/🔑 ApiKey/🔐 OAuth | ✅/No | [Link](https://example.com/docs) |
```

Guidelines:

- Keep descriptions concise and practical
- Use `No`, `🔑 ApiKey`, or `🔐 OAuth` for auth
- Use `✅` or `No` for HTTPS
- Keep entries alphabetized within each category where possible
- Avoid duplicate APIs and duplicate links

## Local Validation Before Opening a PR

Run link checks:

```bash
python scripts/check_links.py
```

If your changes affect docs structure/content generation, also run:

```bash
node scripts/generate-docs.mjs
```

Optional docs build check:

```bash
cd docs-site
npm ci
npm run build
```

## Suggested Contribution Workflow

```bash
git fork https://github.com/ThanhNguyxn/awesome-free-apis
git clone https://github.com/YOUR-USERNAME/awesome-free-apis.git
cd awesome-free-apis
git checkout -b feat/add-api-name
```

Make your changes, run validation, then open a PR using the PR template.

## Pull Request Checklist

- API(s) are not duplicates
- Link(s) are reachable
- Entry format matches the README table
- Category placement is correct
- Local checks were run (or reason provided)

## Community Standards

By participating, you agree to follow our [Code of Conduct](./CODE_OF_CONDUCT.md).
