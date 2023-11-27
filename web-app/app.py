"""Web app"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """Return the main page"""
    return "Hello, Flask!"


if __name__ == "__main__":
    app.run(debug=True)
