DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
        # Override Django’s default behaviour of using an in-memory database
        # in tests for SQLite, since that avoids connection.close() working.
        "TEST": {"NAME": "test_db.sqlite3"},
    },
}

INSTALLED_APPS = [
    "example",
]

SECRET_KEY = "django-insecure-)6es3666b(7vcth7dm&)^(@e70@%9_f54%1k6*5&k!x_l*56db"
