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


    #Função que gera um email sobre o alerta de foragido
    def gera_gmail():
    	# Credenciais
		remetente    = 'seu-gmail@gmail.com'
		senha        = 'sua-senha'
		 
		# Informações da mensagem
		destinatario = 'email-do-destinatario@qualquercoisa.com'
		assunto      = 'Alerta de Foragido'
		texto        = _mensagem
		 
		# Preparando a mensagem
		msg = '\r\n'.join([
		  'From: %s' % remetente,
		  'To: %s' % destinatario,
		  'Subject: %s' % assunto,
		  '',
		  '%s' % texto
		  ])
		 
		# Enviando o email
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(remetente,senha)
		server.sendmail(remetente, destinatario, msg)
		server.quit()