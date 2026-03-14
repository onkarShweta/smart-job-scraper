import schedule
import time
from scraper import scrape_jobs

schedule.every(6).hours.do(scrape_jobs)

while True:
    schedule.run_pending()
    time.sleep(1)