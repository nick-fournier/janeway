
import os
import dj_database_url
import dotenv


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load .env file
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)


# SECURITY WARNING: keep the secret key used in production secret!
# You should change this key before you go live!
SECRET_KEY = os.environ.get("SECRET_KEY")


# This is the default redirect if no other sites are found.
DEFAULT_HOST = 'https://localhost:8000'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
LOGIN_REDIRECT_URL = '/user/profile/'

# CATCHA_TYPE should be either 'simple_math' or 'recaptcha' to enable captcha
#fields, otherwise disabled
CAPTCHA_TYPE = 'recaptcha'
RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY")
RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY")

# ORCID Settings
ENABLE_ORCID = True
ORCID_API_URL = 'http://pub.orcid.org/v1.2_rc7/'
ORCID_URL = 'https://orcid.org/oauth/authorize'
ORCID_TOKEN_URL = 'https://pub.orcid.org/oauth/token'
ORCID_CLIENT_SECRET = os.environ.get("ORCID_CLIENT_SECRET")
ORCID_CLIENT_ID = os.environ.get("ORCID_CLIENT_ID")

# Default Langague
LANGUAGE_CODE = 'en'

URL_CONFIG = 'path'  # path or domain

DATABASES = {
    'default': {
        #Example ENGINEs:
        #   sqlite:     'django.db.backends.sqlite
        #   mysql:      'django.db.backends.sqlite
        #   postgres:   'django.db.backends.postgres
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
#        'USER': '',
#        'PASSWORD': '',
#        'HOST': '',
#        'PORT': '',
#        'OPTIONS': {'init_command': 'SET default_storage_engine=INNODB'},
    }
}

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)
