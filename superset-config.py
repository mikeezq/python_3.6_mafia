import os
from superset.config import *

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = 'postgresql://myuser:mypassword@127.0.0.1:5432/mydb'

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = ''

# The S3 bucket where the default user avatar is uploaded during user registration.
DEFAULT_AVATAR_S3_BUCKET = ''

# The S3 key of the default user avatar.
DEFAULT_AVATAR_S3_KEY = ''

# Configure a Flask Secret Key
SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
