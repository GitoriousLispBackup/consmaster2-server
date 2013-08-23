#!/usr/bin/python3
# -*- coding: utf-8 -*-

# COURS   : EDF4REPA - IED - Paris 8
# PROJET  : consMaster2
# AUTEUR  : David Calmeille - 11299110@foad.iedparis8.net - L2
# FICHIER : action.py
# CONTENU : fonctions des actions demandé par le client au serveur
# VERSION : 0.1
# LICENCE : GNU

BDD = "sqlite:///consmaster2.db"

import sys
from datetime import datetime

try:
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.orm import scoped_session
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import Column, Integer, String, Interval, DateTime
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
      return "<Exercice('%s' '%s', '%s')>" % (self.name, self.type, self.level)


engine = create_engine(BDD, echo=False)

# Create tables if they don't exist.
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
