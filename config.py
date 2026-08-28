import secrets
import os
from urllib.parse import quote_plus

class Config:
<<<<<<< HEAD
    DB_PASSWORD = os.getenv("DB_PASSWORD", "labinfo") 
    DB_USERNAME = os.getenv("DB_USERNAME", "root")
    SECRET_KEY = os.getenv('SECRET_KEY', secrets.token_hex(16))
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USERNAME}:{quote_plus(DB_PASSWORD)}@localhost:3306/info4v"
=======
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:labinfo@localhost:3306/info4v'
>>>>>>> b25a6837451576e384a6d86b0372eb1612f8723f
