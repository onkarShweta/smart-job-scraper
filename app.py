from flask import Flask
from routes.job_routes import job_routes

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>

<title>Smart Job Scraper</title>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">

</head>

<body class="bg-light">

<div class="container text-center mt-5">

<h1 class="mb-4">Smart Job Scraper</h1>

<p class="lead">A simple job aggregation dashboard built with Python and Flask.</p>

<a href="/jobs" class="btn btn-primary btn-lg mt-3">View Job Listings</a>

</div>

</body>
</html>
"""

app.register_blueprint(job_routes)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000, debug=True)