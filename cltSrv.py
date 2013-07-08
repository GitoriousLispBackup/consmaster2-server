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
#data = '{"action":"identUser","data":{"nom": "aqaq", "password":"emzo123"}}'

# Suppression d'un utilisateur
#data = '{"action":"delUser","data":{"id": 3}}'

# Listing des utilisateurs
data = '{"action":"listUser","data":{"prenom":"Emile","droit":1}}'



#////////////////////////////////////////////////////////////////////////////
#   USAGE: EXERCICES
#////////////////////////////////////////////////////////////////////////////

#Creation d'un nouvel exercice
#data = '{"action":"creatExo","data":{"level": 2, "type": "__NG__", "__ExoBase__": true, "lst": ["(1 2 (3 . 4))"]}}'

# Loading des exercices
#data = '{"action":"loadExo","data":{"type":"__NG__","__ExoBase__":1, "level":2}}'

# Suppression d'un exercice
#data = '{"action":"delExoss","data":{"id": 2}}'

#////////////////////////////////////////////////////////////////////////////

new_s = Connexion(data)

print (new_s.result)

#dataSon = json.loads(new_s.result)
#print(dataSon["data"])