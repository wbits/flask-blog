from flaskblog import db, login_manager
from flask_login import UserMixin
from flaskblog.domain.user import User as DomainUser
from flaskblog.domain.value_objects import UserId, Username, Email, EncryptedPassword, ProfilePicture


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

    @staticmethod
    def from_domain_user(domain_user: DomainUser):
        return User(
            id=int(domain_user.id()),
            username=str(domain_user.username()),
            email=str(domain_user.email()),
            password=str(domain_user.password()),
            image_file=str(domain_user.profile_picture())
        )

    def to_domain_user(self):
        return DomainUser(
            UserId(str(self.id)),
            Username(self.username),
            Email(self.email),
            EncryptedPassword(self.password)
        )
