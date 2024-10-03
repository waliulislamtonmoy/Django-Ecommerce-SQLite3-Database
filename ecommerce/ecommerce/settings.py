
from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES_DIR=os.path.join(BASE_DIR/'templates')
STATIC_DIR=os.path.join(BASE_DIR/'static')
MEDIA_DIR=os.path.join(BASE_DIR/'media')


SECRET_KEY = 'django-insecure-_&#c*l8&bk+ns&zpk4-a_e4o8q5id^0^btqbjq)0&+vx-*=j_0'


DEBUG = True

ALLOWED_HOSTS = ['*']




INSTALLED_APPS = [
    "crispy_forms",
    "crispy_tailwind",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'App_Account',
    'App_Shop',
]


#CUSTOM USER MODEL
AUTH_USER_MODEL='App_Account.User'

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

#{% load tailwind_filters %}
#{% load crispy_forms_tags %}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates',],
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

WSGI_APPLICATION = 'ecommerce.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_TZ = True




STATIC_URL='/static/'
STATICFILES_DIRS=[STATIC_DIR,]
MEDIA_URL='/media/'
MEDIA_ROOT=MEDIA_DIR
MEDIAFILES_DIRS=MEDIA_ROOT


LOGIN_URL='/accounts/login/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
