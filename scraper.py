import requests
from bs4 import BeautifulSoup
import sqlite3

URL = "https://realpython.github.io/fake-jobs/"

def scrape_jobs():

    response = requests.get(URL)

    soup = BeautifulSoup(response.text,"html.parser")

    jobs = soup.find_all("div",class_="card-content")

    conn = sqlite3.connect("data/jobs.db")
    cursor = conn.cursor()

    for job in jobs:

        title = job.find("h2").text.strip()
        company = job.find("h3").text.strip()

        cursor.execute(
        "SELECT * FROM jobs WHERE title=? AND company=?",
        (title,company)
        )

        if not cursor.fetchone():

            cursor.execute(
            "INSERT INTO jobs(title,company) VALUES(?,?)",
            (title,company)
            )

    conn.commit()
    conn.close()

    print("Scraping completed")

if __name__ == "__main__":
    scrape_jobs()