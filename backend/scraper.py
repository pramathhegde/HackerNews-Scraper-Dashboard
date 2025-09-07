import requests
from bs4 import BeautifulSoup
import mysql.connector
import logging
from datetime import datetime
import schedule
import time
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

logging.basicConfig(filename="scraper.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
cursor = conn.cursor()

def scrape_hackernews():
    url = "https://news.ycombinator.com/"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        headlines = soup.select(".titleline a")
        saved_count = 0

        for headline in headlines:
            title = headline.get_text(strip=True)
            link = headline.get("href")

            try:
                cursor.execute("INSERT INTO headlines (title, link, scraped_at) VALUES (%s, %s, %s)",
                               (title, link, datetime.utcnow()))
                conn.commit()
                saved_count += 1
                logging.info(f"Saved: {title}")
            except mysql.connector.errors.IntegrityError:
                logging.info(f"Skipped duplicate: {title}")

        logging.info(f"Scrape complete — {saved_count} new items.")
        print(f"Scrape complete — {saved_count} new items.")
    except Exception as e:
        logging.error(f"Scraping failed: {e}")
        print("Scraping failed. Check scraper.log")

def run_loop(interval_minutes=60):
    schedule.every(interval_minutes).minutes.do(scrape_hackernews)
    logging.info(f"Scheduler started: every {interval_minutes} minutes.")
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Scheduler stopped by user.")

if __name__ == "__main__":
    scrape_hackernews()
    # Uncomment below to run continuously
    # run_loop(60)
    conn.close()
