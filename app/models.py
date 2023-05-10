from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, unique=True, index=True, primary_key=True)
    uid = db.Column(db.String(128), nullable=False, unique=True, index=True)
    name = db.Column(db.String(128), nullable=False)
    img = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, uid, name, img):
        self.uid = uid
        self.name = name
        self.img = img

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self

    def to_dict(self):
        return {
            'id': self.id,
            'uid': self.uid,
            'name': self.name,
            'img': self.img,
        }



class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(280), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_uid = db.Column(db.String, db.ForeignKey('user.uid'), nullable=False)
    user = db.relationship('User', backref=db.backref('user', lazy=True))

    def __init__(self, body, user_uid):
        self.body = body
        self.user_uid = user_uid

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self
    
    def clear(self):
        self.carts=[]
        # x=self.carts.all()
        # x.clear()
        # self.carts=x
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'body': self.body,
            'created_at': self.created_at,
            'user': self.user.to_dict(),
        }

