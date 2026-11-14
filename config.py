import os

class Config:
    # Clave secreta para mensajes flash y sesiones en Flask
    SECRET_KEY = os.environ.get("SECRET_KEY", "clave_secreta_proyecto_bd_2026")
    
    # Conexión a MongoDB Atlas 
    MONGO_URI = os.environ.get(
        "MONGO_URI", 
        "mongodb+srv://hernandezcaro04n_db_user:u8ErRAoBTJSUWhbX@proyectobasesdatos.hmehemm.mongodb.net/?retryWrites=true&w=majority"
    )
    MONGO_DB_NAME = "eventos_db"

    # Configuración base para Redis (la completará la Persona B)
    REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))
    REDIS_DB = int(os.environ.get("REDIS_DB", 0))