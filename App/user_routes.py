from flask import Blueprint, request, jsonify

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/", methods=["GET"])
def get_users():
    return jsonify({"message": "List of users"}), 200

@user_bp.route("/create", methods=["POST"])
def create_user():
    data = request.json
    return jsonify({"message": "User created", "data": data}), 201

