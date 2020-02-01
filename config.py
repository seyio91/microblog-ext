import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
        SECRET_KEY = os.environ.get('SECRET_KEY')
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        POSTS_PER_PAGE = 3
        MAIL_SERVER = os.environ.get('MAIL_SERVER')
        MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
        MAIL_USE_TLS = False
        MAIL_USE_SSL = True
        MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
        MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
        ADMINS = ['seyi_obaweya@yahoo.com']
        LANGUAGES = ['en', 'es']
        MS_TRANSLATOR_KEY=os.environ.get('TRANSLATE_API_KEY')
        ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
        REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'