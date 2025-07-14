import requests
from bs4 import BeautifulSoup
import csv
import logging
import os

url = "http://quotes.toscrape.com/"

logpath = 'log/scraper.log'
csvpath = 'data/quotes.csv'

if not os.path.exists('log'):
    os.makedirs('log')
if not os.path.exists('data'):
    os.makedirs('data')

# Configurazione del logging
logging.basicConfig(
    filename=logpath,      # File dove scrivere i log
    level=logging.INFO,          # Livello minimo che vuoi loggare
    format='%(asctime)s - %(levelname)s - %(message)s'
)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger().addHandler(console)

pages_to_scrape = 10  # Number of pages to scrape

def scrape_quotes(pages=pages_to_scrape):
    all_quotes = []
    for i in range(1, pages + 1):  # Scrape specified number of  pages
        page_url = f"{url}page/{i}/"
        logging.info(f"Scraping page {i}: {page_url}")
        quotes = extract_quotes(page_url)
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
        #print(f"{text} by {author}   with tags {tags}")
        if text and author and tags:
            quotes.append({
                'text': text,
                'author': author,
                'tags': tags
            })
    if not quotes:
        logging.info(f"No quotes found on {page_url}")
    return quotes


def save_quotes_to_file(quotes, filename=csvpath):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['quote', 'author', 'tags']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for quote in quotes:
            writer.writerow({
                'quote': quote['text'],
                'author': quote['author'],
                'tags': ', '.join(quote['tags'])
            })
    logging.info(f"{len(quotes)} Quotes saved to {filename}")


if __name__ == "__main__":
    logging.info("Starting the scraping process...")
    quotes = scrape_quotes()
    save_quotes_to_file(quotes)
    logging.info(f"Scraping completed. {len(quotes)} quotes found.")