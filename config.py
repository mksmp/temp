import os

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://flask_db:admin@127.0.0.1:3306/flask_db'

SECRET_KEY = '72f5a72a25d8d5f5a10a9fd21eeec4b2cb347e839c82b061e4ff5e6ad5011b88'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media', 'images')

ADMIN_ROLE_ID = 1
MODER_ROLE_ID = 2
USER_ROLE_ID = 3