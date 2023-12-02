"""Web app"""
import subprocess
import os
from flask import Flask, render_template, redirect, url_for
import db
import speech_recognition as sr
from pymongo import DESCENDING



app = Flask(__name__)
recognizer = sr.Recognizer()


@app.route("/")
def animals_db():
    """Return the main page"""
    animals = db.db.collection.find().sort("_id", DESCENDING)
    return render_template("index.html", animals=animals)


path = os.path.join(os.path.dirname(os.path.dirname(__file__)))


@app.route("/run")
def run():
    """Executes ml.py script in machine-learning-client folder"""
    audio = capture_voice_input()
    audio_file_path = os.path.join(path, "machine-learning-client", "temp_audio.wav")
    with open(audio_file_path, "wb") as audio_file:
        audio_file.write(audio.get_wav_data())
        
    run_path = os.path.join(path, "machine-learning-client", "ml.py")
    subprocess.run(["python", run_path, audio_file_path], check=False)
    return redirect(url_for("animals_db"))


def capture_voice_input(timeout=3):
    """Captures audio from microphone with a specified timeout"""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=timeout)
            if not audio:
                print("No audio detected. Please speak louder or try again.")
        except sr.WaitTimeoutError:
            print("Timeout occurred. No audio input received.")
            return redirect(url_for("animals_db"))
    return audio

if __name__ == "__main__":
    app.run(port=8000)
