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
    nom = Column(String, nullable = False, unique = True)
    prenom = Column(String)
    password = Column(String)
    droit = Column(Integer)
    created_date = Column(DateTime, default=datetime.utcnow)

    def __init__(self, nom, prenom, password, droit):
        self.nom = nom
        self.prenom = prenom
        self.password = password
        self.droit = droit

    def __repr__(self):
      return "<User('%s','%s', '%s', '%s')>" % (self.nom, self.prenom, self.password, self.droit)


class Exercice(Base):
    __tablename__ = 'exos'

    id = Column(Integer, primary_key=True)
    type = Column(String)
    __ExoBase__ = Column(String)
    lst = Column(String)
    level = Column(Integer)
    created_date = Column(DateTime, default=datetime.utcnow)

    def __init__(self, type, __ExoBase__, lst, level):
        self.type = type
        self.__ExoBase__ = __ExoBase__
        self.lst = lst
        self.level = level

    def __repr__(self):
      return "<Exercice('%s','%s', '%s', '%s')>" % (self.type, self.__ExoBase__, self.lst, self.level)


engine = create_engine(BDD, echo=False)

# Create tables if they don't exist.
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
