# 📝 Quotes Scraper

Uno scraper semplice ma completo, scritto in Python, che estrae citazioni dal sito [quotes.toscrape.com](http://quotes.toscrape.com) e le salva in un file CSV.

## 🚀 Funzionalità principali

- 📄 Estrae citazioni, autori e tag da più pagine
- 🛠️ Struttura modulare (config, core, utils)
- 🧾 Salva i risultati in formato CSV personalizzabile
- 🧠 Logging avanzato su file e console
- 🛡️ Gestione errori e creazione automatica delle cartelle
- 🛎️ Parametri da riga di comando via `argparse`

## 🧪 Come usarlo

Assicurati di avere **Python 3.6+** installato.

Installa i requisiti (solo `beautifulsoup4` e `requests`):

```bash
pip install -r requirements.txt
```

### 📥 Esegui lo scraper

```bash
python main.py
```

Per personalizzare:

```bash
python main.py --pages 5 --output risultati/citazioni.csv
```

## ⚙️ Argomenti CLI disponibili

| Argomento     | Descrizione                            | Default                |
|---------------|----------------------------------------|------------------------|
| `--pages`     | Numero di pagine da scrapare           | `10`                   |
| `--output`    | Percorso del file CSV di output        | `data/quotes.csv`      |

## 🗂️ Struttura del progetto

```
quotes-scraper/
├── scraper/
│   ├── __init__.py
│   ├── config.py
│   ├── core.py
│   └── utils.py
├── data/
│   └── quotes.csv
├── log/
│   └── scraper.log
├── main.py
├── requirements.txt
└── README.md
```

## 📦 requirements.txt

```
requests
beautifulsoup4
```

## 👤 Autore

Luca Marrazzo — progetto sviluppato nel mio percorso di crescita come sviluppatore Python, con attenzione all'automazione e alla qualità del codice.

## 📝 Licenza

Distribuito liberamente per uso personale o didattico. Nessuna licenza formale.