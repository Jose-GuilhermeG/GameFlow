from pathlib import Path
from os.path import join
from environ import Env
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent
Env.read_env(join(BASE_DIR, ".env"))

env = Env()
SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG", default=False)
ALLOWED_HOSTS = ["*"]
TRIDY_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django_browser_reload',
    'django_filters',
]
PROJECT_APPS = [
    "users",
    "core",
    "tournament"
]
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]
INSTALLED_APPS = DJANGO_APPS + TRIDY_APPS + PROJECT_APPS
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]
ROOT_URLCONF = "configs.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
WSGI_APPLICATION = "configs.wsgi.application"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("DATABASE_NAME"),
        "USER": env("DATABASE_USER"),
        "HOST": env("DATABASE_HOST"),
        "PASSWORD": env("DATABASE_PASSWORD"),
        "PORT": env("DATABASE_PORT"),
        "ATOMIC_REQUESTS": True,
        "TEST": {
            "NAME": "gameFlow_test",
            "CHARSET": "utf8mb4",
            "COLLATION": "utf8mb4_unicode_ci",
        },
    }
}
FIXTURE_DIRS = [
    BASE_DIR / "fixtures",
]
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

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
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
LENGUAGES = [
    ("en", "English"),
    ("pt-br", "Português"),
]
LOCALE_PATHS = [join(BASE_DIR, "locale")]
STATIC_URL = "/static/"
STATIC_ROOT = join(BASE_DIR, "staticData")
STATICFILES_DIRS = [
    join(BASE_DIR,'static')
]
MEDIA_ROOT = join(BASE_DIR, "media")
MEDIA_URL = "/media/"
AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)
ACCOUNT_EMAIL_VERIFICATION = 'optional'
SITE_ID = 1
ACCOUNT_LOGIN_METHODS = {'email'}
ACCOUNT_SIGNUP_FIELDS = ['email*', 'password1*', 'password2*']
LOGIN_REDIRECT_URL = reverse_lazy("users:profile")
LOGIN_URL = reverse_lazy("users:login")
AUTH_USER_MODEL = 'users.User'

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
