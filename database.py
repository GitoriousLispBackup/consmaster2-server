#!/usr/bin/python3
# -*- coding: utf-8 -*-

## @package database
# COURS   : EDF4REPA - IED - Paris 8
# PROJET  : consMaster2
# AUTEUR  : David Calmeille - 11299110@foad.iedparis8.net - L2
# FICHIER : database.py
# CONTENU : Creation et connexion à la base de donnees.
# VERSION : 0.2
# LICENCE : GNU

BDD = "sqlite:///consmaster2.db"

import sys
from datetime import datetime

try:
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.orm import scoped_session
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import Column, Integer, String, Interval, DateTime, join
    from sqlalchemy import ForeignKey
    from sqlalchemy.orm import relationship, backref
except:
    print ("Error:", "This program needs SQLAlchemy module.")
    sys.exit(1)


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    nickname = Column(String, nullable=False, unique=True)
    nom = Column(String)
    prenom = Column(String)
    email = Column(String)
    password = Column(String, nullable=False)
    droit = Column(Integer, nullable=False)
    created_date = Column(DateTime, default=datetime.utcnow)

    def __init__(self, nickname, nom, prenom, email, password, droit):
        self.nickname = nickname
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.password = password
        self.droit = droit

    def __repr__(self):
      return "<User('%s', '%s','%s','%s','%s','%s')>" % (self.nickname, self.nom, self.prenom, self.email, self.password, self.droit)


class Exercice(Base):
    __tablename__ = 'exos'
    __table_args__ = {'sqlite_autoincrement': True}

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String, nullable=False)
    level = Column(Integer, nullable=False)
    raw = Column(String, nullable=False)
    created_date = Column(DateTime, default=datetime.utcnow)

    def __init__(self, name, type, level, raw):
        self.name = name
        self.type = type
        self.level = level
        self.raw = raw

    def __repr__(self):
      return "<Exercice('%s', '%s', '%s')>" % (self.name, self.type, self.level)


class Soumission(Base):
    __tablename__ = 'soumissions'
    __table_args__ = {'sqlite_autoincrement': True}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    exo_id = Column(Integer, nullable=False)
    soumission = Column(String, nullable=False)
    created_date = Column(DateTime, default=datetime.utcnow)

    def __init__(self, user_id, exo_id, soumission):
        self.user_id = user_id
        self.exo_id = exo_id
        self.soumission = soumission

    def __repr__(self):
      return "<Soumission('%s', '%s', '%s')>" % (self.user_id, self.exo_id, self.soumission)





engine = create_engine(BDD, echo=True)

## Create tables if they don't exist.
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
