"""
Django settings for myblog project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'blog/templates/blog')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = os.environ.get('SECRETKEY')
SECRET_KEY = '!e^ekq6@t^b@i^u-fu9xw9cdqz&lrz=6p&aw2aguue1-!930bu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS=['makingcomputerssmart.com','www.makingcomputerssmart.com','13.127.61.28', 'localhost']

# Application definition
SUMMERNOTE_THEME = 'bs3'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'django_summernote',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django.contrib.sites',
    'pwa',
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

ROOT_URLCONF = 'myblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ],
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

WSGI_APPLICATION = 'myblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),

    }

}



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

#STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),

        ]

ENV_PATH=os.path.abspath(os.path.dirname(__file__))
MEDIA_URL='/media/'
MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')
MEDIALFILES_DIR=[
        os.path.join(BASE_DIR,'media'),
        ]

SITE_ID = 1
LOGIN_REDIRECT_URL = '/'

X_FRAME_OPTIONS = 'SAMEORIGIN'

AUTHENTICATION_BACKENDS = (
 'django.contrib.auth.backends.ModelBackend',
 'allauth.account.auth_backends.AuthenticationBackend',
 )
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}


SENDGRID_API_KEY='SG.hb8PP6R1S0CbD_ocQDRHMA.OtoAoK7T-hR0eK49S7m7Hj5dwjFOw6ik57yPp_sUDk'

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

SUMMERNOTE_CONFIG = {

    'iframe': False,
}


# Defining PWA
PWA_APP_NAME = 'Making Computers Smart'
PWA_APP_DESCRIPTION = "This blog is about machine learning and deep learning, by Tanmay and Aniket"
PWA_APP_THEME_COLOR = '#6610f2'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'portrait'
PWA_APP_START_URL = 'https://www.makingcomputerssmart.com/'
PWA_APP_STATUS_BAR_COLOR = '#6610f2'
PWA_APP_ICONS = [
    {
        "src": "/static/images/icon-192x192.png",
        "sizes": "192x192",
        "type": "image/png"
    },
    {
        "src": "/static/images/icon-256x256.png",
        "sizes": "256x256",
        "type": "image/png"
    },
    {
        "src": "/static/images/icon-384x384.png",
        "sizes": "384x384",
        "type": "image/png"
    },
    {
        "src": "/static/images/icon-512x512.png",
        "sizes": "512x512",
        "type": "image/png"
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': "/static/images/icon-192x192.png",
        'sizes': '192x192'
    }
]
#PWA_APP_SPLASH_SCREEN = [
#    {
#        'src': '/static/images/icons/splash-640x1136.png',
#        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
#    }
#]
#PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'

#PWA_SERVICE_WORKER_PATH = os.path.join(TEMPLATE_DIR, 'serviceworker.js')
