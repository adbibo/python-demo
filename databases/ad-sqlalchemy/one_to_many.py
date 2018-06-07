#!/usr/bin/env python
# -*- coding=utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index, Table
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+pymysql://root:adbibo@127.0.0.1:3306/test", max_overflow=5)

Base = declarative_base()

Session = declarative_base(bind=engine)

session = Session()


class Group(Base):
    __tablename__ = 'groups'

    nid = Column(Integer, primary_key=True, autoincrement=True)

    caption = Column(String(32))


class User(Base):
    __tablename__ = 'users'

    nid = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32))
    group_id = Column(Integer, ForeignKey('groups.nid'))
    group = relationship("Group", backref='user')


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


# 插入数据
session.add_all([
    Group(caption='SA'),
    Group(caption='DEV'),
    Group(caption='TEST'),
    Group(caption='DBA')
])
session.commit()

session.add_all([
    User(username='tom', group_id=1),
    User(username='jerry', group_id=1),
    User(username='jack', group_id=2),
    User(username='rose', group_id=3),
    User(username='eric', group_id=4),
    User(username='james', group_id=4)
])

session.commit()