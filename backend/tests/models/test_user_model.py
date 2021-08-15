from sqlalchemy.orm import Session
from trackerapi.models import User


def test_user1_model_create(db: Session) -> None:
    email = 'test1@test.com'
    password = 'testpass'
    user1 = User(email=email, password=password)

    db.add(user1)
    db.commit()
    db.refresh(user1)

    assert user1.email == email
    assert user1.id == 1


def test_user2_model_create(db: Session) -> None:
    email = 'test2@test.com'
    password = 'testpass'
    user2 = User(email=email, password=password)

    db.add(user2)
    db.commit()
    db.refresh(user2)

    assert user2.email == email
    assert user2.id == 2
