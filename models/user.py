from __future__ import annotations

from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username: str) -> UserModel:
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, id: int) -> UserModel:
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
