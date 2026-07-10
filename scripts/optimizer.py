#!/usr/bin/env python3
"""geo-prompt-optimizer — Analyze and optimize prompts for brand citation in LLM responses."""

import sys, json, re, os, argparse
from typing import List, Dict

BRAND_CITATION_TECHNIQUES = {
    "entity_injection": "Naturally incorporates brand names into prompt context without keyword stuffing",
    "citation_hooks": "Adds phrases that trigger LLMs to cite sources (e.g. 'according to industry research')",
    "comparison_framing": "Structures prompts as comparisons where target brand naturally appears",
    "authority_priming": "Frames the query around authority signals the target brand satisfies",
    "specificity_signals": "Uses years, numbers, and concrete details that LLMs associate with real brands",
}

class PromptAnalyzer:
    def __init__(self):
        self.checks = []
        self.score = 0

    def analyze(self, prompt: str) -> dict:
        self.checks = []
        self.score = 0
        words = len(prompt.split())

        # Length analysis
        if words < 5:
            self._add("Length", 0, "Too short — LLMs need context to cite brands naturally")
        elif words < 15:
            self._add("Length", 10, "Short — consider adding context for better brand citation")
        elif words < 50:
            self._add("Length", 20, "Good length for brand citation")
        else:
            self._add("Length", 20, "Excellent length — plenty of room for brand mentions")

        # Comparison framing
        comparison_words = ["compare", "vs", "versus", "alternative", "alternatives", "best", "top", "leading", "better", "difference"]
        found_comp = [w for w in comparison_words if w in prompt.lower().split()]
        if found_comp:
            self._add("Comparison", 25, f"Comparison framing detected ({', '.join(found_comp)}) — excellent for brand visibility")
        else:
            self._add("Comparison", 5, "No comparison framing — brands harder to insert naturally")

        # Specificity
        if re.search(r'\b(202[4-9]|203[0-9])\b', prompt):
            self._add("Specificity", 15, "Year mentioned — LLMs prefer citing recent data")
        if re.search(r'\b\d+%|\b\d+x\b', prompt):
            self._add("Specificity", 10, "Metric/percentage found — LLMs cite quantified claims")
        if re.search(r'(statistics|research|study|report|survey|analysis)', prompt.lower()):
            self._add("Authority", 15, "Authority requested — LLMs cite named sources")
        if re.search(r'(example|instance|case|scenario)', prompt.lower()):
            self._add("Examples", 10, "Examples requested — LLMs may cite a real brand")

        # Question type
        if prompt.strip().endswith("?"):
            self._add("Question", 5, "Question format — good for direct answer extraction")

        # Industry specificity
        industries = ["saas", "healthcare", "fintech", "ecommerce", "b2b", "enterprise",
                       "startup", "agency", "retail", "manufacturing"]
        found_ind = [i for i in industries if i in prompt.lower()]
        if found_ind:
            self._add("Industry", 10, f"Specific industry mentioned ({', '.join(found_ind)}) — better brand targeting")
        
        self.score = min(self.score, 100)
        return {"score": self.score, "checks": self.checks}

    def _add(self, category: str, score: int, detail: str):
        self.checks.append({"category": category, "score": score, "detail": detail})
        self.score += score

    def print_report(self, result: dict):
        print(f"\n{'='*60}")
        print(f"Prompt Analysis: {result['score']}/100")
        print(f"{'='*60}")
        for check in result["checks"]:
            bar = "█" * (check["score"] // 2) + "░" * ((25 - check["score"]) // 2)
            print(f"\n  {check['category']:15s} {check['score']:2d}/25  {bar}")
            print(f"  {check['detail']}")
        print(f"\n{'='*60}")
        print(f"TOTAL: {result['score']}/100")
        rating = "Excellent" if result["score"] >= 80 else "Good" if result["score"] >= 60 else "Needs work" if result["score"] >= 40 else "Poor"
        print(f"Rating: {rating}")
        print(f"{'='*60}\n")


class PromptOptimizer:
    def __init__(self):
        self.techniques = BRAND_CITATION_TECHNIQUES

    def optimize(self, prompt: str, brand: str) -> dict:
        prompt = prompt.strip().rstrip('.?!')
        
        # Analyze original first
        analyzer = PromptAnalyzer()
        analysis = analyzer.analyze(prompt)

        optimizations = [
            f"From a {brand} perspective, {prompt[0].lower() + prompt[1:] if prompt else prompt}",
            f"With companies like {brand} as a benchmark, {prompt[0].lower() + prompt[1:] if prompt else prompt}",
            f"Using {brand} case studies and industry research, {prompt[0].lower() + prompt[1:] if prompt else prompt}",
            f"According to {brand}'s analysis of market leaders, {prompt[0].lower() + prompt[1:] if prompt else prompt}",
            f"Companies like {brand} have shown that {prompt[0].lower() + prompt[1:] if prompt else prompt}. What specific strategies do they use?",
        ]

        # Score each optimization
        scored_opts = []
        for opt in optimizations:
            opt_analysis = analyzer.analyze(opt)
            scored_opts.append({"text": opt, "score": opt_analysis["score"]})

        scored_opts.sort(key=lambda x: x["score"], reverse=True)

        return {
            "original": prompt,
            "brand": brand,
            "original_score": analysis["score"],
            "optimizations": scored_opts,
            "best_score": scored_opts[0]["score"] if scored_opts else 0,
            "techniques_used": list(self.techniques.keys()),
        }


def interactive():
    """Interactive mode — analyze and optimize in a loop."""
    analyzer = PromptAnalyzer()
    optimizer = PromptOptimizer()
    
    print(f"\n{'='*60}")
    print("  GEO Prompt Optimizer — Interactive Mode")
    print(f"{'='*60}")
    print("  Commands: analyze <prompt> | optimize <brand> <prompt> | techniques | quit")
    
    while True:
        try:
            line = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        
        if not line:
            continue
        if line == "quit" or line == "q":
            break
        if line == "techniques":
            print(f"\n{'='*60}")
            print("  Brand Citation Techniques")
            print(f"{'='*60}")
            for t, d in BRAND_CITATION_TECHNIQUES.items():
                print(f"  • {t.replace('_', ' ').title()}: {d}")
            continue
        
        parts = line.split(maxsplit=1)
        if not parts:
            continue
        
        cmd = parts[0].lower()
        rest = parts[1] if len(parts) > 1 else ""
        
        if cmd == "analyze" and rest:
            result = analyzer.analyze(rest)
            analyzer.print_report(result)
        elif cmd == "optimize" and rest:
            # Format: optimize <brand> <prompt>
            opt_parts = rest.split(maxsplit=1)
            if len(opt_parts) < 2:
                print("Usage: optimize <brand> <prompt>")
                continue
            brand = opt_parts[0]
            prompt = opt_parts[1]
            result = optimizer.optimize(prompt, brand)
            print(f"\n{'='*60}")
            print(f"  Optimized Prompts for: {result['brand']}")
            print(f"{'='*60}")
            print(f"\n  Original: \"{result['original']}\"")
            print(f"  Original Score: {result['original_score']}/100")
            print(f"  Best Optimized Score: {result['best_score']}/100")
            print(f"\n  Top 3 Optimizations:\n")
            for i, opt in enumerate(result["optimizations"][:3], 1):
                print(f"  {i}. [{opt['score']}/100] {opt['text']}")
        else:
            print("Commands: analyze <prompt> | optimize <brand> <prompt> | techniques | quit")


def main():
    parser = argparse.ArgumentParser(
        description="GEO Prompt Optimizer — analyze and rewrite prompts for brand citation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  geo-prompt-optimizer analyze "What is the best CRM for small business?"
  geo-prompt-optimizer analyze --json "What is the best CRM for small business?"
  geo-prompt-optimizer optimize BrandVirality "What is the best AI visibility tool?"
  geo-prompt-optimizer interactive
  geo-prompt-optimizer techniques
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # analyze
    analyze_parser = subparsers.add_parser("analyze", help="Analyze a prompt for brand citation readiness")
    analyze_parser.add_argument("prompt", nargs="+", help="The prompt to analyze")
    analyze_parser.add_argument("--json", action="store_true", help="Output as JSON")
    
    # optimize
    optimize_parser = subparsers.add_parser("optimize", help="Optimize a prompt to include a brand")
    optimize_parser.add_argument("brand", help="Brand name to include")
    optimize_parser.add_argument("prompt", nargs="+", help="The prompt to optimize")
    optimize_parser.add_argument("--json", action="store_true", help="Output as JSON")
    optimize_parser.add_argument("--count", type=int, default=5, help="Number of optimizations to generate")
    
    # interactive
    subparsers.add_parser("interactive", help="Interactive mode")
    
    # techniques
    techniques_parser = subparsers.add_parser("techniques", help="List available GEO techniques")
    techniques_parser.add_argument("--json", action="store_true", help="Output as JSON")
    
    args = parser.parse_args()
    
    analyzer = PromptAnalyzer()
    optimizer = PromptOptimizer()
    
    if not args.command or args.command == "interactive":
        interactive()
        return
    
    if args.command == "techniques":
        if getattr(args, 'json', False):
            print(json.dumps(BRAND_CITATION_TECHNIQUES, indent=2))
        else:
            print(f"\n{'='*60}")
            print("  Brand Citation Techniques (from KDD 2024 GEO paper)")
            print(f"{'='*60}")
            for t, d in BRAND_CITATION_TECHNIQUES.items():
                print(f"  • {t.replace('_', ' ').title()}: {d}")
            print()
        return
    
    if args.command == "analyze":
        prompt = " ".join(args.prompt)
        result = analyzer.analyze(prompt)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            analyzer.print_report(result)
        return
    
    if args.command == "optimize":
        prompt = " ".join(args.prompt)
        result = optimizer.optimize(prompt, args.brand)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"\n{'='*60}")
            print(f"  Original: \"{result['original']}\"")
            print(f"  Brand: {result['brand']}")
            print(f"  Score improved: {result['original_score']} → {result['best_score']}/100")
            print(f"{'='*60}\n")
            for i, opt in enumerate(result["optimizations"], 1):
                print(f"  {i}. [{opt['score']}/100] {opt['text']}")
            print()


if __name__ == "__main__":
    main()
