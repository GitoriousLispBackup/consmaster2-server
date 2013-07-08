#!/usr/bin/python3
# -*- coding: utf-8 -*-

# COURS   : EDF4REPA - IED - Paris 8
# PROJET  : consMaster2
# AUTEUR  : David Calmeille - 11299110@foad.iedparis8.net - L2
# FICHIER : code.py
# CONTENU : codes
# VERSION : 0.1
# LICENCE : GNU


# Connexion au serveur
HOST = "localhost"
PORT = 9991


# Code Erreur Action
E_AUC = "Erreur: creatUser"
E_AUI = "Erreur: identUser"
E_AUD = "Erreur: delUser"
E_AUL = "Erreur: listtUser"

E_AEC = "Erreur: creatExo"
E_AEL = "Erreur: loadExo"
E_AED = "Erreur: delExo"

E_AJS = "Erreur: JSON format"
E_AGA = "Erreur: pas de fonction de ce nom"

# Code Success Action
S_AUC = "creatUser"
S_AUI = "identUser"
S_AUD = "delUser"
S_AUL = "listtUser"

S_AEC = "creatExo"
S_AEL = "loadExo"
S_AED = "delExo"



#Code Erreur Connexion

E_CJS = "Erreur: jsonCheck"
E_CSO = "Erreur: socketCreate"
E_CHO = "Erreur: Nom d\'hôte"
E_CCO = "Erreur: connection"
E_CSE = "Erreur: sendMessage"



# Compression
COMP = "Off"

dic = {
  # action
       #   ' ':'',
   '"action"':'ac',
     '"data"':'da',
     '"nom":':'no:',
   '"prenom"':'pr',
 '"password"':'pa',
    '"droit"':'dr',


 # exos
    '"level"':'le',
     '"type"':'ty',
'"__ExoBase__"':'ex',
  '"__NDN__"':'nd',
      '"lst"':'ls',
      '"dotted"':'do',
      '"normal"':'nr',


 '"listUser"':'lu',
'"creatUser"':'cu',
 '"creatExo"':'ce'
}


