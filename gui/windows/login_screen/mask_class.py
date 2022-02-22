from qt_core import *
from gui.windows.login_screen.verify_login import *

class LineEdit(QLineEdit):
	def __init__(self, parent=None):
		QLineEdit.__init__(self, parent=parent)

		self.setPlaceholderText('000.000.000-00')

	def focusInEvent(self, event):
		self.setInputMask('999.999.999-99')

	def focusOutEvent(self, event):
		self.setPlaceholderText('000.000.000-00')
