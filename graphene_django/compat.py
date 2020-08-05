class MissingType(object):
    pass


try:
    try:  # Django 3.1+ has universal JSONField, old import path will deprecate in 4.0
        from django.db.models import JSONField
    except ImportError:
        from django.contrib.postgres.fields import JSONField

    # Postgres fields are only available in Django with psycopg2 installed
    # and we cannot have psycopg2 on PyPy
    from django.contrib.postgres.fields import (
        ArrayField,
        HStoreField,
        RangeField,
    )
except ImportError:
    ArrayField, HStoreField, JSONField, RangeField = (MissingType,) * 4
