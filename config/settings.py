import os.path
from pathlib import Path

from django.conf.global_settings import STATICFILES_DIRS, MEDIA_URL, MEDIA_ROOT

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-(jxvt2raqych%463^g)29b!+=ut5ndhyf-gfun)0l!3_mf0=89'

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'catalog',
    'blog',
    'widget_tweaks',
    'users'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Или 'django.db.backends.postgresql_psycopg2', если требуется
        'NAME': 'DjangoProjectHW',                   # Имя вашей базы данных
        'USER': 'postgres',                           # Имя пользователя PostgreSQL
        'PASSWORD': '0608',                           # Пароль пользователя PostgreSQL
        'HOST': 'localhost',                          # Хост (обычно 'localhost')
        'PORT': '5432',                               # Порт (по умолчанию 5432)
    }
}

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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATICFILES_DIRS = (BASE_DIR / 'static',)

MEDIA_URL = 'media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTH_USER_MODEL = 'users.CustomUser'
