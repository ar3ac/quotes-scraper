import logging
import os
from scraper import config
from scraper import core
from scraper import utils

def main():
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
    quotes = core.scrape_quotes()
    utils.save_quotes_to_file(quotes)
    logging.info(f"Scraping completed. {len(quotes)} quotes found.")

if __name__ == "__main__":
    main()