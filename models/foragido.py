import rosto

class Foragido(object):

    def __init__(self, nome, Rosto, caminho):
        self._nome = nome
        self._rosto = Rosto(caminho)