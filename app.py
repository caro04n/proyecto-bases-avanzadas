from flask import Flask, render_template, request, redirect, url_for
from config import Config
from database.mongo_connection import db, eventos_collection

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    # Ruta principal que renderiza tu interfaz web
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)