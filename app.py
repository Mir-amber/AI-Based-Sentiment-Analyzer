# app.py

from flask import Flask, render_template, request
from sentiment_model import analyze_sentiment

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    score = None

    if request.method == "POST":
        user_review = request.form["review"]
        sentiment, score = analyze_sentiment(user_review)

    return render_template("index.html", sentiment=sentiment, score=score)

if __name__ == "__main__":
    app.run(debug=True)
