from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "name": user.name} for user in users]), 200


@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    
    if "id" not in data or "name" not in data:
        return jsonify({"error": "Missing 'id' or 'name' field"}), 400

    new_user = User(id=data["id"], name=data["name"])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User added successfully", "user": {"id": new_user.id, "name": new_user.name}}), 201

if __name__ == '__main__':
    app.run(debug=True)
