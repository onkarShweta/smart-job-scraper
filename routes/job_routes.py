from flask import Blueprint, render_template, request
import sqlite3

job_routes = Blueprint("job_routes", __name__)

@job_routes.route("/jobs")
def get_jobs():

    company = request.args.get("company")

    conn = sqlite3.connect("data/jobs.db")
    cursor = conn.cursor()

    if company:
        cursor.execute(
        "SELECT * FROM jobs WHERE company LIKE ?",
        ('%' + company + '%',)
        )
    else:
        cursor.execute("SELECT * FROM jobs")

    rows = cursor.fetchall()

    jobs = []

    for row in rows:
        jobs.append({
            "id": row[0],
            "title": row[1],
            "company": row[2]
        })

    conn.close()

    return render_template("jobs.html", jobs=jobs)