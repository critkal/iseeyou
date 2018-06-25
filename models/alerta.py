import foragido
import rosto
import camera
import smtplib
from datetime import datetime

class Alerta(object):

    def __init__(self, Foragido, Rosto, Camera):
        self._mensagem = mensagem
        self._foragido = Foragido(nome, Rosto())
        self._camera = Camera()

    

    def alerta_foragido():
    	now = datetime.now()
    	_mensagem = "O foragido " + Foragido._nome + " foi reconhecido pela " + Camera._rua + "às " + str(now.hour)+":"
    		+ str(now.minute) + ":" + str(now.second), "do dia" +  str(now.day) + " do mês " + str(now.month) + " do ano de " +
    		str (now.year)
    	return _mensagem


    