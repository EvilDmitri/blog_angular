import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

SECRET_KEY = 's3cr3t'
WTF_CSRF_ENABLED = False
CSRF_SESSION_KEY = 'Ck7Ezvg6V6jqUGlk'