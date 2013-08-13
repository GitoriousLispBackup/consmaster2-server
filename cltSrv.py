#!/usr/bin/python3
# -*- coding: utf-8 -*-

# COURS   : EDF4REPA - IED - Paris 8
# PROJET  : consMaster2
# AUTEUR  : David Calmeille - 11299110@foad.iedparis8.net - L2
# FICHIER : cltSrv.py
# CONTENU : client : Exemples d'utilisation de dialogues client / serveur
# VERSION : 0.1
# LICENCE : GNU

import json
from connexion import Connexion
from codes import *


#////////////////////////////////////////////////////////////////////////////
#   USAGE: UTILISATEURS
#////////////////////////////////////////////////////////////////////////////

#Creation d'un nouvel utilisateur
#data = '{"action":"creatUser","data":{"nom": "Zola", "prenom":"Emile", "password":"emzo123", "droit":1}}'

# Identification d'un utilisateur
#data = '{"action":"identUser","data":{"nom": "Zola", "password":"emzo123"}}'

# Suppression d'un utilisateur
#data = '{"action":"delUser","data":{"id": 41}}'

# Listing des utilisateurs
#data = '{"action":"listUser","data":{"prenom":"Emile","droit":1}}'
#data = '{"action":"listUser","data":{"droit":1}}'
#data = '{"action":"listUser","data":{"id":2}}'


#////////////////////////////////////////////////////////////////////////////
#   USAGE: EXERCICES
#////////////////////////////////////////////////////////////////////////////

#Creation d'un nouvel exercice
#data = '{"action":"creatExo","data":{"level": 3, "type": "__NG__", "__ExoBase__": true, "lst": ["(1 2 (3 . 4))"]}}'

# Loading des exercices
#data = '{"action":"loadExo","data":{"type":"__NDN__","__ExoBase__":1, "level":2}}'
#data = '{"action":"loadExo","data":{"type":"__NDN__","__ExoBase__":1}}'
#data = '{"action":"loadExo","data":{"type":"__NG__"}}'
#data = '{"action":"loadExo","data":{"__ExoBase__":1, "level":2}}'
#data = '{"action":"loadExo","data":{"type":"__NDN__", "level":2}}'
data = '{"action":"loadExo","data":{"id":3}}'

# Suppression d'un exercice
#data = '{"action":"delExo","data":{"id": 14}}'

#////////////////////////////////////////////////////////////////////////////

#new_s = Connexion(data) # se base sur COMP
#new_s = Connexion(data, "Off")
#new_s = Connexion(data, "On")
new_s = Connexion(data) # ref. COMP dans code.py
print("data", data)

print (new_s.result)

#dataSon = json.loads(new_s.result)
#print (dataSon["data"])