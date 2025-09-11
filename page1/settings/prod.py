from .base import *

DEBUG = False
ALLOWED_HOSTS = ["*"]  



STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
