# Quotes Scraper

Uno scraper realizzato in Python per estrarre citazioni e dettagli sugli autori dal sito [Quotes to Scrape](http://quotes.toscrape.com).

## Funzionalità

- Estrae citazioni, autori e tag da un numero configurabile di pagine.
- Salva i dati in file CSV (citazioni e dettagli sugli autori).
- Raccoglie informazioni dettagliate sugli autori (data e luogo di nascita).
- Logging dettagliato in file dedicato.

## Struttura del progetto

```
quotes-scraper/
├── main.py                  # Entry point
├── scraper/
│   ├── core.py             # Logica principale scraping
│   ├── utils.py            # Salvataggio CSV e scraping autori
│   ├── config.py           # Configurazioni generali
├── data/                   # CSV output (quotes e authors)
├── logs/                   # File di log
```

## Utilizzo

### Requisiti

- Python 3.x
- Librerie: `requests`, `beautifulsoup4`

Installa le dipendenze:

```bash
pip install -r requirements.txt
```

### Esecuzione

```bash
python main.py --pages 5 --output data/quotes.csv --authors data/authors.csv
```

Argomenti:

- `--pages`: Numero di pagine da scrapare (default: 10)
- `--output`: Percorso CSV per le citazioni
- `--authors`: Percorso CSV per i dettagli autori

## Logging

Viene creato un file di log nella cartella `logs/`, utile per tracciare errori e informazioni sull'andamento dello scraping.

## Esempio output

**quotes.csv**

| quote | author | tags |
|-------|--------|------|

**authors.csv**

| name | link | born_date | born_location |
|------|------|-----------|----------------|

## Note

- Il progetto è pensato a scopo didattico.
- Il sito `quotes.toscrape.com` è un sito di test per scraping.

## Autore

Realizzato da Luca Marrazzo nell'ambito del proprio percorso di studio Python e automazione.

---

🚀 Buon scraping!