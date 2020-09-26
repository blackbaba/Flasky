import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = '6ae01515e64c92'
    MAIL_PASSWORD = 'c02e04a2bfd8cd'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    ADMINS = ['your-email@example.com']
    POSTS_PER_PAGE = 25
