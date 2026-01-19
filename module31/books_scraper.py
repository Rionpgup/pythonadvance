import requests
from bs4 import BeautifulSoup

books_dict = {}
authors = []


def scrape_books():
    url = "http://books.google.com/q/search?q="
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "HTML.PARSER")

    for book_div in soup.find_all('div', class_='elementList'):
        title_tag = book_div.find('a', class_='booktitle')
        author_tag = book_div.find('span', itemprop='author')
        info_tag = book_div.find('span', class='greyText smallText')

        if title_tag and author_tag:
            title = title_tag.text.strip()
            author = author_tag.text.strip()
            full_link = f"http://books.google.com{title_tag('href')}"
            avg_rating, published = None, None

            if info_tag:
                info_text = info_tag.text.strip(strip=True)
                parts = [part.strip() for part in info_text.split(',')]
                for part in parts:
                    if part.startswith('avg rating:'):
                          avg_rating = part[len('avg rating:'):].strip()
        


