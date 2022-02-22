import sys
from qt_core import *
from gui.windows.login_screen.login_window import *
from gui.windows.login_screen.verify_login import *

class Login_screen(QMainWindow, Ui_login_window):
	def verify_login(self):
		if self.is_cpf: # Entra se for para verificar CPF's
			if Login_Verification.cpf_validation(self, self.entry_cpf.text()): # Chama a funcao da classe login_verifications e altera as informacoes da tela.
				self.user_cpf = self.entry_cpf.text()
				self.is_cpf = False
				self.trys = 0
				self.label_sub_title.setText("Digite sua senha:")
				self.login_button.setText("Entrar")
				self.entry_cpf.hide()
				self.entry_senha.show()
				self.cpf_invalido.setText('')
			else:
				self.cpf_invalido.setText(f"CPF invalido. ({self.trys})")
				self.trys += 1
		else:
			if Login_Verification.password_validation(self, self.user_cpf, self.entry_senha.text()):
				print('Entrou no sistema.')
			else:
				self.cpf_invalido.setText(f"Senha incorreta. ({self.trys})")
				self.trys += 1
			
	def __init__(self):
		super(Login_screen, self).__init__()
		self.setupUi(self)
		self.user_cpf = ''
		self.is_cpf = True
		self.setWindowTitle('Login Sistema Goublet')
		self.login_button.clicked.connect(self.verify_login) # salva o cpf de entrada no atributo

		

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Login_screen()
	window.show()
	sys.exit(app.exec())