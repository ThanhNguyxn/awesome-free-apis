# Copilot Instructions for awesome-free-apis

## Project Overview
This is a curated collection of free APIs for developers. The main content is in `README.md` organized by categories.

## API Entry Format
Each API entry in README.md must follow this exact format:
```markdown
| **API Name** | Short description. | Auth Type | HTTPS | [Link](url) |
```

### Auth Types:
- `No` - No authentication required
- `🔑 ApiKey` - API key required
- `🔐 OAuth` - OAuth authentication

### HTTPS:
- `✅` - HTTPS supported
- `No` - HTTP only

## Review Guidelines

### When reviewing new API additions:
1. ✅ Verify the API link is accessible (not 404/dead)
2. ✅ Check the format matches existing entries
3. ✅ Ensure the API is placed in the correct category
4. ✅ Description should be concise (under 60 characters)
5. ✅ Prefer APIs with **No Auth** or **ApiKey** over OAuth
6. ✅ Mark `(**No Auth**)` in description if no authentication needed

### When reviewing code changes:
1. Check `scripts/check_links.py` for link validation logic
2. Ensure workflow files in `.github/workflows/` are valid YAML
3. Validate that broken link detection works correctly

## Quality Standards
- APIs should be **free** (at least free tier available)
- APIs should be **actively maintained**
- Documentation link must be provided
- Duplicate APIs should be avoided
