"""Web app"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def animals_db():
    """Return the main page"""
    return "Hello, Flask!"


if __name__ == "__main__":
    app.run(port=8000)
