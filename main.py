import logging
import os
from scraper import config
from scraper import core
from scraper import utils
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Scraper di citazioni")
    parser.add_argument('--pages', type=int, default=10,
                    help='Numero di pagine da scrapare')
    parser.add_argument('--output', type=str,
                    default='data/quotes.csv', help='Percorso file CSV')

    args = parser.parse_args()
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    #logging.info(f"Scraperà {args.pages} pagine e salverà in {args.output}")    
    return args


def main():
    args = parse_arguments()
    #print(args)
    # Create necessary directories if they do not exist
    if not os.path.exists(config.LOG_FOLDER):
        os.makedirs(config.LOG_FOLDER)
    if not os.path.exists(config.DOWNLOAD_FOLDER):
        os.makedirs(config.DOWNLOAD_FOLDER)

    # Configurazione del logging
    log_path = os.path.join(config.LOG_FOLDER, config.LOG_FILENAME)
    logging.basicConfig(
        filename=log_path,      # File dove scrivere i log
        level=logging.INFO,          # Livello minimo che vuoi loggare
        format='%(asctime)s - %(levelname)s - %(message)s'
    ) 
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)
    logging.info("Starting the scraping process...")

    quotes = core.scrape_quotes(pages=args.pages)
    utils.save_quotes_to_file(quotes, filename=args.output)

    logging.info(f"Scraping completed. {len(quotes)} quotes found.")

if __name__ == "__main__":
    main()