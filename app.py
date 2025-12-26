from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
FILE_NAME = os.path.join(DATA_DIR, "job_applications.csv")


def setup():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Company", "Role", "Date", "Status"])


@app.route("/")
def index():
    jobs = []
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            jobs.append(row)
    return render_template("index.html", jobs=jobs)


@app.route("/add", methods=["GET", "POST"])
def add_job():
    if request.method == "POST":
        company = request.form["company"]
        role = request.form["role"]
        date = request.form["date"]
        status = "Applied"

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([company, role, date, status])

        return redirect(url_for("index"))

    return render_template("add_job.html")


if __name__ == "__main__":
    setup()
    app.run(debug=True)
