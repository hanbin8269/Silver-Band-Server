import os
import json

# \silver-band=server\silver_band\config
_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# \silver-band=server\silver_band
BASE_DIR = os.path.dirname(_BASE)
# \silver-band=server\silver_band\config
ROOT_DIR = os.path.dirname(BASE_DIR)

CONFIG_SECRET_DIR = os.path.join(ROOT_DIR, ".config_secret")
CONFIG_SECRET_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, "settings_common.json")

if os.path.isfile(CONFIG_SECRET_COMMON_FILE):
    # 로컬 환경 또는 배포 환경
    config_secret_common = json.loads(open(CONFIG_SECRET_COMMON_FILE).read())
else:
    # 테스팅 환경 (환경변수로 지정해야댐)
    config_secret_common = json.loads(os.environ["SECRET_SETTING"])

SECRET_KEY = config_secret_common["django"]["secret_key"]

JWT_AUTH = {
    "JWT_ALLOW_REFRESH": True,
    "JWT_SECRET_KEY": config_secret_common["jwt"]["secret_key"],
    "JWT_ALGORITHM": config_secret_common["jwt"]["algorithm"],
}

DATABASES = config_secret_common["django"]["database"]

AUTH_USER_MODEL = "account.User"

DEBUG = True

ALLOWED_HOSTS = []

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",  # Django가 관리하는 AUTH
]
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "account",
    "gps",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
