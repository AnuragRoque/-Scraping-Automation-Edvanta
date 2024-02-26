# app.py

from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
@app.route('/')
def home():
    default_search_term = "Backend Development"
    articles = scrape_articles(default_search_term)
    
    return render_template('index.html', default_search=default_search_term, articles=articles)

@app.route('/search')
def search():
    search_term = request.args.get('keyword', '')
    articles = scrape_articles(search_term)
    return jsonify({'articles': articles})

def scrape_articles(search_term):
    # scraping articles from Google
    url = f"https://www.google.com/search?q={search_term}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = [result.text for result in soup.find_all('h3')]

    return articles
if __name__ == '__main__':
    app.run(debug=True)
