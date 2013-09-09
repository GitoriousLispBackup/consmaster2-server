#!/usr/bin/python3
# -*- coding: utf-8 -*-

## @package test
# COURS   : EDF4REPA - IED - Paris 8
# PROJET  : consMaster2
# AUTEUR  : David Calmeille - 11299110@foad.iedparis8.net - L2
# FICHIER : test.py
# CONTENU : test des fonctions utilisateurs en realation avec la base de donnees :
#           * Creation d'un nouvel utilisateur nom
#           * Creation d'un utilisateur deja existant
#           * Identification d'un utilisateur
#           * Identification d'un utilisateur inconnu
#           * Listing des utilisateurs
#           * Test du format JSON
#           * Suppression d'un utilisateur
# VERSION : 0.2
# LICENCE : GNU

import sys
import json
from connexion import Connexion
import codes
import time


error = []


def test(data, attendue, tested):
  global error
  new_d = Connexion(data)

  print("Envoyer: " + data)
  print('Prévu:   {"status":"'+ attendue + '", ...') # reponse attendue
  print("Reçu:    " + new_d.result)
  try:
      resultJson = json.loads(new_d.result)
      if (resultJson["status"] != attendue):
          print("Error: " + getattr(codes, resultJson["code"]) + " -> " + data)
          error.append(tested + " -> " + getattr(codes, resultJson["code"]))
          print("#########################  ERROR   ###########################")
      else :
          print("###########################  OK   ############################")
      return resultJson
  except AttributeError:
      print("no json")
      return 1


if __name__ == "__main__":

    Qdroit = ""

    Qdroit = input('Quelle droit pour l\'utilisateur: 0, 1, 2 ou rien : ')

    if (Qdroit == "0") :
        nickname = "superU"
        password = "superU"

    if (Qdroit == "1") :
        nickname = "superEtudiant"
        password = "superEtudiant"

    if (Qdroit == "2") :
        nickname = "Etudiant"
        password = "Etudiant"

    if (Qdroit == "") :
        nickname = ""
        password = ""

    userI = '"nickname": "'+ nickname +'", "password":"'+ password +'",'

    data = '{"action":"identUser","data":{"nickname": "'+ nickname +'", "password":"'+ password +'"}}'
    new_u = Connexion(data)
    resultUser = json.loads(new_u.result)


    if (((Qdroit == "0") or  (Qdroit == "1")) and (str(resultUser["data"])  == "{}")):
        print("L'utilisateur n'existe pas vous devez le créer dans la base: " + userI[:-1])
        sys.exit(0)

    print()
    print("##############################################################")
    print("                    TEST UTILISATEURS                         ")
    print("##############################################################")
    print()

    ## Creation d'un nouvel utilisateur
    ts1 = time.time()
    print("##############################################################")
    print("Creation d'un nouvel utilisateur nickname:" + str(ts1))
    data = '{"action":"creatUser", '+ str(userI) +' "data":{"nickname": "' + str(ts1) +'", "nom": "name", "prenom":"surname", "email": "test@ied.fr", "password":"emzo123", "droit":2}}'
    test(data, "success", "Creation d'un nouvel utilisateur")


    print()

    ## Creation d'un utilisateur deja existant
    print("##############################################################")
    print("Creation d'un utilisateur deja existant nickname:" + str(ts1))
    data = '{"action":"creatUser", '+ str(userI) +' "data":{"nickname": "' + str(ts1) +'", "nom": "name", "prenom":"surname", "email": "test@ied.fr", "password":"emzo123", "droit":1}}'
    test(data, "error", "Creation d'un utilisateur deja existant")


    print()

    ## Identification d'un utilisateur
    print("##############################################################")
    print("Identification d'un utilisateur existant:" + str(ts1))
    data = '{"action":"identUser","data":{"nickname": "' + str(ts1) +'", "password":"emzo123"}}'

    iu = test(data, "success", "Identification d'un utilisateur")
    iuid = 0
    if (iu["status"] == "success" ):
        iuid = iu["data"]["id"]


    print()

    ## Identification d'un utilisateur inconnu
    print("##############################################################")
    print("Identification d'un utilisateur inconnu nickname: youKnowMe")
    data = '{"action":"identUser","data":{"nickname": "youKnowMe", "password":"emzo123"}}'
    test(data, "success", "Identification d'un utilisateur inconnu")


    print()

    ## Listing des utilisateurs
    print("##############################################################")
    print('Listing des utilisateurs : "prenom":"surname","droit":1')
    data = '{"action":"listUser", '+ str(userI) +' "data":{"prenom":"surname","droit":2}}'
    test(data, "success", "Listing des utilisateurs")

    print()

    ## test du format JSON
    print("##############################################################")
    print('Test du format JSON')
    data = '{"action":"listUser", '+ str(userI) +' NON PAS ICI "data":{"prenom":"surname","droit":1}}'
    test(data, "error", "Test du format JSON")

    print()

    ## Suppression d'un utilisateur
    print("##############################################################")
    print("Suppression d'un utilisateur id:" + str(iuid))
    data = '{"action":"delUser", '+ str(userI) +' "data":{"id": '+ str(iuid) +'}}'
    test(data, "success", "Suppression d'un utilisateur")

    if error :
        print()
        print("##############################################################")
        print("Liste des erreurs: ")
        for i, item in enumerate(error):
            print (item)
        print("##############################################################")

