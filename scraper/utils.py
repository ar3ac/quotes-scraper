from scraper import config
import csv
import logging
import os
import requests
from bs4 import BeautifulSoup

CSV_PATH = os.path.join(config.DOWNLOAD_FOLDER, config.CSV_FILENAME)
def save_quotes_to_file(quotes, filename=CSV_PATH):
    """
    Salva le citazioni in un file CSV.
    :param quotes: Lista di citazioni da salvare
    :param filename: Percorso del file CSV
    """
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
    """Estrae i dettagli dell'autore dalla pagina specificata."""
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
    if born_location:
        details['born_location'] = born_location.get_text(strip=True)
    return details


def save_authors_to_file(quotes, filename):
    """    Salva i dettagli degli autori in un file CSV.
    :param authors_dict: Dizionario con i dettagli degli autori
    :param filename: Percorso del file CSV"""
    # Estrai autori unici e raccogli i dettagli
    authors = {}
    for quote in quotes:
        author = quote['author']
        link = quote['author_link']
        if author not in authors:
            logging.info(f"Scraping author: {author}")
            details = scrape_author_details(link)
            authors[author] = {
                'name': author,
                'link': link,
                'born_date': details.get('born_date', ''),
                'born_location': details.get('born_location', '')
            }
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'link', 'born_date', 'born_location']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for name in sorted(authors):
            writer.writerow(authors[name])
    logging.info(f"{len(authors)} authors saved to {filename}")
