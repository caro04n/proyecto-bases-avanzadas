from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)


# (Acuérdate de cambiar <password> por tu contraseña real, sin los signos < >)
MONGO_URI = "mongodb+srv://hernandezcaro04n_db_user:u8ErRAoBTJSUWhbX@proyectobasesdatos.hmehemm.mongodb.net/"

client = MongoClient(MONGO_URI)

# Seleccionamos la base de datos (puedes nombrarla como prefieras, ej: "eventos_db")
db = client["eventos_db"]
# Colección para el catálogo de eventos (F1)
eventos_collection = db["eventos"]

@app.route('/')
def index():
    # Ruta principal para verificar que la app y la base de datos responden
    try:
        # Intentamos hacer un ping rápido a la base de datos
        client.admin.command('ping')
        estado_db = "¡Conectado exitosamente a MongoDB Atlas! 🚀"
    except Exception as e:
        estado_db = f"Error al conectar a la base de datos: {e}"
        
    return f"<h1>Proyecto Bases de Datos Avanzadas</h1><p>{estado_db}</p>"

if __name__ == '__main__':
    app.run(debug=True)