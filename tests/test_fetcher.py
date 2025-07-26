import pytest
from news_sentiment.fetcher import fetch_headlines

def test_fetch_headlines(monkeypatch):
    class DummyResp:
        def raise_for_status(self): pass
        def json(self): return {"articles":[{"content":"Hello world"}]}
    monkeypatch.setattr("requests.get", lambda *args, **kw: DummyResp())
    out = fetch_headlines("test", limit=1)
    assert out == ["Hello world"]
