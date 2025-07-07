# sentiment_model.py

from transformers import pipeline

# Load sentiment pipeline once
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    label = result["label"]
    score = result["score"]

    # Optional: Treat low confidence as NEUTRAL
    if 0.45 < score < 0.55:
        sentiment = "NEUTRAL"
    else:
        sentiment = label.upper()

    return sentiment, round(score, 2)
