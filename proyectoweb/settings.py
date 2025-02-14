"""
Django settings for proyectoweb project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from msilib.schema import Media
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#para incluir los mensajes de error
from django.contrib.messages import constants as mensajes_de_error

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q!6^hh*44b60lsct@l8=a31$ni6r4ku3j*6a(vvavs_1$^2u_#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #como estaba 27 de de junio
#DEBUG = False

ALLOWED_HOSTS = [] #modifique 27 de junio etaba asi ALLOWED_HOSTS = []

MESSAGE_STORAGE="django.contrib.messages.storage.cookie.CookieStorage"

STATIC_URL_FILES=['D:/SENA 2024/SENA_2024/SANTA BARBARA 2023/CONSTRUIR/proyectoweb/proyectowebapp/static/proyectowebapp',
'D:/SENA 2024/SENA_2024/SANTA BARBARA 2023/CONSTRUIR/proyectoweb/proyectowebapp/static/proyectowebapp/css/gestion.css']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'proyectowebapp',
    'servicios',
    'blog',
    'tienda',
    'carro',
    'autenticacion',
    'crispy_forms',
    'crispy_bootstrap5',
    'pedidos',
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



ROOT_URLCONF = 'proyectoweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['D:/SENA 2024/SENA_2024/SANTA BARBARA 2023/CONSTRUIR/proyectoweb/proyectowebapp/templates/proyectowebapp',
        'D:/SENA 2024/SENA_2024/SANTA BARBARA 2023/CONSTRUIR/proyectoweb/tienda/templates/tienda/tinda.html','D:/SENA 2024/SENA_2024/SANTA BARBARA 2023/CONSTRUIR/proyectoweb/autenticacion/templates/login'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'carro.context_processor.importe_total_carro'#en esta parte registramos lo hecho en el archivo context_processor.py
            ],
        },
    },
]

WSGI_APPLICATION = 'proyectoweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'proyecto',
        'USER':'conectar',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':3306,
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
# cargar las imagenes de los modelos
MEDIA_URL='/media/'
MEDIA_ROOT= 'D:/SENA 2024/SENA_2024/SANTA BARBARA 2023/CONSTRUIR/proyectoweb/media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#configuracion para el envio de mensajes por correo
EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST="smtp.gmail.com"
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER="senaadso058@gmail.com"
#EMAIL_HOST_PASSWORD="santa12345*"
EMAIL_HOST_PASSWORD="diyj hblp oykc ionm"

#para el manejo de los formularios
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

#configuracion de los mensajes de error segun documentacion de Django
MESSAGES_TAGS={
    mensajes_de_error.DEBUG:'debug',
    mensajes_de_error.INFO:'info',
    mensajes_de_error.SUCCESS:'success',
    mensajes_de_error.WARNING:'warning',
    mensajes_de_error.ERROR:'danger',
}