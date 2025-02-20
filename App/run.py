from flask import Flask
from App import create_app
from App import create_app, db
from user_routes import user_bp  

app = create_app()

app = create_app("development")


app = Flask(__name__)

app.register_blueprint(user_bp, url_prefix="/users")

if __name__ == "__main__":
    app.run(debug=True)
    with app.app_context():
        db.create_all()  
    app.run()

    