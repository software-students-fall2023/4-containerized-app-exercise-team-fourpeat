"""Web app"""
from flask import Flask, render_template
import db

app = Flask(__name__)


@app.route("/")
def animals_db():
    """Return the main page"""
    animals = db.db.collection.find({})
    return render_template("index.html", animals=animals)


if __name__ == "__main__":
    app.run(port=8000)
