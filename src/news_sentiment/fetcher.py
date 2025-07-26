import requests
from .config import settings

def fetch_headlines(query: str, limit: int = 10) -> list[str]:
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "apiKey": settings.newsapi_key,
        "pageSize": limit,
        "language": "en",
        "sortBy": "publishedAt",
    }
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()
    return [art.get("content") or art.get("description", "") for art in data.get("articles", [])]
