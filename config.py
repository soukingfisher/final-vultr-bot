import os

class Config:
    DATABASE_URI = 'sqlite:///database.db'
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

config = Config()