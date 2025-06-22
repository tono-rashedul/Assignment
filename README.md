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
### 2. Create and Activate a Virtual Environment
#### Linux/MacOs
Create virtual environment
```
python3 -m venv venv
```

Activate virtual environment
```
source venv/bin/activate
```

#### Windows (cmd)

Create virtual environment
```
python -m venv venv
```

Activate virtual environment
```
venv\Scripts\activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

Also install playwright browser binaries:
```
playwright install
```
### 4. Run the Scraper
#### Linux/macOS
```
python3 main.py 
```

#### Windows
```
python main.py 
```

When prompted, enter a keyword (e.g., laptop). The script will scrape 3 pages and store product data in `flipkart.db`


**Open `flipkart.db` with any db management tool to see the result.**


### How It Works
> Launches Chromium browser using Playwright.

> Loads Flipkart search results for the given keyword.

> Uses BeautifulSoup to parse the page.

> Extracted data (title, price, image_url) is saved to database.
