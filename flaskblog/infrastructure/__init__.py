from flask_login import current_user, login_user, logout_user
from flaskblog import db
from flaskblog.infrastructure.bcrypt_encryption_service import BCryptEncryptionService
from flaskblog.infrastructure.session import Session
from flaskblog.infrastructure.sqlalchemy_user_repository import SqlAlchemyUserRepository


def user_repository() -> SqlAlchemyUserRepository:
    return SqlAlchemyUserRepository(db)


def encryption_service() -> BCryptEncryptionService:
    return BCryptEncryptionService()


def session() -> Session:
    return Session(current_user, login_user, logout_user)
