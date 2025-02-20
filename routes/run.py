from flask import Flask
from models import db
from Controllers.user_controller import user_bp



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Change as needed
db.init_app(app)

app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)
