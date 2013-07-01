#!/usr/bin/python3
# -*- coding: utf-8 -*-

# COURS   : EDF4REPA - IED - Paris 8
# PROJET  : consMaster2
# AUTEUR  : David Calmeille - 11299110@foad.iedparis8.net - L2
# FICHIER : action.py
# CONTENU : fonctions utilisateur: creation, identification, suppression, listing.
#           fonctions exercices: creation, suppression, loading.
# VERSION : 0.1
# LICENCE : GNU

from database import *
from codes import *

#////////////////////////////////////////////////////////////////////////////
#     UTILISATEUR
#////////////////////////////////////////////////////////////////////////////

def creatUser(data):  # Creation d'un nouvel utilisateur
  try:
      session = Session()
      new_user = User(data["nom"], data["prenom"], data["password"], data["droit"])
      session.add(new_user)
      session.commit()
      insertId = str(new_user.id)
      session.close()
      return '{"status":"success","data":{"id":'+insertId+'}}'
  except Exception as e:
      return '{"status":"error","code":"E_AUC","descrition":"'+ str(e) +'"}'


def identUser(data):  # Identification d'un utilisateur
  try:
      session = Session()
      res = session.query(User). \
                filter(User.nom == data["nom"]). \
                filter(User.password == data["password"]).all()
      session.commit()

      ident = str(res[0].id)
      droit = str(res[0].droit)
      session.close()
      return '{"status":"success","data":{"id":'+ident+',"droit":'+droit+'}}'
  except Exception as e:
      return '{"status":"error","code":"E_AUI","descrition":"'+ str(e) +'"}'


def delUser(data):  # Suppression d'un utilisateur
  try:
      session = Session()
      res = session.query(User).filter(User.id==data["id"]).first()
      session.delete(res)
      session.commit()
      session.close()
      return '{"status":"success","data":{"id":'+str(data["id"])+'}}'
  except Exception as e:
      return '{"status":"error","code":"E_AUD","descrition":"'+ str(e) +'"}'


def listUser(data):  # listing des utilisateurs
  try:
      session = Session()
      q = session.query(User)
      for item, value in data.items():
          q = q.filter(getattr(User, item).like("%%%s%%" % value))
      session.commit()
      response = ""
      for item in q:
          response += ('{"id":' + str(item.id) +',"nom":"'+ item.nom +'","prenom":"'+ item.prenom + '"},')
      session.close()
      return '{"status":"success","data":['+ response[:-1] +']}'
  except Exception as e:
      return '{"status":"error","code":"E_AUL","descrition":"'+ str(e) +'"}'


#////////////////////////////////////////////////////////////////////////////
#     EXERCICES
#////////////////////////////////////////////////////////////////////////////

def creatExo(data):  # Creation d'un nouvel exercice
  try:
      session = Session()
      #exobase = data["__ExoBase__"]
      new_exo = Exercice(data["type"], data["__ExoBase__"] , str(data["lst"]), data["level"])
      session.add(new_exo)
      session.commit()
      insertId = str(new_exo.id)
      session.close()
      return '{"status":"success","data":{"id":'+insertId+'}}'
  except Exception as e:
      return '{"status":"error","code":"E_AEC","descrition":"'+ str(e) +'"}'


def loadExo(data):  # loading des exercices
  try:
      #print(data["__ExoBase__"])
      #print(data)
      session = Session()
      q = session.query(Exercice)
      for item, value in data.items():
          q = q.filter(getattr(Exercice, item).like("%%%s%%" % value))
      session.commit()
      response = ""
      for item in q:
          response += ('{"id":' + str(item.id) +',"type":"'+ item.type +'","__ExoBase__":"'+ item.__ExoBase__ + '","level":"'+ str(item.level) +'", ,"lst":"'+ item.lst +'"}, ')
      session.close()
      return '{"status":"success","data":['+ response[:-1] +']}'
  except Exception as e:
      return '{"status":"error","code":"E_AEL","descrition":"'+ str(e) +'"}'


def delExo(data):  # Suppression d'un exercice
  try:
      session = Session()
      res = session.query(Exercice).filter(Exercice.id==data["id"]).first()
      session.delete(res)
      session.commit()
      session.close()
      return '{"status":"success","data":{"id":'+str(data["id"])+'}}'
  except Exception as e:
      return '{"status":"error","code":"E_AED","descrition":"'+ str(e) +'"}'








