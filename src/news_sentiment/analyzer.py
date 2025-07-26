from transformers import pipeline

# initialize once
_sentiment = pipeline("sentiment-analysis")

def analyze(texts: list[str]) -> list[dict]:
    """
    Returns a list of {label: str, score: float}.
    """
    return _sentiment(texts)
