import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
from urllib.parse import urljoin
from flask_caching import Cache

app = Flask(__name__)

BASE_URL = "https://paperswithcode.com/"

cache = Cache(app, config={"CACHE_TYPE": "simple"})


@app.route("/")
def index():
    url = request.args.get("url")

    cached_response = cache.get(url)

    if cached_response:
        return cached_response

    if not url:
        return jsonify({"error": "Invalid URL"}), 400

    try:
        response = requests.get(urljoin(BASE_URL, url), timeout=5)
    except:
        return jsonify({"error": "Invalid URL"}), 400

    if response.status_code != 200:
        return jsonify({"error": "Invalid URL"}), 400

    data = response.text
    soup = BeautifulSoup(data, "html.parser")

    papers = []

    for a in soup.find_all("a", href=True):
        if "/paper/" in a["href"]:
            papers.append({"title": a.text, "url": a["href"]})

    feed = {
        "version": "https://jsonfeed.org/version/1",
        "title": f"Papers with Code ({url})",
        "home_page_url": urljoin(BASE_URL, url),
        "feed_url": "https://example.org/feed.json",
        "items": [
            {
                "id": "https://paperswithcode.com" + p["url"],
                "title": p["title"].strip(),
                "content_text": p["title"].strip(),
                "url": "https://paperswithcode.com" + p["url"],
            }
            for p in papers
            if len(p["title"].strip()) > 10
        ],
    }

    cache.set(url, jsonify(feed), timeout=300)

    return jsonify(feed)


if __name__ == "__main__":
    app.run(debug=True)
