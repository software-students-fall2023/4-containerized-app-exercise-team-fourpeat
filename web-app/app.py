from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
import db

@app.route('/')
def animals_db():
  return "hello world"
    

if __name__ == '__main__':
  app.run(port=8000)