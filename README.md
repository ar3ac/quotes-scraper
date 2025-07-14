# 🧠 Quote Scraper – Progetto di Web Scraping in Python

Un semplice progetto di web scraping sviluppato in Python, che estrae citazioni, autori e tag dal sito [quotes.toscrape.com](http://quotes.toscrape.com/) e li salva in un file `.csv`.

Questo progetto è parte del mio percorso di apprendimento su Python, con focus su:
- automazione dei dati
- gestione dei file
- logging delle attività
- pulizia del codice

---

## 🚀 Funzionalità

- 🔍 Scansione automatica di più pagine web
- 📑 Estrazione di:
  - Testo della citazione
  - Nome dell’autore
  - Lista di tag associati
- 💾 Salvataggio dei dati in formato CSV (`quotes.csv`)
- 🪵 Logging completo su file (`scraper.log`)
- 📂 Struttura organizzata in cartelle (`/data` e `/log`)

---

## 📁 Struttura del progetto

```
quotes-scraper/
├── data/
│   └── quotes.csv        ← File con tutte le citazioni estratte
├── log/
│   └── scraper.log       ← Log dettagliato dell’attività
├── scraper.py            ← Script principale di scraping
├── README.md             ← Descrizione del progetto
```

---

## ⚙️ Come usarlo

### 1. Requisiti
- Python 3.6+
- Librerie: `requests`, `beautifulsoup4`

Installa le dipendenze con:

```bash
pip install -r requirements.txt
```

*(oppure manualmente)*

```bash
pip install requests beautifulsoup4
```

---

### 2. Esecuzione

Esegui lo script:

```bash
python scraper.py
```

I risultati saranno salvati in:
- `data/quotes.csv`
- `log/scraper.log`

---

## ✏️ Personalizzazione

Puoi modificare facilmente:
- Il numero di pagine da estrarre (`pages_to_scrape`)
- Il nome del file CSV o del log
- Il comportamento in caso di errori o pagine vuote

---

## 📌 Obiettivo del progetto

Questo progetto è stato realizzato con l'obiettivo di:
- Consolidare le basi di Python
- Applicare il web scraping a un sito reale
- Imparare a strutturare e pubblicare codice su GitHub in modo ordinato

---

## 👤 Autore

**Luca Marrazzo**  
Appassionato di automazione e tecnologie.  
In transizione professionale verso il mondo IT.  
👉 [GitHub Profile](https://github.com/TUOUSERNAME)

---

## 📝 Licenza

Distribuito per fini didattici e personali, liberamente modificabile e riutilizzabile.
