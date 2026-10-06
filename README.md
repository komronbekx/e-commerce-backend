# E-Commerce Backend

REST API for an e-commerce application, built with Python, Django and Django REST Framework.

> **Status:** early development. Only the project foundation (configuration, tooling, API docs) is in place so far.

## Tech Stack

- **Python** 3.13+
- **Django** and **Django REST Framework**
- **PostgreSQL** (production) / **SQLite** (local development)
- **JWT authentication** via `djangorestframework-simplejwt`
- **API documentation** via `drf-spectacular` (OpenAPI / Swagger UI)
- **Filtering** via `django-filter`
- **Tooling:** `uv` (dependency management), `ruff` (linting), `mypy` (type checking)

## Prerequisites

- [Python 3.13+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- PostgreSQL (only needed for production settings)

## Getting Started

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd e-commerce-backend
   ```

2. Install dependencies (including development tools):

   ```bash
   uv sync
   ```

3. Create your `.env` file from the example and fill in the values:

   ```bash
   # Linux / macOS
   cp .env.example .env

   # Windows (cmd)
   copy .env.example .env
   ```

4. Apply database migrations:

   ```bash
   uv run python manage.py migrate
   ```

5. Start the development server:

   ```bash
   uv run python manage.py runserver
   ```

The API is now available at `http://127.0.0.1:8000/`.

## API Documentation

With the server running, open the interactive docs:

| Page       | URL                                      |
| ---------- | ---------------------------------------- |
| Swagger UI | `http://127.0.0.1:8000/api/schema/swagger-ui/` |
| ReDoc      | `http://127.0.0.1:8000/api/schema/redoc/`      |
| OpenAPI schema | `http://127.0.0.1:8000/api/schema/`        |

## Configuration

### Settings modules

Settings are split by environment in `config/settings/`:

| Module     | Purpose                                                   |
| ---------- | --------------------------------------------------------- |
| `base.py`  | Shared settings used by every environment                 |
| `local.py` | Local development (SQLite database, debug mode)           |
| `prod.py`  | Production (PostgreSQL database, `DEBUG = False`)         |

`local.py` is used by default. To use another module, set the `DJANGO_SETTINGS_MODULE`
environment variable, for example `config.settings.prod`.

### Environment variables

Variables are loaded from the `.env` file in the project root. See `.env.example` for the
full list and a template. **Never commit your real `.env` file.**

| Variable        | Used in    | Description                                         |
| --------------- | ---------- | --------------------------------------------------- |
| `SECRET_KEY`    | all        | Django secret key. Must be unique and kept private. |
| `DEBUG`         | local      | Enables Django debug mode.                          |
| `ALLOWED_HOSTS` | all        | Comma-separated list of allowed host names.         |
| `DB_NAME`       | production | PostgreSQL database name.                           |
| `DB_USER`       | production | PostgreSQL user.                                    |
| `DB_PASSWORD`   | production | PostgreSQL password.                                |
| `DB_HOST`       | production | PostgreSQL host (default: `localhost`).             |
| `DB_PORT`       | production | PostgreSQL port (default: `5432`).                  |

## Code Quality

Run the linter and the type checker before committing:

```bash
uv run ruff check .
uv run mypy .
```
