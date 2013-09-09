#!/usr/bin/python3
# -*- coding: utf-8 -*-

## @package cltSrv
# COURS   : EDF4REPA - IED - Paris 8
# PROJET  : consMaster2
# AUTEUR  : David Calmeille - 11299110@foad.iedparis8.net - L2
# FICHIER : cltSrv.py
# CONTENU : client : Exemples d'utilisation de dialogues client / serveur
# VERSION : 0.2
# LICENCE : GNU

import json
from connexion import Connexion
from codes import *


# 0
nickname = "superU"
password = "superU"

# 1
#nickname = "JD"
#password = "jd123"

# 2
#nickname = "david"
#password = "david"

#nickname = ""
#password = ""

#////////////////////////////////////////////////////////////////////////////
#   USAGE: UTILISATEURS
#////////////////////////////////////////////////////////////////////////////

## Creation d'un nouvel utilisateur
#data = '{"action":"creatUser", "nickname": "'+ nickname +'", "password":"'+ password +'","data":{"nickname": "JD6", "nom": "Dalton", "prenom":"Joe", "email": "JoeDalton@ied.fr", "password":"jd123", "droit":"0"}}'

## Identification d'un utilisateur
#data = '{"action":"identUser", "data":{"nickname": "JDa", "password":"jd123"}}'

## Suppression d'un utilisateur
#data = '{"action":"delMyUser", "data":{"nickname": "JD", "password":"jd123"}}'

## Suppression d'un utilisateur
#data = '{"action":"delUser", "nickname": "'+ nickname +'", "password":"'+ password +'","data":{"id": 4}}'

## Listing des utilisateurs
#data = '{"action":"listUser", "nickname": "'+ nickname +'", "password":"'+ password +'", "data":{"prenom":"Emile", "droit":2}}'
#data = '{"action":"listUser", "nickname": "'+ nickname +'", "password":"'+ password +'", "data":{"droit":29}}'
#data = '{"action":"listUser", "nickname": "'+ nickname +'", "password":"'+ password +'", "data":{"id":2}}'


#////////////////////////////////////////////////////////////////////////////
#   USAGE: EXERCICES
#////////////////////////////////////////////////////////////////////////////

## Creation d'un nouvel exercice

#data = '{"action":"creatExo", "nickname": "'+ nickname +'", "password":"'+ password +'", "data":{"level": 3, "type": "__NG__", "lst": ["(1 2 (3 . 4))"]}}'

##  Loading des exercices
#data = '{"action":"loadExo", "nickname": "'+ nickname +'", "password":"'+ password +'", "data":{"level": 3, "type":"__NDN__"}}'
#data = '{"action":"loadExo", "nickname": "'+ nickname +'", "password":"'+ password +'", "data":{"type":"__NDN__"}}'
#data = '{"action":"loadExo", "nickname": "'+ nickname +'", "password":"'+ password +'", "data":{"level": 3, "type":"__NDN__"}}'
#data = '{"action":"loadExo", "nickname": "'+ nickname +'", "password":"'+ password +'", "data":{"level": 2, "type":"__NG__"}}'
#data = '{"action":"loadExo", "nickname": "'+ nickname +'", "password":"'+ password +'", "data":{"level": 3, "id":3}}'


##  Suppression d'un exercice
#data = '{"action":"delExo", "nickname": "'+ nickname +'", "password":"'+ password +'", "data":{"id": 3}}'

#////////////////////////////////////////////////////////////////////////////


#////////////////////////////////////////////////////////////////////////////
#   USAGE: SOUMISSION
#////////////////////////////////////////////////////////////////////////////

## Creation d'une nouvelle soumission

#data = '{"action":"creatSubm", "nickname": "'+ nickname +'", "password":"'+ password +'", "data":{"exo_id": 8, "soumission":"soumission de nickname"}}'


# listing des soumissions

data = '{"action":"listSubm", "nickname": "superU", "password":"superU" , "data":{"exo_id": "8"}}'

#data = '{"action":"listSubm", "nickname": "superU", "password":"superU" , "data":{"nickname": "superU"}}'

#////////////////////////////////////////////////////////////////////////////

#new_s = Connexion(data) # se base sur COMP
#new_s = Connexion(data, "Off")
#new_s = Connexion(data, "On")
new_s = Connexion(data) ##  ref. COMP dans code.py
print("data", data)

print (new_s.result)

dataSon = json.loads(new_s.result)
#results = dataSon["data"]
#for entry in results:
    #print (entry["lst"])

