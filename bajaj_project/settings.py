from pathlib import Path
import os
import dj_database_url
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-replace-this'
DEBUG = False
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'bajaj_project.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'bajaj_project.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
AUTH_PASSWORD_VALIDATORS = []
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
BFHL_FULL_NAME = os.environ.get('BFHL_FULL_NAME', 'nithes_kumar_s')
BFHL_DOB_DDMMYYYY = os.environ.get('BFHL_DOB_DDMMYYYY', '02062004')
BFHL_EMAIL = os.environ.get('BFHL_EMAIL', 'nithes262004@gmail.com')
BFHL_ROLL = os.environ.get('BFHL_ROLL', '22BCE2778')
DATABASES['default'] = dj_database_url.config(default='sqlite:///db.sqlite3')
