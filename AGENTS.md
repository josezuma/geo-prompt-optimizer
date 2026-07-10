# geo-prompt-optimizer — Prompt analysis & brand citation optimization

## Install
```bash
python3 scripts/optimizer.py analyze "Your prompt here"
pip install requests  # for JSON mode
```

## For AI agents
- `scripts/optimizer.py` is the main entrypoint
- Subcommands: analyze, optimize, interactive, techniques
- Output: scored report with prioritized improvements
- Sister repo: geo-prompts (benchmark prompt sets)
- Sister repo: ai-search-share-of-voice (query LLMs)
- Sister repo: llm-citation-scanner (scan responses)
