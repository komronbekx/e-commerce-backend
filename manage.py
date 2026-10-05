import os
import sys

import environ

from config.settings.base import BASE_DIR

env = environ.Env()
environ.Env.read_env(BASE_DIR / ".env")

django_env = env("DJANGO_ENV", default="local")

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    f"config.settings.{django_env}",
)


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"config.settings.{django_env}")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
