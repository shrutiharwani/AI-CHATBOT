import secrets

class Config:
    SECRET_KEY = secrets.token_hex(16) # For Flask security
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:shru6@localhost:5432/AI_CHAT_BOT"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GEMINI_API_KEY = "Your API Key"  # Replace with your actual API key
    JWT_SECRET_KEY = "Your JWT Key"
    JWT_ACCESS_TOKEN_EXPIRES = 3600  #  Tokens expire in 1 hour



