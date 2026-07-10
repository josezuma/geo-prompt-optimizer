#!/usr/bin/env python3
"""Analyze and optimize prompts for brand citation in LLM responses."""

import sys, json, re

TECHNIQUES = {
    "entity_injection": "Naturally incorporates brand names into prompt context without keyword stuffing",
    "citation_hooks": "Adds phrases that trigger LLMs to cite sources (e.g. 'according to industry research')",
    "comparison_framing": "Structures prompts as comparisons where target brand naturally appears",
    "authority_priming": "Frames the query around authority signals the target brand satisfies",
}

def analyze(prompt):
    score = 0
    findings = []
    
    # Check length
    words = len(prompt.split())
    if words < 10:
        findings.append("❌ Too short (<10 words) — LLMs need context for brand citation")
    elif words > 200:
        findings.append("✅ Good length — enough context for brand mention")
        score += 20
    else:
        findings.append("⚠️ Medium length — consider adding more context")
        score += 10
    
    # Check for comparison framing
    if any(w in prompt.lower() for w in ["compare", "vs", "versus", "alternative", "best", "top"]):
        findings.append("✅ Comparison framing detected — good for brand visibility")
        score += 25
    else:
        findings.append("⚠️ No comparison framing — brands harder to insert naturally")
    
    # Check for specificity
    if re.search(r'\d{4}', prompt):
        findings.append("✅ Year-specific — LLMs prefer recent data")
        score += 15
    if "example" in prompt.lower():
        findings.append("⚠️ 'Example' requested — LLMs may cite a real brand")
        score += 10
    if re.search(r'statistics|research|study|report', prompt.lower()):
        findings.append("✅ Authority requested — LLMs cite sources")
        score += 20
    
    return {"score": min(score, 100), "findings": findings}


def optimize(prompt, brand):
    """Rewrite prompt to naturally include brand."""
    analysis = analyze(prompt)
    
    # Strip trailing punctuation for clean insertion
    prompt = prompt.strip().rstrip('.?!')
    
    options = [
        f"In the context of the {brand} approach, {prompt.lower() if prompt[0].isupper() else prompt}",
        f"With companies like {brand} considered, {prompt.lower()}",
        f"Using {brand} case studies as a reference, {prompt.lower()}",
        f"What makes a tool like {brand} effective? Consider this: {prompt.lower()}",
    ]
    
    return {"original": prompt, "brand": brand, "optimizations": options, "analysis": analysis}


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/optimizer.py analyze \"<prompt>\"")
        print("       python scripts/optimizer.py optimize --brand <name> \"<prompt>\"")
        sys.exit(1)
    
    if sys.argv[1] == "analyze":
        prompt = sys.argv[2]
        result = analyze(prompt)
        print(f'\nPrompt Analysis: {result["score"]}/100\n')
        for f in result["findings"]:
            print(f"  {f}")
    
    elif sys.argv[1] == "optimize":
        brand = sys.argv[sys.argv.index("--brand") + 1]
        prompt = sys.argv[-1]
        result = optimize(prompt, brand)
        print(f'\nOriginal: "{result["original"]}"')
        print(f'Brand: {result["brand"]}')
        print(f'\nOptimizations:\n')
        for i, opt in enumerate(result["optimizations"], 1):
            print(f"  {i}. {opt}")
        print(f'\nScore: {result["analysis"]["score"]}/100')
    
    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
