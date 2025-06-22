import sqlite3
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


class Database:
    def __init__(self):
        self._setup()
    
    def _setup(self):
        conn = sqlite3.connect('flipkart.db')
        conn.execute("""
                create table if not exists product_info (
                id integer primary key autoincrement,
                title varchar(255),
                image_url varchar(255),
                price  varchar(255),
                created_at timestamp default current_timestamp
            )
        """)
        conn.commit()
        conn.close()
    
    def save(self, products):
        conn = sqlite3.connect('flipkart.db')
        conn.executemany(
            "insert into product_info (title, image_url, price) values (?, ?, ?)",
            [(p['title'], p['image_url'], p['price']) for p in products]
        )
        conn.commit()
        conn.close()


class Flipkart:
    paginator_url = "https://www.flipkart.com/search?q=__keyword__&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=__page__"
    
    def __init__(self):
        self.db = Database()

    def get_content(self, url):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(viewport={"width": 1920, "height": 1080})
            page = context.new_page()
            page.goto(url)
            page.wait_for_timeout(2000)
            content = page.content()
            context.close()
            browser.close()
            return content

    def save_to_db(self, products):
        self.db.save(products)

    def start(self):
        keyword = input("Enter keyword: ")
        all_results = []

        for i in range(3):
            print(f"Scraping page {i+1}...")
            
            url = self.paginator_url.replace("__keyword__", str(keyword)).replace("__page__", str(i + 1))
            content = self.get_content(url)
            soup = BeautifulSoup(content, features="html.parser")
            products = soup.find_all("div", attrs={"data-id": True})

            page_results = []
            for product in products:
                try:
                    title_elements = product.find(attrs={"class": ["wjcEIp", "KzDlHZ"]})
                    price_elements = product.find("div", attrs={"class": ["Nx9bqj", "_4b5DiR"]})
                    image_elements = product.find("img")

                    if title_elements and price_elements and image_elements:
                        title = title_elements.get_text(strip=True)
                        price = price_elements.get_text(strip=True)
                        image_url = image_elements.get("src") or image_elements.get("data-src")

                        result_obj = {
                            "title": title, 
                            "price": price, 
                            "image_url": image_url
                        }
                        page_results.append(result_obj)
                        all_results.append(result_obj)
                except:
                    continue

            print(f"Found {len(page_results)} products on page {i+1}")

        if all_results:
            self.save_to_db(all_results)
            print(f"Total {len(all_results)} products saved to database!")
        else:
            print("No products found!")


if __name__ == "__main__":
    scraper = Flipkart()
    scraper.start()