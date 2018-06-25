
class AlertController():
	def __init__(self):
		#Cria uma lista de alertas


	def Imprime_Alerta(foragido, rosto, camera):
		#Cria um alerta com esses parametros
		#Adiciona a lista de alertas.
		#Imprime




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
		