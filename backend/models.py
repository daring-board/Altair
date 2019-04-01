from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DATETIME, ForeignKey, Time
from sqlalchemy.orm import relationship, backref
from datetime import datetime, time

db = SQLAlchemy()

def get_model_dict(model):
    tmp = dict((column.name, getattr(model, column.name)) 
                for column in model.__table__.columns)
    for key in tmp.keys():
        if isinstance(tmp[key], datetime):
            tmp[key] = tmp[key].strftime('%Y/%m/%d')
        if isinstance(tmp[key], time):
            tmp[key] = tmp[key].strftime('%H:%M:%S')
    return tmp

class Members(db.Model):
    """
    会員モデル
    """
    __tablename__ = "members"
    id = Column(Integer, primary_key=True)
    user_id = Column('user_id', Integer, ForeignKey('users.id'), index=True, nullable=False)
    name = Column('name', String(255), index=True, nullable=False)
    application = Column('application', DATETIME, default=datetime.now, nullable=True)
    winning = Column('winning', DATETIME, nullable=True)
    created = Column('created', DATETIME, default=datetime.now, nullable=False)
    modified = Column('modified', DATETIME, nullable=True)

    #初期化
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.created = datetime.now()

class Concerts(db.Model):
    """
    コンサートモデル
    """
    __tablename__ = "concerts"
    id = Column(Integer, primary_key=True)
    user_id = Column('user_id', Integer, ForeignKey('users.id'), index=True, nullable=False)
    name = Column('name', String(255), nullable=False)
    created = Column('created', DATETIME, default=datetime.now, nullable=False)
    modified = Column('modified', DATETIME, nullable=True)

    #初期化
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.created = datetime.now()

class Schedules(db.Model):
    """
    スケジュールモデル
    """
    __tablename__ = "schedules"
    id = Column(Integer, primary_key=True)
    concert_id = Column('concert_id', Integer, ForeignKey('concerts.id'), index=True, nullable=False)
    date = Column('date', DATETIME, nullable=False)
    time = Column('time', Time, nullable=False)
    place = Column('place', String(255), nullable=False)
    created = Column('created', DATETIME, default=datetime.now, nullable=False)
    modified = Column('modified', DATETIME, nullable=True)

    #初期化
    def __init__(self, concert_id, date, time, place):
        self.concert_id = concert_id
        self.date = date
        self.time = time
        self.place = place
        self.created = datetime.now()

class Tickets(db.Model):
    """
    チケットモデル
    """
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True)
    member_id = Column('member_id', Integer, ForeignKey('members.id'), index=True, nullable=False)
    schedule_id = Column('schedule_id', Integer, ForeignKey('schedules.id'), index=True, nullable=False)
    status = Column('status', String(255), nullable=False)
    number = Column('number', Integer, nullable=False)
    seate = Column('seate', String(255), nullable=True)
    created = Column('created', DATETIME, default=datetime.now, nullable=False)
    modified = Column('modified', DATETIME, nullable=True)

    #初期化
    def __init__(self, member_id, schedule_id, status, number):
        self.member_id = member_id
        self.schedule_id = schedule_id
        self.status = status
        self.number = number
        self.created = datetime.now()

class Users(db.Model):
    """
    ユーザーモデル
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column('username', String(255), index=True, unique=True, nullable=False)
    password = Column('password', String(255), nullable=False)
    created = Column('created', DATETIME, default=datetime.now, nullable=False)
    modified = Column('modified', DATETIME, nullable=True)

    #初期化
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.created = datetime.now()