"""This module sends alerts."""

import smtplib

class AlertController():
	def __init__(self):
		#Cria uma lista de alertas
		pass


	def Imprime_Alerta(self, Alerta):
		"""Print the alert message"""

		#Cria um alerta com esses parametros
		print (Alerta._mensagem)
		#Adiciona a lista de alertas.
		#Imprime
		pass
		
	#Função que gera um email sobre o alerta de foragido
	def gera_gmail(self, Alerta):
		"""Send an e-mail with the message generated by the Alert"""

    	# Credenciais
		remetente    = 'seu-gmail@gmail.com'
		senha        = 'sua-senha'
		 
		# Informações da mensagem
		destinatario = 'email-do-destinatario@qualquercoisa.com'
		assunto      = 'Alerta de Foragido'
		texto        = Alerta._mensagem
		 
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
		pass