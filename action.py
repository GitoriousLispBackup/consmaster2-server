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
import json

class Action:

    def __init__(self, myString) :
        self.myString = myString
        self.resultat = ''

        # Verifie si la chaine est au format JSON
        try:
            self.myJson = json.loads(myString)
        except Exception as e:
            self.resultat = '{"status":"error","code":"E_AJS","description":"'+ str(e) +'"}'

        # Va executer l'action desirer
        try:
            getattr(Action,self.myJson["action"])(self)
        except Exception as e:
            self.resultat = '{"status":"error","code":"E_AGA","description":"'+ str(e) +'"}'


    #////////////////////////////////////////////////////////////////////////////
    #     UTILISATEUR
    #////////////////////////////////////////////////////////////////////////////

    def creatUser(self):  # Creation d'un nouvel utilisateur
      try:
          session = Session()
          res = session.query(User).filter(User.nom == self.myJson["data"]["nom"]).first()
          if res:
              self.resultat =  '{"status":"error","code":"E_AUC","description":"utilisateur deja existant"}'
          else:
              new_user = User(self.myJson["data"]["nom"], self.myJson["data"]["prenom"], self.myJson["data"]["password"], self.myJson["data"]["droit"])
              session.add(new_user)
              session.commit()
              insertId = str(new_user.id)
              session.close()
              self.resultat = '{"status":"success","code":"S_AUC","data":{"id":'+insertId+'}}'
      except Exception as e:
          self.resultat =  '{"status":"error","code":"E_AUC","description":"'+ str(e) +'"}'


    def identUser(self):  # Identification d'un utilisateur
      try:
          session = Session()
          res = session.query(User). \
                    filter(User.nom == self.myJson["data"]["nom"]). \
                    filter(User.password == self.myJson["data"]["password"]).all()
          session.commit()

          ident = str(res[0].id)
          droit = str(res[0].droit)
          session.close()
          self.resultat =  '{"status":"success","code":"S_AUI","data":{"id":'+ident+',"droit":'+droit+'}}'
      except Exception as e:
          self.resultat =  '{"status":"error","code":"E_AUI","description":"'+ str(e) +'"}'


    def delUser(self):  # Suppression d'un utilisateur
      try:
          session = Session()
          res = session.query(User).filter(User.id==self.myJson["data"]["id"]).first()
          session.delete(res)
          session.commit()
          session.close()
          self.resultat =  '{"status":"success","code":"S_AUD","data":{"id":'+str(self.myJson["data"]["id"])+'}}'
      except Exception as e:
          self.resultat =  '{"status":"error","code":"E_AUD","description":"'+ str(e) +'"}'


    def listUser(self):  # listing des utilisateurs
      try:
          session = Session()
          q = session.query(User)
          for item, value in self.myJson["data"].items():
              q = q.filter(getattr(User, item).like("%%%s%%" % value))
          session.commit()
          response = ""
          for item in q:
              response += ('{"id":' + str(item.id) +',"nom":"'+ item.nom +'","prenom":"'+ item.prenom + '"},')
          session.close()
          self.resultat =  '{"status":"success","code":"S_AUL","data":['+ response[:-1] +']}'
      except Exception as e:
          self.resultat =  '{"status":"error","code":"E_AUL","description":"'+ str(e) +'"}'


    #////////////////////////////////////////////////////////////////////////////
    #     EXERCICES
    #////////////////////////////////////////////////////////////////////////////

    def creatExo(self):  # Creation d'un nouvel exercice
      try:
          session = Session()
          new_exo = Exercice(self.myJson["data"]["type"], self.myJson["data"]["__ExoBase__"] , str(self.myJson["data"]["lst"]), self.myJson["data"]["level"])
          session.add(new_exo)
          session.commit()
          insertId = str(new_exo.id)
          session.close()
          self.resultat =  '{"status":"success","code":"S_AEC","data":{"id":'+insertId+'}}'
      except Exception as e:
          self.resultat =  '{"status":"error","code":"E_AEC","description":"'+ str(e) +'"}'


    def loadExo(self):  # Loading des exercices
      try:
          session = Session()
          q = session.query(Exercice)
          for item, value in self.myJson["data"].items():
              q = q.filter(getattr(Exercice, item).like("%%%s%%" % value))
          session.commit()
          response = ""
          for item in q:
              response += ('{"id":' + str(item.id) +',"type":"'+ item.type +'","__ExoBase__":"'+ item.__ExoBase__ + '","level":"'+ str(item.level) +'", ,"lst":"'+ item.lst +'"}, ')
          session.close()
          self.resultat =  '{"status":"success","code":"S_AEL","data":['+ response[:-1] +']}'
      except Exception as e:
          self.resultat =  '{"status":"error","code":"E_AEL","description":"'+ str(e) +'"}'


    def delExo(self):  # Suppression d'un exercice
      try:
          session = Session()
          res = session.query(Exercice).filter(Exercice.id==self.myJson["data"]["id"]).first()
          session.delete(res)
          session.commit()
          session.close()
          self.resultat =  '{"status":"success","code":"S_AED","data":{"id":'+str(self.myJson["data"]["id"])+'}}'
      except Exception as e:
          self.resultat =  '{"status":"error","code":"E_AED","description":"'+ str(e) +'"}'

