from pymongo import MongoClient
from config import Config

try:
    client = MongoClient(Config.MONGO_URI)
    # Verificación rápida de conexión
    client.admin.command('ping')
    db = client[Config.MONGO_DB_NAME]
    
    # Colecciones principales del proyecto
    eventos_collection = db["eventos"]
    entradas_collection = db["entradas"]
    print(" Conexión a MongoDB Atlas establecida correctamente.")
except Exception as e:
    print(f" Error conectando a MongoDB Atlas: {e}")
    db = None
    eventos_collection = None
    entradas_collection = None