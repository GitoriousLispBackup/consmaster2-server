#!/usr/bin/python3
# -*- coding: utf-8 -*-

# COURS   : EDF4REPA - IED - Paris 8
# PROJET  : consMaster2
# AUTEUR  : David Calmeille - 11299110@foad.iedparis8.net - L2
# FICHIER : serveur.py
# CONTENU : Serveur socket
# VERSION : 0.1
# LICENCE : GNU

import socketserver
from codes import *
import json
import time
from database import *
import action
import logging



class MyTCPHandler(socketserver.BaseRequestHandler):
  def handle(self):
      myString = ""

      while 1:
          self.data = self.request.recv(1024)
          myString = myString + self.data.decode("utf-8")
          data_len = len(self.data)

          if not self.data:
              break

          if (data_len) < 1024:
              # decode le format json
              myJson = json.loads(myString)
              # Appelle de la fonction
              res = getattr(action, myJson["action"])(myJson["data"])
              # fichier de log
              logging.warning(str(self.client_address[0]) + " " + myJson["action"])

              # envoie au client
              self.request.sendall(bytes(res, 'utf-8'))


if __name__ == "__main__":


    logging.basicConfig(filename='serveur.log', level=logging.INFO, format='%(asctime)s %(message)s')

    # Cree le serveur, liaison de l'adresse HOST sur le port PORT
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Active le serveur. Ctrl-C pour le stopper
    server.serve_forever()