from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-t!c!ns!)iyu4$=r-m2)$vmqi1p0e@)kh(2e31%@r=esx=c197p'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'ckeditor',           # ckeditor
    'ckeditor_uploader',  # ckeditor для загрузки картинок
    
    'phonenumber_field', # поле номера телефона

    'rest_framework', # pip install django-rest-framework

    'django_otp',                  # вход в админку с qrcode
    'django_otp.plugins.otp_totp',  # pip install django-otp, pip install qrcode

    'debug_toolbar', # отладка сайта
    
    'accounts', # пользователи
    'app', # мои приложения

    'crispy_forms', # формы
    'django_social_share', # функция поделиться pip install django-social-share
    'django_countries', # pip install django-countries (страны)
    'cities_light', # pip install django-cities-light (города)
    
]

LOGIN_URL ='/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/logout/'
LOGOUT_REDIRECT_URL = '/login/'


# user model
AUTH_USER_MODEL = 'accounts.CustomUser'

# настройка ckeditor
CKEDITOR_UPLOAD_PATH = "uploads/" # настройки ckeditor для загрузки картинок

# настройка для qrcode
OTP_TOTP_ISSUER = 'admin'

# настройки crispy form
CRISPY_TEMPLATE_PACK = 'bootstrap4'


CITIES_LIGHT_CITY_SOURCES = ['http://download.geonames.org/export/dump/cities5000.zip']
CITIES_LIGHT_TRANSLATION_LANGUAGES = ['rus',]
CITIES_LIGHT_INCLUDE_COUNTRIES = ['RUS']



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    # django_otp
    'django_otp.middleware.OTPMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # debug_toolbar
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'delta.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'delta.wsgi.application'


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


LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Asia/Vladivostok'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# настройки static
STATIC_URL = '/static/'

if not DEBUG:
    STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_DIRS = [
    (BASE_DIR / 'static'),
]


# настройки media
MEDIA_URL = '/media/'
MEDIA_ROOT = (BASE_DIR / 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# отладка сайта
INTERNAL_IPS = [
    '127.0.0.1',
]

# закрытие сессий при закрытии браузера
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


# Email настройки
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'dfcdelta@gmail.com'
EMAIL_HOST_PASSWORD = 'tmqhifloroiojwzo'

# twilio - отправка sms
TWILIO_ACCOUNT_SID = 'AC2eadb185256f82c57ce243f382f56c42'
TWILIO_AUTH_TOKEN = 'f33b643bd3cfb66770f8919dffb06c0f'