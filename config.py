import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
        SECRET_KEY = os.environ.get('SECRET_KEY') # or 'pa55wor0'
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
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