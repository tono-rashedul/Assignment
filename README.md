# Flipkart Product Scraper

This Python script scrapes product information (title, price, image URL) from Flipkart using Playwright and BeautifulSoup, and stores it in a local SQLite database.

## Features

- Scrapes multiple pages of Flipkart search results
- Extracts product title, image URL, and price
- Saves results to `flipkart.db` using SQLite

## Setup Instructions

### 1. Clone the repository
```
git clone git@github.com:tono-rashedul/Assignment.git
```
```
cd Assignment
```
### 1. Create and Activate a Virtual Environment (Recommended)

```
# Create virtual environment
python3 -m venv venv
```
```
# Activate on macOS/Linux
source venv/bin/activate
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```

Also install playwright browser binaries:
```
playwright install
```
### 3. Run the Scraper
```
python3 main.py
```

When prompted, enter a keyword (e.g., laptop). The script will scrape 3 pages and store product data in flipkart.db.

### How It Works
> Launches Chromium browser using Playwright

> Loads Flipkart search results for the given keyword

> Uses BeautifulSoup to parse the page

> Extracted data (title, price, image_url) is saved to SQL