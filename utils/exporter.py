import sqlite3
import pandas as pd

def export_excel():

    conn = sqlite3.connect("data/jobs.db")

    query = "SELECT * FROM jobs"

    df = pd.read_sql_query(query,conn)

    df.to_excel("jobs.xlsx",index=False)

    print("Excel exported")