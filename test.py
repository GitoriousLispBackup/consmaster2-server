#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
#           * Suppression d'un utilisateur
# VERSION : 0.1
# LICENCE : GNU

import json
from connexion import Connexion
import codes
import time
import compress/text_huffman

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


    print()
    print("##############################################################")
    print("                    TEST UTILISATEURS                         ")
    print("##############################################################")
    print()

    #Creation d'un nouvel utilisateur
    ts1 = time.time()
    print("##############################################################")
    print("Creation d'un nouvel utilisateur nom:" + str(ts1))
    #data = '{"action":"creatUser", NONPASICI"data":{"nom": "' + str(ts1) +'", "prenom":"Emile", "password":"emzo123", "droit":1}}' # Not OK
    data = '{"action":"creatUser", "data":{"nom": "' + str(ts1) +'", "prenom":"Emile", "password":"emzo123", "droit":1}}' # OK
    test(data, "success", "Creation d'un nouvel utilisateur")


    print()

    #Creation d'un utilisateur deja existant
    print("##############################################################")
    print("Creation d'un utilisateur deja existant nom:" + str(ts1))
    data = '{"action":"creatUser","data":{"nom": "' + str(ts1) +'", "prenom":"Emile", "password":"emzo123", "droit":1}}'
    test(data, "error", "Creation d'un utilisateur deja existant")


    print()

    #Identification d'un utilisateur
    print("##############################################################")
    print("Identification d'un utilisateur existant:" + str(ts1))
    data = '{"action":"identUser","data":{"nom": "' + str(ts1) +'", "password":"emzo123"}}'

    iu = test(data, "success", "Identification d'un utilisateur")
    iuid = 0
    if (iu["status"] == "success" ):
        iuid = iu["data"]["id"]


    print()

    #Identification d'un utilisateur inconnu
    print("##############################################################")
    print("Identification d'un utilisateur inconnu nom: youKnowMe")
    data = '{"action":"identUser","data":{"nom": "youKnowMe", "password":"emzo123"}}'
    test(data, "error", "Identification d'un utilisateur inconnu")


    print()

    # Listing des utilisateurs
    print("##############################################################")
    print('Listing des utilisateurs : "prenom":"Emile","droit":1')
    data = '{"action":"listUser","data":{"prenom":"Emile","droit":1}}'
    test(data, "success", "")

    print()

    # Suppression d'un utilisateur
    print("##############################################################")
    print("Suppression d'un utilisateur id:" + str(iuid))
    data = '{"action":"delUser","data":{"id": '+ str(iuid) +'}}'
    test(data, "success", "Listing des utilisateurs")

    if error :
        print()
        print("##############################################################")
        print("Liste des erreurs: ")
        for i, item in enumerate(error):
            print (item)
        print("##############################################################")


    dede = code_huffman ('{"action":"listUser","data":{"prenom":"Emile","droit":1}}')
    print(decode_huffman (dede))