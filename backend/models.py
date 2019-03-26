from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DATETIME, ForeignKey
from sqlalchemy.orm import relationship, backref
from datetime import datetime

db = SQLAlchemy()

def get_model_dict(model):
    tmp = dict((column.name, getattr(model, column.name)) 
                for column in model.__table__.columns)
    for key in tmp.keys():
        if not isinstance(tmp[key], datetime): continue
        tmp[key] = tmp[key].strftime('%Y/%m/%d')    
    return tmp

class Members(db.Model):
    """
    会員モデル
    """
    __tablename__ = "members"
    id = Column(Integer, primary_key=True)
    name = Column('name', String(255), index=True, unique=True)
    application = Column('application', DATETIME, default=datetime.now, nullable=True)
    winning = Column('winning', DATETIME, nullable=True)
    created = Column('created', DATETIME, default=datetime.now, nullable=False)
    modified = Column('modified', DATETIME, nullable=True)

    #初期化
    def __init__(self, name):
        self.name = name
        self.created = datetime.now()

class Concerts(db.Model):
    """
    コンサートモデル
    """
    __tablename__ = "concerts"
    id = Column(Integer, primary_key=True)
    name = Column('name', String(255), index=True)
    place = Column('place', String(255), nullable=False)
    date = Column('date', DATETIME, nullable=False)
    created = Column('created', DATETIME, default=datetime.now, nullable=False)
    modified = Column('modified', DATETIME, nullable=True)

    #初期化
    def __init__(self, name, place, date):
        self.name = name
        self.place = place
        self.date = date
        self.created = datetime.now()

class Tickets(db.Model):
    """
    チケットモデル
    """
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True)
    member_id = Column('member_id', Integer, ForeignKey('members.id'),index=True, nullable=False)
    concert_id = Column('concert_id', Integer, ForeignKey('concerts.id'), index=True, nullable=False)
    priority = Column('priority', Integer, nullable=False)
    status = Column('status', String(255), nullable=False)
    created = Column('created', DATETIME, default=datetime.now, nullable=False)
    modified = Column('modified', DATETIME, nullable=True)

    #初期化
    def __init__(self, member_id, concert_id, priority, status):
        self.member_id = member_id
        self.concert_id = concert_id
        self.priority = priority
        self.status = status
        self.created = datetime.now()
