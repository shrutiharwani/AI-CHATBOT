from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from models import db
from config import Config
from auth import auth_bp
from routes import routes

app = Flask(__name__, template_folder="templates")
app.config.from_object(Config)

# Initialize extensions
jwt = JWTManager(app)
db.init_app(app)
CORS(app)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(routes)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
