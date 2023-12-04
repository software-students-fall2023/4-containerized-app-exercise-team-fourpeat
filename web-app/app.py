"""Web app"""
import subprocess
import os
from flask import Flask, render_template, jsonify, request
import db
import speech_recognition as sr
from pymongo import DESCENDING


app = Flask(__name__)
recognizer = sr.Recognizer()


@app.route("/")
def animals_db():
    """Return the main page"""
    animals = db.db["animal_sounds"].find().sort("_id", DESCENDING)
    return render_template("index.html", animals=animals)


path = os.path.join(os.path.dirname(os.path.dirname(__file__)))


@app.route("/capture_audio", methods=['POST'])
def capture_audio():
    """Executes ml.py script in machine-learning-client folder"""
    data = request.get_json()
    animal = data.get("word", "")

    run_path = os.path.join(path, "machine-learning-client", "ml.py")
    subprocess.run(["python", run_path, animal], check=False)
    return jsonify({"success": True})


if __name__ == "__main__":
    app.run(port=8000)
