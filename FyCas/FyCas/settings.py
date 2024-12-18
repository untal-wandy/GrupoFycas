

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2%+$&&1q7qun3jro$0m=2k+xmadqian-44$=-s@aknvom9+h-x'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True 

ALLOWED_HOSTS = ['64.23.214.96', 'grupofycas.online', 'www.grupofycas.online', 'localhost','127.0.0.1' ]

CSRF_TRUSTED_ORIGINS = ['https://8000-cs-764470ba-73bf-4820-b736-e9a1023a88b7.cs-us-east1-pkhd.cloudshell.dev']
# Application definition

INSTALLED_APPS = [
    'Shop.apps.ShopConfig',
    'MensApp.apps.MensappConfig', # App de Mensajes
    'Maps.apps.MapsConfig', # App de Mapas
    'Customer.apps.CustomerConfig', # App de Clientes
    # Apps create for the one UntalWandy
    'django.contrib.admin', # App de Administrador
    'django.contrib.auth', # App de Autenticación
    'django.contrib.contenttypes', # App de Tipos de Contenido
    'django.contrib.sessions', # App de Sesiones
    'django.contrib.messages', # App de Mensajes
    'django.contrib.staticfiles', # App de Archivos Estáticos
    'django.contrib.humanize', # App de Humanización
    'django_twilio',  # App de Twilio
    'allauth',  # App de Autenticación
    'allauth.account', # App de Cuentas
    'allauth.socialaccount', # App de Cuentas Sociales
     'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # 
     'allauth.account.middleware.AccountMiddleware', 
]

ROOT_URLCONF = 'FyCas.urls'

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

WSGI_APPLICATION = 'FyCas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-US'
TIME_ZONE = 'America/Santo_Domingo'
USE_I18N = True
USE_L10N = True
USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

GOOGLE_MAPS_API_KEY  = 'AIzaSyAfnJbgtHm5EZLkozG5Dzo_cgkeJndxNjA'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# Se