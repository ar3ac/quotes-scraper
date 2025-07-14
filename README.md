# 🧠 Quote Scraper

Uno scraper in Python che raccoglie citazioni dal sito [quotes.toscrape.com](http://quotes.toscrape.com/) e le salva in un file CSV.  
Strutturato in moduli per rendere il progetto scalabile, ordinato e facile da manutenere.

---

## 📁 Struttura del Progetto

```
quotes-scraper/
├── main.py               # Entry point: gestisce il flusso principale
├── scraper/
│   ├── __init__.py       # (Pacchetto Python)
│   ├── config.py         # Configurazioni (URL, path, costanti)
│   ├── core.py           # Funzioni per scraping e parsing
│   └── utils.py          # Funzioni di supporto (es. salvataggio CSV)
├── data/
│   └── quotes.csv        # Output dei dati
├── log/
│   └── scraper.log       # File di log generato automaticamente
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Funzionalità

- Scraping multi-pagina con gestione dinamica delle URL
- Salvataggio in CSV con separazione dei dati
- Logging avanzato su file e su console
- Struttura modulare: separazione chiara tra configurazione, logica e utility
- Percorsi dei file gestiti dinamicamente via `os.path`

---

## 🧪 Requisiti

- Python 3.6+
- Librerie: `requests`, `beautifulsoup4`

Installa con:

```bash
pip install -r requirements.txt
```

---

## 💻 Esecuzione

Esegui il programma con:

```bash
python main.py
```

Il file CSV verrà salvato in `data/quotes.csv`  
I log saranno visibili in `log/scraper.log`

---

## ✏️ Note tecniche

- Il file `config.py` centralizza tutte le impostazioni (es. URL base, numero di pagine, percorsi)
- Le funzioni di scraping sono in `core.py`
- Le funzioni di salvataggio sono in `utils.py`
- Il file `main.py` gestisce l'esecuzione e configura il logging

---

## 📌 Licenza & Autore

Creato da **Luca Marrazzo**  
Progetto open-source a scopo didattico  
Puoi riutilizzarlo liberamente per apprendere e sperimentare
