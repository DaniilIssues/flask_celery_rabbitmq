from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from .database import metadata, db_session


class User(object):
    query = db_session.query_property()

    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.username)


users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('username', String(50), unique=True),
              Column('email', String(120), unique=True),
              Column('password', String(120), unique=False)
              )

mapper(User, users)
