
# 📝 Quote Scraper

Uno scraper Python che estrae citazioni dal sito [quotes.toscrape.com](http://quotes.toscrape.com/), insieme ai dettagli sugli autori. I dati vengono salvati in formato CSV.

---

## 🚀 Funzionalità

- 🔍 Scraping di citazioni da più pagine
- 🧠 Estrazione dettagliata dell'autore (data di nascita, luogo, descrizione)
- 🏷️ Estrazione dei tag associati a ciascuna citazione
- 💾 Salvataggio in due file CSV separati (`quotes.csv` e `authors.csv`)
- 📦 Modularizzazione del codice
- 🔧 Configurabile da riga di comando con `argparse`
- 🧪 Logging completo in `scraper.log`

---

## 🧰 Struttura del progetto

```
quotes-scraper/
├── scraper/
│   ├── __init__.py
│   ├── config.py
│   ├── core.py
│   ├── utils.py
├── data/
│   ├── quotes.csv
│   ├── authors.csv
├── log/
│   └── scraper.log
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Utilizzo

```bash
# Per eseguire lo scraping delle citazioni (default: 10 pagine)
python main.py

# Per specificare numero di pagine e output personalizzato
python main.py --pages 5 --output data/citazioni.csv --authors data/autori.csv

```

---

## 🔧 Configurazione

Le configurazioni di base (URL, cartelle di log e dati, numero pagine) si trovano nel file `scraper/config.py`.  
Puoi modificarlo per adattarlo ai tuoi scopi.

---

## 📦 Requisiti

- Python 3.6+
- Richieste installabili da `requirements.txt`

```bash
pip install -r requirements.txt
```

---

## 🧠 Autore

**Luca Marrazzo**  
Progetto realizzato come parte del mio percorso di crescita in Python e automazione.  
Mi trovi su GitHub: [@ar3ac](https://github.com/ar3ac)

---

## 📌 Note

- Lo script ignora le citazioni senza testo/autore/tag
- È pensato per essere esteso e integrato in altri sistemi
