#!/usr/bin/python3
# -*- coding: utf-8 -*-

## @package serveur
# COURS   : EDF4REPA - IED - Paris 8
# PROJET  : consMaster2
# AUTEUR  : David Calmeille - 11299110@foad.iedparis8.net - L2
# FICHIER : serveur.py
# CONTENU : Serveur socket
# VERSION : 0.2
# LICENCE : GNU

import socketserver
from codes import *
from database import *
import time
from action import Action
from compress import *
import logging
try:
    from compress import *
except ImportError:
    pass

def module_exists(module_name):
    if globals().get(module_name, False):
        return True
    return False

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
              new_d = decompression(myString)
              myString = new_d.dataDecompression()
              new_a = Action(myString)
              try:
                  logging.warning(str(self.client_address[0]) + " " + new_a.myJson["action"])
              except Exception as e:
                  self.resultat = '{"status":"error","code":"E_SRL","description":"'+ str(e) +'"}'
              if new_d.recomp == "On":
                  new_c = compression(new_a.resultat)
                  new_c.dataCompression()
                  new_a.resultat = new_c.comp
              self.request.sendall(bytes(str(new_a.resultat), 'utf-8'))


if __name__ == "__main__":

    ## Start logging
    logging.basicConfig(filename='serveur.log', level=logging.INFO, format='%(asctime)s %(message)s')

    ## Cree le serveur, liaison de l'adresse HOST sur le port PORT
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    ## Active le serveur. Ctrl-C pour le stopper
    server.serve_forever()