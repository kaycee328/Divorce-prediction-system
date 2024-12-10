import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-=022$ui%j9$%l0_j!(%f7d5f_c9h!w2r!jh=80q(2&*!d&)muf"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third party apps
    "crispy_forms",
    "debug_toolbar",
    "crispy_bootstrap5",
    "rest_framework",
    "corsheaders",
    # my apps
    "main",
    "users",
    "api",
    "prototype",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Adding linkedin
]

ROOT_URLCONF = "dpsproject.urls"
print("pppppppppppppp--------------------pppppppppppppppp")
print(BASE_DIR)
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "dpsproject.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR + "/db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# URL to access static files
STATIC_URL = "/static/"

# Directories where Django will look for additional static files
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Directory where Django will collect all static files when running `collectstatic`
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "media/"

CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACK = "bootstrap5"
# LOGIN_REDIRECT_URL = "dps"
LOGIN_REDIRECT_URL = "http://localhost:8000/dj-rest-auth/linkedin/"
LOGIN_URL = "signin1"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
INTERNAL_IPS = [
    "127.0.0.1",
]
# REST_FRAMEWORK = {
#     "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
# }

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:5173",  # Your React app's origin
# ]

CORS_ALLOW_ALL_ORIGINS = True

"""
    FROM THIS POINT BELOW IS FOR LINKEDIN AUTHENTICATION
"""

SITE_ID = 1
ACCOUNT_EMAIL_VERIFICATION = "none"  # Optional, based on your needs
ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_REQUIRED = False

INSTALLED_APPS += [
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.linkedin_oauth2",
    "dj_rest_auth",
    "rest_framework.authtoken",
]

MIDDLEWARE += [
    "social_django.middleware.SocialAuthExceptionMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

SOCIAL_AUTH_PIPELINE = (
    "social_core.pipeline.social_auth.social_details",
    "social_core.pipeline.social_auth.social_uid",
    "social_core.pipeline.social_auth.auth_allowed",
    "social_core.pipeline.social_auth.social_user",
    "social_core.pipeline.user.get_username",
    "social_core.pipeline.user.create_user",
    "social_core.pipeline.social_auth.associate_user",
    "social_core.pipeline.social_auth.load_extra_data",
    "social_core.pipeline.user.user_details",
)

SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = [
    "id",
    "first-name",
    "last-name",
    "email-address",
]

# LinkedIn OAuth credentials
SOCIALACCOUNT_PROVIDERS = {
    "linkedin_oauth2": {
        "APP": {
            "client_id": "774syucozphm0v",
            "secret": "WPL_AP1.FGympepMcRzQr3cV.61paPg==",
            "key": "",
        },
        "SCOPE": ["r_liteprofile", "r_emailaddress"],
        "PROFILE_FIELDS": ["id", "first-name", "last-name", "email-address"],
    }
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
}
