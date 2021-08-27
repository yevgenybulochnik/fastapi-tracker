import os
from trackerapi.core.config import Settings


def test_config_settings_default():
    os.unsetenv('POSTGRES_SERVER')
    os.unsetenv('POSTGRES_USER')
    os.unsetenv('POSTGRES_PASSWORD')
    os.unsetenv('POSTGRES_DB')
    os.unsetenv('SQLALCHEMY_DATABASE_URI')

    settings = Settings()

    assert settings.SQLALCHEMY_DATABASE_URI == 'sqlite:///./db.sqlite'


def test_config_settings_missing():
    os.unsetenv('POSTGRES_SERVER')
    os.unsetenv('POSTGRES_USER')
    os.unsetenv('POSTGRES_PASSWORD')
    os.unsetenv('POSTGRES_DB')
    os.unsetenv('SQLALCHEMY_DATABASE_URI')

    os.environ['POSTGRES_USER'] = 'testuser'

    settings = Settings()

    assert settings.SQLALCHEMY_DATABASE_URI == 'sqlite:///./db.sqlite'


def test_config_settings_postgres():
    os.unsetenv('POSTGRES_SERVER')
    os.unsetenv('POSTGRES_USER')
    os.unsetenv('POSTGRES_PASSWORD')
    os.unsetenv('POSTGRES_DB')
    os.unsetenv('SQLALCHEMY_DATABASE_URI')

    os.environ['POSTGRES_SERVER'] = 'db'
    os.environ['POSTGRES_USER'] = 'postgres'
    os.environ['POSTGRES_PASSWORD'] = 'postgres'
    os.environ['POSTGRES_DB'] = 'testdb'

    settings = Settings()

    URI = settings.SQLALCHEMY_DATABASE_URI

    assert URI == 'postgresql://postgres:postgres@db/testdb'
