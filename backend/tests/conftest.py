from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from trackerapi.main import app
from trackerapi import models


@pytest.fixture(scope="module")
def db() -> Generator:
    SQLALCHEMY_DATABASE_URL = "sqlite://"

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )

    TestingSessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False, bind=engine
    )

    models.Base.metadata.create_all(bind=engine)
    yield TestingSessionLocal()


@pytest.fixture(scope='module')
def client() -> Generator:
    with TestClient(app) as c:
        yield c
