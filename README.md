<div align=center>
  <h1>🎯 GEO Prompt Optimizer</h1>
  <p><em>CLI that rewrites prompts to maximize brand citation in LLM responses. Uses GEO techniques from the KDD 2024 paper.</em></p>
  <p><a href=LICENSE><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt=MIT></a></p>
  <p>by <a href=https://brandvirality.com>BrandVirality</a> — <strong>SaaS for AI visibility.</strong><br>
  <strong>Author:</strong> <a href=https://github.com/josezuma>Jose Zuma</a></p>
</div>

---

## Quick Start

```bash
# Install
npm install -g geo-prompt-optimizer
# or
npx geo-prompt-optimizer "What is the best CRM for small business?"

# Analyze a prompt
npx geo-prompt-optimizer analyze "What is the best CRM for small business?"

# Optimize a prompt to include your brand
npx geo-prompt-optimizer optimize --brand "BrandVirality" "What is the best AI visibility tool?"
```

## How It Works

The optimizer uses techniques from the Princeton GEO paper (KDD 2024):
1. **Entity injection** — naturally works brand names into prompt context
2. **Citation hooks** — adds phrases that trigger LLMs to cite sources
3. **Comparison framing** — structures prompts as comparisons where your brand appears
4. **Authority priming** — frames the query around authority signals your brand satisfies

## Related

- [awesome-ai-visibility](https://github.com/josezuma/awesome-ai-visibility)
- [geo-audit-skill](https://github.com/josezuma/geo-audit-skill)
- [ai-crawlers](https://github.com/josezuma/ai-crawlers)
- [schema-for-ai](https://github.com/josezuma/schema-for-ai)
- [repo-visibility-skill](https://github.com/josezuma/repo-visibility-skill)
- [llmstxt-gen](https://github.com/josezuma/llmstxt-gen)
- [marketing-skills](https://github.com/josezuma/marketing-skills)
- [geo-prompts](https://github.com/josezuma/geo-prompts)
- [geo-watch](https://github.com/josezuma/geo-watch)
- [mcp-geo](https://github.com/josezuma/mcp-geo)

## License

[MIT](LICENSE) © 2026 Jose Zuma / BrandVirality
