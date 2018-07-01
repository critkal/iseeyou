"""This module defines Alerta and its methods."""
import foragido
import camera
import smtplib
from datetime import datetime

class Alerta(object):

    def __init__(self, mensagem, Foragido, Camera):
        self._mensagem = mensagem
        self._foragido = Foragido()
        self._camera = Camera()

    

    def cria_mensagem(self):
        """Creates a Message with the data it owns"""
        #get the time
    	now = datetime.now()
        #append all informations on the message
    	self._mensagem = "O foragido " + self._foragido._nome + " foi reconhecido pela " + self._camera._rua + "às " + str(now.hour)+":"\
    		+ str(now.minute) + ":" + str(now.second), "do dia" +  str(now.day) + " do mês " + str(now.month) + " do ano de " +\
    		str (now.year)
    	return self._mensagem


    