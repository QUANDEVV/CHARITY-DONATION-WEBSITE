from app import app, db
from models import User

def seed_database():
    with app.app_context():
        # Drop existing tables and recreate them
        db.drop_all()
        db.create_all()

        # Create sample users
        users_data = [
            {'email': 'z@gmail.com', 'password': 'ilovekennedy', 'user_type': 'donor'},
            {'email': 'k@gmail.com', 'password': 'kenaas', 'user_type': 'charity'},
            {'email': '2@gmail.com', 'password': 'karenwangeshi', 'user_type': 'admin'}
        ]

        for user_data in users_data:
            email = user_data['email']
            password = user_data['password']
            user_type = user_data['user_type']
            user = User(email=email, password=password, user_type=user_type)
            db.session.add(user)

        db.session.commit()

if __name__ == '__main__':
    seed_database()
