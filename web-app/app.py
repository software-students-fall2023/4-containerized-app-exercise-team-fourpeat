"""Web app"""
from flask import Flask, render_template, redirect, url_for
import db
import subprocess
import os


app = Flask(__name__)


@app.route("/")
def animals_db():
    """Return the main page"""
    animals = db.db.collection.find({})
    return render_template("index.html", animals=animals)

@app.route('/run')
def run():
    run_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'machine-learning-client', 'ml.py')
    subprocess.run(['python', run_path])
    return redirect(url_for('animals_db'))

if __name__ == "__main__":
    app.run(port=8000)
