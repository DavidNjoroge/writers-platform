from . import db
from datetime import datetime
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(UserMixin,db.Model):
    __tablename__='users'

    id = db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(255))
    # bio=db.Column(db.String(255))
    pass_secure=db.Column(db.String(255))
    article=db.relationship('Article',backref='user',lazy="dynamic")
    comment=db.relationship('Comment',backref='user',lazy="dynamic")


    @property
    def password(self):
        raise AttributeError('sorry you cannot view the password')

    @password.setter
    def password(self,password):
        self.pass_secure=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        # return str(self.username)
        return f'User {self.username}'

class Article(db.Model):
    __tablename__='articles'

    id =db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(255))
    body=db.Column(db.String(255))
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_article(self):
        db.session.add(self)
        db.session.commit()
    def __repr__(self):
        return f'User {self.title}'

class Comment(db.Model):
    __tablename__='comments'

    id=db.Column(db.Integer,primary_key=True)
    body=db.Column(db.String(255))
    article_id=db.Column(db.Integer)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()


    def __repr__(self):
        return f'User {self.body}'
