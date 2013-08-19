#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
#nickname = "JD2"
#password = "jd123"

#nickname = ""
#password = ""

#////////////////////////////////////////////////////////////////////////////
#   USAGE: UTILISATEURS
#////////////////////////////////////////////////////////////////////////////

#Creation d'un nouvel utilisateur
data = '{"action":"creatUser", "nickname": "'+ nickname +'", "password":"'+ password +'","data":{"nickname": "JD5", "nom": "Dalton", "prenom":"Joe", "email": "JoeDalton@ied.fr", "password":"jd123", "droit":"0"}}'

# Identification d'un utilisateur
#data = '{"action":"identUser","nickname": "'+ nickname +'", "password":"'+ password +'", "data":{"nickname": "JD4", "password":"jd123"}}'

# Suppression d'un utilisateur
#data = '{"action":"delUser", "nickname": "'+ nickname +'", "password":"'+ password +'","data":{"id": 4}}'

# Listing des utilisateurs
#data = '{"action":"listUser", "nickname": "'+ nickname +'", "password":"'+ password +'", "data":{"prenom":"Emile", "droit":2}}'
#data = '{"action":"listUser", "nickname": "'+ nickname +'", "password":"'+ password +'", "data":{"droit":2}}'
#data = '{"action":"listUser", "nickname": "'+ nickname +'", "password":"'+ password +'", "data":{"id":2}}'


#////////////////////////////////////////////////////////////////////////////
#   USAGE: EXERCICES
#////////////////////////////////////////////////////////////////////////////

#Creation d'un nouvel exercice
<<<<<<< HEAD
#data = '{"action":"creatExo", "nickname": "'+ nickname +'", "password":"'+ password +'", "data":{"level": 3, "type": "__NG__", "lst": ["(1 2 (3 . 4))"]}}'

# Loading des exercices
#data = '{"action":"loadExo", "nickname": "'+ nickname +'", "password":"'+ password +'", "data":{"level": 3, "type":"__NDN__"}}'
#data = '{"action":"loadExo", "nickname": "'+ nickname +'", "password":"'+ password +'", "data":{"type":"__NDN__"}}'
#data = '{"action":"loadExo", "nickname": "'+ nickname +'", "password":"'+ password +'", "data":{"level": 3, "type":"__NDN__"}}'
#data = '{"action":"loadExo", "nickname": "'+ nickname +'", "password":"'+ password +'", "data":{"level": 2, "type":"__NG__"}}'
#data = '{"action":"loadExo", "nickname": "'+ nickname +'", "password":"'+ password +'", "data":{"level": 3, "id":3}}'
=======
#data = '{"action":"creatExo","data":{"level": 3, "type": "__NG__", "lst": ["(1 2 (3 . 4))"]}}'

# Loading des exercices
#data = '{"action":"loadExo","data":{"type":"__NDN__", "level":2}}'
#data = '{"action":"loadExo","data":{"type":"__NDN__"}}'
data = '{"action":"loadExo","data":{"type":"__NG__"}}'
#data = '{"action":"loadExo","data":{"level":2}}'
#data = '{"action":"loadExo","data":{"type":"__NG__", "level":3}}'
#data = '{"action":"loadExo","data":{"id":3}}'
>>>>>>> 8a8d74b02b962d888188c8ac2aefafdc35d9bfb2

# Suppression d'un exercice
#data = '{"action":"delExo", "nickname": "'+ nickname +'", "password":"'+ password +'", "data":{"id": 3}}'

#////////////////////////////////////////////////////////////////////////////

#new_s = Connexion(data) # se base sur COMP
#new_s = Connexion(data, "Off")
#new_s = Connexion(data, "On")
new_s = Connexion(data) # ref. COMP dans code.py
print("data", data)

print (new_s.result)

dataSon = json.loads(new_s.result)
<<<<<<< HEAD
#results = dataSon["data"]
#for entry in results:
    #print (entry["lst"])
=======
results = dataSon["data"]
for entry in results:
    print (entry["lst"])
>>>>>>> 8a8d74b02b962d888188c8ac2aefafdc35d9bfb2
