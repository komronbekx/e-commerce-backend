import os

import environ
from django.core.wsgi import get_wsgi_application

from config.settings.base import BASE_DIR

env = environ.Env()
environ.Env.read_env(BASE_DIR / ".env")

django_env = env("DJANGO_ENV", default="local")

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    f"config.settings.{django_env}",
)

application = get_wsgi_application()
