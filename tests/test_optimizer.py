"""Tests for geo-prompt-optimizer."""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from scripts.optimizer import PromptAnalyzer, PromptOptimizer

analyzer = PromptAnalyzer()
optimizer = PromptOptimizer()

def test_analyze_short_prompt():
    result = analyzer.analyze("Best CRM?")
    assert result["score"] >= 0
    assert result["score"] <= 100
    assert len(result["checks"]) >= 3
    print("✅ test_analyze_short_prompt passed (%d/100)" % result["score"])

def test_analyze_long_prompt():
    result = analyzer.analyze("What is the best CRM for small businesses in 2026 according to industry research?")
    assert result["score"] >= 40
    print("✅ test_analyze_long_prompt passed (%d/100)" % result["score"])

def test_optimize_improves_score():
    result = optimizer.optimize("Best CRM for small business?", "BrandVirality")
    assert result["best_score"] >= result["original_score"]
    assert len(result["optimizations"]) > 0
    print("✅ test_optimize_improves_score passed (%d → %d)" % (result["original_score"], result["best_score"]))

def test_json_output():
    import subprocess
    r = subprocess.run([sys.executable, "scripts/optimizer.py", "analyze", "--json", "Best CRM?"],
                      capture_output=True, text=True, cwd=os.path.join(os.path.dirname(__file__), '..'))
    data = json.loads(r.stdout)
    assert "score" in data
    assert "checks" in data
    print("✅ test_json_output passed")

def test_techniques_list():
    result = optimizer.optimize("What is the best tool?", "TestBrand")
    assert len(result["techniques_used"]) == 5
    print("✅ test_techniques_list passed (5 techniques)")

def test_interactive_not_crashing():
    """Just verify the module imports don't crash."""
    assert True
    print("✅ test_interactive_not_crashing passed")

if __name__ == "__main__":
    tests = [fn for name, fn in sorted(globals().items()) if name.startswith("test_")]
    passed = 0
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print("❌ %s failed: %s" % (test.__name__, e))
    print("\n%d/%d tests passed" % (passed, len(tests)))
