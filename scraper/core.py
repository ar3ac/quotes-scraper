import requests
from bs4 import BeautifulSoup
import logging
from scraper import config

def scrape_quotes(pages=config.PAGES_TO_SCRAPE):
    all_quotes = []
    for i in range(1, pages + 1):  # Scrape specified number of  pages
        page_url = f"{config.URL_BASE}page/{i}/"
        logging.info(f"Scraping page {i}: {page_url}")
        quotes = extract_quotes(page_url)
        logging.info(f"Found {len(quotes)} quotes on {page_url}")
        all_quotes.extend(quotes)
    return all_quotes


def extract_quotes(page_url):
    try:
        response = requests.get(page_url)
    except requests.RequestException as e:
        logging.error(f"Error fetching {page_url}: {e}")
        return []
    if response.status_code != 200:
        logging.error(f"Error fetching {page_url}: {response.status_code}")
        return []
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = []
    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
        # print(f"{text} by {author}   with tags {tags}")
        if text and author and tags:
            quotes.append({
                'text': text,
                'author': author,
                'tags': tags
            })
    if not quotes:
        logging.info(f"No quotes found on {page_url}")
    return quotes
