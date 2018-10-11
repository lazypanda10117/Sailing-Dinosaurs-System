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

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hm*m-^7l7m3ogup&2tz+kvavp)8rice!30$kh$(8)u5%c)n!d_'

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get('DATABASE_URL') is None:
    DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','sailing-dinosaurs-system.herokuapp.com']

SILENCED_SYSTEM_CHECKS = ["fields.W161"]

CORS_ORIGIN_ALLOW_ALL = True

# Application definition

INSTALLED_APPS = [
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

db_remote_url = None;
db_url = 'localhost'
db_name = 'ranking'
db_user = 'lazypanda'
db_pwd = ''
db_port = '5432'

if os.environ.get('DATABASE_URL') is not None:
    db_remote_url = make_url(os.environ.get('DATABASE_URL'));
    db_url = db_remote_url.host;
    db_name = db_remote_url.database;
    db_user = db_remote_url.username;
    db_pwd = db_remote_url.password;
    db_port = db_remote_url.port;
    DATABASES = {
        "default": {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': db_name,
            'USER': db_user,
            'PASSWORD': db_pwd,
            'HOST': db_url,
            'PORT': db_port
        }
    }
else:
    DATABASES = {
        "default": {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': db_name,
            'USER': db_user,
            'PORT': db_port
        }
    }


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
