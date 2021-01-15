import os


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

FB_APP_ID = 405030733919306
SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"
