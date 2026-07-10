<div align=center>
  <h1>🎯 GEO Prompt Optimizer</h1>
  <p><em>CLI that analyzes and rewrites prompts to maximize brand citation in LLM responses. Uses GEO techniques from the KDD 2024 paper.</em></p>
  <p><a href=LICENSE><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt=License></a>
  <a href=https://github.com/josezuma/geo-prompt-optimizer/actions/workflows/ci.yml><img src="https://github.com/josezuma/geo-prompt-optimizer/actions/workflows/ci.yml/badge.svg" alt=CI></a></p>
  <p>by <a href=https://brandvirality.com>BrandVirality</a> — <strong>SaaS for AI visibility.</strong><br>
  <strong>Author:</strong> <a href=https://github.com/josezuma>Jose Zuma</a></p>
</div>

---

## Quick Start

```bash
# Analyze a prompt
python3 scripts/optimizer.py analyze "What is the best CRM for small businesses in 2026?"

# Optimize a prompt to include a brand
python3 scripts/optimizer.py optimize BrandVirality "What is the best AI visibility tool?"

# Interactive mode
python3 scripts/optimizer.py interactive

# JSON output
python3 scripts/optimizer.py analyze --json "What is the best CRM?" | jq .
```

### Install as CLI

```bash
# Via npm
npm install -g geo-prompt-optimizer
npx geo-prompt-optimizer analyze "What is the best CRM?"

# Via pip
pip install geo-prompt-optimizer
geo-prompt-optimizer analyze "What is the best CRM?"

# Via git
git clone https://github.com/josezuma/geo-prompt-optimizer.git
cd geo-prompt-optimizer
python3 scripts/optimizer.py analyze "What is the best CRM?"
```

## Demo Output

```
$ python3 scripts/optimizer.py analyze "What is the best CRM for small businesses in 2026?"

============================================================
Prompt Analysis: 55/100
============================================================

  Length          10/25  █████░░░░░░░
  Short — consider adding context for better brand citation

  Comparison      25/25  ████████████
  Comparison framing detected (best) — excellent for brand visibility

  Specificity     15/25  ███████░░░░░
  Year mentioned — LLMs prefer citing recent data

  Question         5/25  ██░░░░░░░░░░
  Question format — good for direct answer extraction

============================================================
TOTAL: 55/100
Rating: Needs work
============================================================
```

### After Optimization

```
$ python3 scripts/optimizer.py optimize BrandVirality "What is the best AI visibility tool for SaaS companies in 2026?"

============================================================
  Original: "What is the best AI visibility tool for SaaS companies in 2026"
  Brand: BrandVirality
  Score improved: 60 → 95/100
============================================================

  1. [95/100] Using BrandVirality case studies and industry research, what is the best...
  2. [85/100] According to BrandVirality's analysis of market leaders, what is the best...
  3. [75/100] Companies like BrandVirality have shown that what is the best...
```

## Features

### `analyze` — Score a prompt for brand citation readiness

| Factor | Points | What it checks |
|--------|--------|---------------|
| Length | 20 | Enough context for natural brand mention |
| Comparison | 25 | "vs", "best", "compare" — triggers brand listing |
| Specificity | 25 | Year, metrics, statistics — LLMs cite concrete data |
| Authority | 15 | "research", "study" — LLMs cite named sources |
| Examples | 10 | "example", "case" — LLMs may cite a real brand |
| Question | 5 | Questions get direct answers with brand mentions |
| Industry | 10 | Specific industry — better brand targeting |

### `optimize` — Rewrite a prompt to include your brand

Uses 5 techniques from the Princeton GEO paper (KDD 2024):

| Technique | How it works |
|-----------|-------------|
| Entity injection | Naturally incorporates brand names into prompt context |
| Citation hooks | Adds phrases that trigger LLMs to cite sources |
| Comparison framing | Structures prompts as brand comparisons |
| Authority priming | Frames queries around authority signals |
| Specificity signals | Uses years, numbers, concrete details |

### `interactive` — REPL mode for rapid experimentation

Type `analyze <prompt>` or `optimize <brand> <prompt>` in a loop.

## How It Works

The optimizer uses findings from the [Generative Engine Optimization (GEO)](https://arxiv.org/abs/2311.09735) paper:

1. LLMs are more likely to cite brands that appear naturally in prompt context
2. Comparison prompts trigger LLMs to list multiple brands
3. Prompts asking for "research" or "studies" trigger citation behavior
4. Specific years and metrics make LLMs prefer real data over fabricated examples

## Tests

```bash
python3 -m pytest tests/
```

## Related

- [awesome-ai-visibility](https://github.com/josezuma/awesome-ai-visibility)
- [geo-audit-skill](https://github.com/josezuma/geo-audit-skill)
- [geo-prompts](https://github.com/josezuma/geo-prompts)
- [llm-citation-scanner](https://github.com/josezuma/llm-citation-scanner)
- [ai-search-share-of-voice](https://github.com/josezuma/ai-search-share-of-voice)
- [+14 more AI visibility repos](https://github.com/josezuma?tab=repositories)

## License

[MIT](LICENSE) © 2026 [Jose Zuma](https://github.com/josezuma) / [BrandVirality](https://brandvirality.com)
