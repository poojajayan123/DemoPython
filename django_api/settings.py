import os
from six.moves import urllib
from pymongo import read_preferences

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '6-p%08h$s26t7=j!&mjumodqk)_=)*v@c6)4%q1i47fzr7@tsb'

DEBUG = True

ALLOWED_HOSTS = ['localhost']



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_mongoengine',
    'django_mongoengine',
    'django_mongoengine.mongo_auth',
    'django_mongoengine.mongo_admin',
    'djongo',

    'Question',
    'Exam',
    'Category',
    'User',
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
# REST_FRAMEWORK = {
#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ]
# }

ROOT_URLCONF = 'django_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'django_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# DATABASES = {
#         'default': {
#             'ENGINE': 'djongo',
#             'NAME': 'Proxima',      
#             'HOST' : 'mongodb+srv://root:root@iti.dbmyx.mongodb.net/test',
#             'USER' : 'root',
#             'PASSWORD' : 'root',

#    }
# }

MONGODB_DATABASES = {
    'default' : {
        'MONGODB_NAME'  : 'Proxima',
        
    }
}

import mongoengine
from mongoengine import connect
#SESSION_ENGINE = 'mongoengine.django.sessions'
AUTHENTICATION_BACKENDS = (
       'mongoengine.django.auth.MongoEngineBackend',
        )
_MONGODB_NAME = 'Proxima'
#DEFAULT_CONNECTION_NAME = connect('Proxima')
_MONGODB_DATABASE_HOST = 'mongodb+srv://root:' + urllib.parse.quote_plus('root') + '@iti.dbmyx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

mongoengine.connect(_MONGODB_NAME, host=_MONGODB_DATABASE_HOST)

DATABASES = {
       'default': {
           'ENGINE': 'djongo',
           'NAME': 'Proxima',
           'CLIENT': {
              'host': 'mongodb+srv://root:' + urllib.parse.quote_plus('root') + '@iti.dbmyx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',
              'port': 27017,                                                        
              'username': 'root',
              'password': 'root',
            }
       }
   }

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
# Demo data

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
