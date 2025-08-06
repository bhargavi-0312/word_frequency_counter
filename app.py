from flask import Flask, render_template, request
from collections import Counter
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    word_freq = {}
    total_words = 0

    if request.method == "POST":
        text = request.form["text"].lower()
        words = re.findall(r'\b\w+\b', text)
        word_freq = dict(Counter(words))
        total_words = sum(word_freq.values())

    return render_template("index.html", word_freq=word_freq, total_words=total_words)

if __name__ == "__main__":
    app.run(debug=True)
