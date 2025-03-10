import secrets

class Config:
    SECRET_KEY = secrets.token_hex(16) # For Flask security
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:shru6@localhost:5432/AI_CHAT_BOT"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GEMINI_API_KEY = "AIzaSyDBSPAci-nRScxYm-rQ8MJbzTJEBqhCU3A"  # Replace with your actual API key
    JWT_SECRET_KEY = "f8e606b3d0685d3dc05a141711e06044ceaf2643a1c7b1afd946877bf7b91a61"
    JWT_ACCESS_TOKEN_EXPIRES = 3600  #  Tokens expire in 1 hour



