#!/usr/bin/python3
# -*- coding: utf-8 -*-

# COURS   : EDF4REPA - IED - Paris 8
# PROJET  : consMaster2
# AUTEUR  : David Calmeille - 11299110@foad.iedparis8.net - L2
# FICHIER : connexion.py
# CONTENU : Class Connexion (client)
# USAGE   : new_a = Connexion(HOST, PORT, data, comp)
# VERSION : 0.1
# LICENCE : GNU

import socket
import time
from codes import *
import json
import sys


class Connexion:

    def __init__(self, mess='', comp=COMP, port=PORT, host=HOST):
        # initilisation des variables
        self.mess = mess
        self.port = port
        self.host = host
        self.comp = comp

        self.jsonCheck()


    def jsonCheck(self):
        # vérifie si le message est au format JSON
        try:
            json.loads(self.mess)
        except ValueError:
            self.erreur = ("Erreur: les données ne sont pas au format JSON")
            return 1

        if (self.comp == "On"):
            print("Compress Me")
            self.socketCreate()
        else:
            self.socketCreate()


    def socketCreate(self):
        # création d'un socket TCP/IP V4 avec une communication par flot de données
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #print ('Socket crée')
        except socket.error:
            self.erreur = ('Erreur: Impossible de créer un socket')
            return 1
        self.connection()


    def connection(self):
        try:
            # Traduit le host name en adresse ip
            self.remote_ip = socket.gethostbyname( self.host )
        except socket.gaierror:
            self.erreur = 'Erreur: Nom de l\'hôte ne peut être résolu.'
            return 1

        try:
            # établit une connexion avec le serveur.
            self.s.connect((self.remote_ip , self.port))
            #print ('Socket Connecté à ' + self.host + ' sur ip: ' + self.remote_ip)
        except socket.error as e:
            self.erreur = "Erreur:Impossible de se connecter à " + self.host + " sur le port: " + str(self.port)
            return 1

        self.sendMessage()


    def sendMessage(self):
        try :
            # Envoie les données au serveur
            self.s.sendall(bytes(self.mess, "utf-8"))
        except socket.error:
            self.erreur = 'Erreur: Impossible d\'envoiyer le message'
            return 1


        #print ('Message envoyer avec succès')

        def recv_timeout(the_socket,timeout=2):
            # faire un socket non bloquante
            the_socket.setblocking(0)

            total_data=[];
            data='';

            #debut du temps
            begin=time.time()
            while 1:
                # si il y a des données, break après le timeout
                if total_data and time.time()-begin > timeout:
                    break

                # si il n'y a pas de données, attendre un peu plus longtemps.
                elif time.time()-begin > timeout*2:
                    break

                # réception
                try:
                    data = str(the_socket.recv(8192), "utf-8")
                    if data:
                        total_data.append(data)
                        # modifier le temps de debut
                        begin=time.time()
                    else:
                        # dormir un certain temps pour indiquer un écart
                        time.sleep(0.1)
                except:
                    pass

            # rejoindre toutes les parties de la chaîne
            return ''.join(total_data)

        # obtenir la réponse
        self.result = (recv_timeout(self.s))
        # tester le resultat code erreur

        # ferme le socket
        self.s.close()