import google.generativeai as genai
from flask import Blueprint, jsonify, request, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, ChatHistory
from config import Config

routes = Blueprint("routes", __name__)

genai.configure(api_key=Config.GEMINI_API_KEY)

@routes.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@routes.route("/api/chat", methods=["POST"])
@jwt_required()
def chat():
    user_id = get_jwt_identity()
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "Message cannot be empty"}), 400

    try:
        recent_chats = ChatHistory.query.filter_by(user_id=user_id).order_by(ChatHistory.timestamp.desc()).limit(5).all()
        context = "\n".join([f"User: {chat.message}\nAI: {chat.response}" for chat in reversed(recent_chats)])

        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(f"{context}\nUser: {user_message}\nAI:")
        bot_response = response.text or "I'm not sure how to respond."

        chat_entry = ChatHistory(user_id=user_id, message=user_message, response=bot_response)
        db.session.add(chat_entry)
        db.session.commit()

        return jsonify({"response": bot_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes.route("/api/chat-history", methods=["GET"])
@jwt_required()
def chat_history():
    user_id = get_jwt_identity()
    chats = ChatHistory.query.filter_by(user_id=user_id).order_by(ChatHistory.timestamp.desc()).all()
    return jsonify({"chat_history": [{"message": c.message, "response": c.response, "timestamp": c.timestamp} for c in chats]})
