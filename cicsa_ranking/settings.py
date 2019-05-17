"""
Django settings for sailing_dinosaurs project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from sqlalchemy.engine.url import make_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from sqlalchemy.testing.config import db_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# OS Variables
# Django
djangoSecretKey = os.environ.get("DJANGO_SECRET_KEY", "some_random_key_that_will_not_be_used")

# Postgres
user = os.environ.get("DB_USER", "robot")
password = os.environ.get("DB_PASS", "rootpwd")
host = os.environ.get("DB_HOST", "localhost")
port = os.environ.get("DB_PORT", "5432")
name = os.environ.get("DB_NAME", "ranking")
postgresURL = os.environ.get("DATABASE_URL", "None")
postgresTESTURL = os.environ.get("DATABASE_TEST_URL", "postgres://rvrwungzlszlna:4b2ef3fd92609bc967fb67b46797bb053d5f838e531508480eebf810fb802e18@ec2-54-204-2-26.compute-1.amazonaws.com:5432/d7lnt211athrkq")

# Settings
debugMode = os.environ.get("DEBUG_MODE", "TRUE")
useTestDB = os.environ.get("USE_TEST_DB", "TRUE")
compressEnabled = os.environ.get("COMPRESS_ENABLED", "FALSE")

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = djangoSecretKey
DEBUG = True if debugMode == "TRUE" else False
USE_TEST_DB = True if useTestDB == "TRUE" else False
COMPRESS_ENABLED = True if  compressEnabled == "TRUE" else False


ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'scores.cicsailing.ca',
    '.herokuapp.com',
    '.gitpod.io'
    # 'sailing-dinosaurs-system.herokuapp.com',
    # 'sailing-dino-testing.herokuapp.com',
]

SILENCED_SYSTEM_CHECKS = ["fields.W161"]

CORS_ORIGIN_ALLOW_ALL = True

# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'cicsa_ranking.apps.CicsaRankingConfig',
    'panel.apps.PanelConfig',
    'panel.module.management_data.apps.PanelManagementDataConfig',
    'panel.module.management_event.apps.PanelManagementEventConfig',
    'panel.module.management_ranking.apps.PanelManagementRankingConfig',
    'client.apps.ClientConfig',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cicsa_ranking.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            "template",
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'cicsa_ranking.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
if USE_TEST_DB:
    if postgresTESTURL == "None" :
        postgresURL = "postgresql://%s:%s@%s:%s/%s" % (
            user, password, host, port, name
        )
    else:
        postgresURL = postgresTESTURL
else:
    if postgresURL == "None" :
        postgresURL = "postgresql://%s:%s@%s:%s/%s" % (
            user, password, host, port, name
        )


db_url = make_url(postgresURL)
db_host = db_url.host
db_name = db_url.database
db_user = db_url.username
db_pwd = db_url.password
db_port = db_url.port

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_pwd,
        'HOST': db_host,
        'PORT': db_port
    }
}

print("Database Configurations:")
for key, val in DATABASES["default"].items():
    if key not in ["PASSWORD"]:
        print(key, val)

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
