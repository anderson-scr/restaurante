from qt_core import *
from gui.windows.login_screen.verify_login import *

class LineEdit(QLineEdit):
	def __init__(self, parent=None):
		QLineEdit.__init__(self, parent=parent)
	
	def def_testando(evento, enviador):
		print(evento, enviador)
		if evento == QEvent.KeyPress:
			print('e tecla')
		else:
			print('cago')



def eventFilter(self, source, event):
 
        if event.type() == QEvent.KeyPress and source in [self.ui.lineEdit_data_nasc, self.ui.lineEdit_data_ref, self.ui.lineEdit_data_dep,
                                                            self.ui.lineEdit_data_saida, self.ui.lineEdit_financ_data_inicio, self.ui.lineEdit_financ_data_fim]:
            if event.key() == Qt.Key_Backspace and not source.hasSelectedText():
                
                pos = source.cursorPosition()
                txt = source.text()
 
                if pos >= 2 and txt[source.cursorPosition()-2] == '/':
                    source.setText(txt[0:pos-2] + txt[pos:])
                    source.setCursorPosition(pos-2)
                elif pos >= 1 and txt[source.cursorPosition()-1] != '/':
                    source.setText(txt[0:pos-1] + txt[pos:])
                    source.setCursorPosition(pos-1)
                else:
                    source.setCursorPosition(pos)   
                return True 
                
            if event.key() == Qt.Key_Delete and not source.hasSelectedText():
 
                pos = source.cursorPosition()
                txt = source.text()
                tam = len(txt)
 
                if pos < tam-1 and txt[pos+1] == '/':
                    source.setText(txt[:pos] + txt[pos+2:])
                    source.setCursorPosition(pos)
                elif pos < tam and txt[pos] != '/':
                    source.setText(txt[:pos] + txt[pos+1:])
                    source.setCursorPosition(pos)
                else:
                    source.setCursorPosition(pos)
                return True 
        return False