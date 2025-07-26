# news-driven-sentiment-strategies

A Python library that applies transformer‑based sentiment analysis on financial news, and constructs trading signals.

### Features

#### Sentiment Analysis

- Uses Hugging Face’s FinBERT models for finance‑tuned sentiment scoring
- Batched inference with caching by headline hash
- Returns continuous sentiment scores in [–1, +1]
  
#### Signal Construction
- Daily aggregation per ticker: average sentiment, volume, Z‑score
- Configurable thresholds for long/short signals
- Optional minimum news‑volume filter to reduce noise

### Installation
```sh
git clone https://github.com/rohitmungre/news‑driven‑sentiment‑strategies.git
cd news-driven-sentiment-strategies
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### License
This project is licensed under the MIT License. Feel free to reuse and adapt.
