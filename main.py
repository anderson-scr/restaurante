import ctypes
import sys
from qt_core import *
from gui.windows.login_screen.login_window import *
from gui.windows.login_screen.verify_login import *

class Login_screen(QMainWindow, Ui_login_window):
	def eventFilter(self, source, event):
		text = source.text()
		if event.type() == QEvent.KeyPress:
			if event.key() not in self.blocked_key and not source.hasSelectedText() and (len(text) == 3 or len(text) == 7 or len(text) == 11):
				if len(text) != 11: 
					source.setText(text + '.') 
				else: 
					source.setText(text + '-')
		return False

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
		self.blocked_key = (16777219, 16777223, 16777234, 16777236)
		self.setWindowTitle('Login Sistema Goublet')
		self.entry_cpf.installEventFilter(self) # Precisei desse cara para poder usar o evento
		self.login_button.clicked.connect(self.verify_login) # salva o cpf de entrada no atributo

		

if __name__ == "__main__":
	myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
	app = QApplication(sys.argv)
	app.setWindowIcon(QIcon('gui/windows/login_screen/svg_icons/restaurant_logo_white_bg.svg'))
	window = Login_screen()
	window.show()
	sys.exit(app.exec())