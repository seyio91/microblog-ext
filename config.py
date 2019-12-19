import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'pa55wor0'
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        POSTS_PER_PAGE = 3
