from scraper import config
import csv
import logging
import os

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
