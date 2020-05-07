from flaskblog.domain.error import UserNotFound
from flaskblog.domain.user_repository import UserRepository
from flaskblog.domain.user import User
from flaskblog.domain.value_objects import UserId, Username, Email, EncryptedPassword
from flaskblog import SQLAlchemy
from flaskblog.infrastructure.model.user import User as OrmUser


class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, db: SQLAlchemy):
        self.__db = db

    def next_id(self) -> UserId:
        user = OrmUser(username='', email='', password='')
        self.__db.session.add(user)
        self.__db.session.commit()

        return UserId(str(user.id))

    def save(self, user: User) -> None:
        orm_user = OrmUser.query.get(int(user.id()))
        orm_user.username = str(user.username())
        orm_user.email = str(user.email())
        orm_user.password = str(user.password())
        orm_user.image_file = str(user.profile_picture())
        self.__db.session.commit()

    def get(self, id: UserId) -> User:
        user = OrmUser.query.get(int(id))
        if not user:
            raise UserNotFound

        return self.convert(user)

    def get_by_email(self, email: Email) -> User:
        user = OrmUser.query.filter_by(email=str(email)).first()
        if not user:
            raise UserNotFound

        return self.convert(user)

    @staticmethod
    def convert(orm_user: OrmUser) -> User:
        return User(
            UserId(str(orm_user.id)),
            Username(orm_user.username),
            Email(orm_user.email),
            EncryptedPassword(orm_user.password)
        )
