from flask import Flask, request, jsonify, make_response
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, User
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///uplift.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your-jwt-secret-key'  # Change this to a strong secret key
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


jwt = JWTManager(app)
#allows all origins and should be changed after development
CORS(app, resources={r"/*": {"origins":"*"}})
#when in production
#CORS(app, resources={r"/*": {"origins": "https://your_trusted-frontend-domain.com"}})
migrate = Migrate(app,db)
db.init_app(app)

# Manually create the application context
# with app.app_context():
    # Create the database tables (Since we removed User table, we don't need this anymore)
    # db.create_all()
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Find the user in the database based on email
    user = User.query.filter_by(email=email).first()

    if user and user.password == password:
        return jsonify({'userType': user.user_type})
    else:
        return jsonify({'userType': None})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)