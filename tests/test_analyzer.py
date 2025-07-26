from news_sentiment.analyzer import analyze

def test_analyze_simple():
    res = analyze(["I love this!", "I hate that!"])
    labels = {r["label"] for r in res}
    assert "POSITIVE" in labels and "NEGATIVE" in labels
