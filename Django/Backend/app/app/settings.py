"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
import environ


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Read environment variables from .env file
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env.local'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
try:
    SECRET_KEY = env('SECRET_KEY') # From .env.local
except:
    SECRET_KEY = 'django-insecure-#2inylb!j$80j%d2fs@u)@&)p@1rve@pe*jm&7kl3!_*d1ru!5'

# SECURITY WARNING: don't run with debug turned on in production!
try:
    DEBUG = env('ENV_DEBUG') == 'True' # From .env.local
except:
    DEBUG = os.environ.get('DEBUG', True)

# Current environment
try:
    ENVIRONMENT = env('ENV_ENVIRONMENT') # From .env.local
except:
    ENVIRONMENT = os.environ.get('ENVIRONMENT', 'develop')

# Hosts security
CORS_ORIGIN_ALLOW_ALL = False
try:
    ALLOWED_HOSTS = env('ENV_ALLOWED_HOSTS').split(' ') # From .env.local
except:
    ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(' ')
try:
    CORS_ORIGIN_WHITELIST = env('ENV_CORS_ORIGIN_WHITELIST').split(' ') # From .env.local
except:
    CORS_ORIGIN_WHITELIST = os.environ.get('CORS_ORIGIN_WHITELIST', 'http://localhost').split(' ')

# If EXTRACCION
try:
    EXTRACCION = env('ENV_EXTRACCION') == 'True' # From .env.local
except:
    EXTRACCION = os.environ.get('EXTRACCION', False)

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'core',
    'equivalencias', 
    'sources',
    'rest_framework',
    'rest_framework.authtoken',
    'drf_spectacular',
    'user',
    'django_cleanup.apps.CleanupConfig',
    'django_filters',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# PostgreSQL by default
try:
    # From .env.local
    DB_ENGINE = env('ENV_DB_ENGINE')
    DB_HOST = env('ENV_DB_HOST')
    DB_PORT = env('ENV_DB_PORT')
    DB_NAME = env('ENV_DB_NAME')
    DB_USER = env('ENV_DB_USER')
    DB_PASS = env('ENV_DB_PASS')
except:
    DB_ENGINE = os.environ.get('DB_ENGINE', 'django.db.backends.postgresql')
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT', 5432)
    DB_NAME = os.environ.get('DB_NAME')
    DB_USER = os.environ.get('DB_USER')
    DB_PASS = os.environ.get('DB_PASS')

# MSSQL
DB_OPTIONS = {}
if 'mssql' in DB_ENGINE:
    try:
        DB_OPTION_DRIVER = env('ENV_DB_OPTION_DRIVER')
        DB_OPTION_ISOLATION_LEVEL = env('ENV_DB_OPTION_ISOLATION_LEVEL')
    except:
        DB_OPTION_DRIVER = 'ODBC Driver 17 for SQL Server'
        DB_OPTION_ISOLATION_LEVEL = 'READ UNCOMMITTED'
    
    DB_OPTIONS = {
        'driver': DB_OPTION_DRIVER,
        'isolation_level': DB_OPTION_ISOLATION_LEVEL
    }

DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'OPTIONS': DB_OPTIONS
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'documents/')
MEDIA_URL = 'documents/'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'core.User'

REST_FRAMEWORK = {'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
                  'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']}

PASSWORD_RESET_TIMEOUT = 18000