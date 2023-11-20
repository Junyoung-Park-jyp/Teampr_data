import os

BASE_DIR = os.path.dirname(__file__)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@127.0.0.1/teamdata'  # MySQL 연결 정보 설정
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"