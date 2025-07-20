import logging
import os
from scraper import config
from scraper import core
from scraper import utils
import argparse

def parse_arguments():
    """
    Parsea gli argomenti da linea di comando:
    --pages: numero di pagine da scrapare
    --output: file CSV per le citazioni
    --authors: file CSV per i dettagli degli autori
    """
    parser = argparse.ArgumentParser(description="Scraper di citazioni")
    parser.add_argument('--pages', type=int, default=10,
                    help='Numero di pagine da scrapare')
    parser.add_argument('--output', type=str,
                    default='data/quotes.csv', help='Percorso file CSV')
    parser.add_argument('--authors', type=str,
                    default='data/authors.csv', help='Percorso file CSV per gli autori')
    
    args = parser.parse_args()
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    authors_dir = os.path.dirname(args.authors)
    if authors_dir and not os.path.exists(authors_dir):
        os.makedirs(authors_dir)
    #logging.info(f"Scraperà {args.pages} pagine e salverà in {args.output}")    
    return args

def setup_environment(args):
    """
    Configura l'ambiente di esecuzione:
    - Crea le cartelle necessarie
    - Configura il logging
    """
    if not os.path.exists(config.LOG_FOLDER):
        os.makedirs(config.LOG_FOLDER)
    if not os.path.exists(config.DOWNLOAD_FOLDER):
        os.makedirs(config.DOWNLOAD_FOLDER)

    log_path = os.path.join(config.LOG_FOLDER, config.LOG_FILENAME)
    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)
    logging.info("Starting the scraping process...")

def save_output_to_file(quotes,args):
    """    Salva le citazioni in un file CSV.
    :param quotes: Lista di citazioni da salvare
    """
    utils.save_quotes_to_file(quotes, filename=args.output)
    utils.save_authors_to_file(quotes, filename=args.authors)

def run_scraping(pages):
    """
    Esegue il processo di scraping delle citazioni.
    :param pages: Numero di pagine da scrapare
    """
    quotes = core.scrape_quotes(pages=pages)
    return quotes

def main():
    """
    Funzione principale per eseguire lo scraper.
    """
    args = parse_arguments()
    setup_environment(args)
    quotes = run_scraping(args.pages)

    save_output_to_file(quotes, args)



        

    logging.info(f"Scraping completed. {len(quotes)} quotes found.")

if __name__ == "__main__":
    main()