import foragido
import rosto
import camera

class Alerta(object):

    def __init__(self, mensagem, Foragido, nome, Rosto, Camera):
        self._mensagem = mensagem
        self._foragido = Foragido(nome, Rosto())
        self._camera = Camera()