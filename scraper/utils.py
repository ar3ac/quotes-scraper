from scraper import config
import csv
import logging
import os
import requests
from bs4 import BeautifulSoup

CSV_PATH = os.path.join(config.DOWNLOAD_FOLDER, config.CSV_FILENAME)
def save_quotes_to_file(quotes, filename=CSV_PATH):
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


def scrape_author_details(author_url):
    try:
        response = requests.get(author_url)
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Error fetching {author_url}: {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    born_date = soup.find('span', class_='author-born-date')
    born_location = soup.find('span', class_='author-born-location')

    details = {}

    if born_date:
        details['born_date'] = born_date.get_text(strip=True)
    else:
        details['born_date'] = ''

    if born_location:
        details['born_location'] = born_location.get_text(strip=True)
    else:
        details['born_location'] = ''

    return details


def save_authors_to_file(authors_dict, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'link', 'born_date', 'born_location']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for author_data in authors_dict.values():
            writer.writerow(author_data)
    logging.info(f"{len(authors_dict)} authors saved to {filename}")
