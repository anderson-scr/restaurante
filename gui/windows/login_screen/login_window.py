# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *
from gui.windows.login_screen.mask_class import *

class Ui_login_window(object):
	def setupUi(self, login_window):
		if not login_window.objectName():
			login_window.setObjectName(u"login_window")
		login_window.resize(400, 700)
		login_window.setMinimumSize(QSize(400, 700))
		self.trys = 0 # Contador de tentativas
		font = QFont()
		font.setFamilies([u"Cabin"])
		login_window.setFont(font)
		login_window.setStyleSheet(u"")
		self.login_widget = QWidget(login_window)
		self.login_widget.setFocusPolicy(Qt.StrongFocus) # Easy game pai
		self.login_widget.setObjectName(u"login_widget")
		self.login_widget.setEnabled(True)
		self.login_widget.setAutoFillBackground(False)
		self.login_widget.clearFocus()
		self.login_widget.setStyleSheet(u"#login_widget {\n"
"	border-image: url(gui/windows/login_screen/images/background_login_blur.png) 0 0 0 0 stretch stretch;\n"
"}")
		self.horizontalLayout = QHBoxLayout(self.login_widget)
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.login_entrys = QFrame(self.login_widget)
		self.login_entrys.setObjectName(u"login_entrys")
		self.login_entrys.setEnabled(True)
		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.login_entrys.sizePolicy().hasHeightForWidth())
		self.login_entrys.setSizePolicy(sizePolicy)
		self.login_entrys.setMinimumSize(QSize(360, 660))
		self.login_entrys.setMaximumSize(QSize(360, 660))
		self.login_entrys.setLayoutDirection(Qt.LeftToRight)
		self.login_entrys.setAutoFillBackground(False)
		self.login_entrys.setStyleSheet(u"#login_entrys {\n"
"	background-color: rgba(192, 133, 59, .40);\n"
"	border: 3px solid #85311B;\n"
"	border-radius: 10px;\n"
"}")
		self.login_entrys.setFrameShape(QFrame.StyledPanel)
		self.login_entrys.setFrameShadow(QFrame.Raised)
		self.verticalLayout = QVBoxLayout(self.login_entrys)
		self.verticalLayout.setObjectName(u"verticalLayout")
		self.logo_layout = QHBoxLayout()
		self.logo_layout.setObjectName(u"logo_layout")
		self.logo_layout.setContentsMargins(-1, 20, -1, -1)
		self.label_logo = QLabel(self.login_entrys)
		self.label_logo.setObjectName(u"label_logo")
		self.label_logo.setEnabled(True)
		sizePolicy.setHeightForWidth(self.label_logo.sizePolicy().hasHeightForWidth())
		self.label_logo.setSizePolicy(sizePolicy)
		self.label_logo.setMinimumSize(QSize(191, 191))
		self.label_logo.setMaximumSize(QSize(191, 191))
		self.label_logo.setPixmap(QPixmap(u"gui/windows/login_screen/svg_icons/restaurant_logo_blaack.svg"))
		self.label_logo.setScaledContents(True)

		self.logo_layout.addWidget(self.label_logo)


		self.verticalLayout.addLayout(self.logo_layout)

		self.title_layout = QHBoxLayout()
		self.title_layout.setObjectName(u"title_layout")
		self.label_title = QLabel(self.login_entrys)
		self.label_title.setObjectName(u"label_title")
		sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
		self.label_title.setSizePolicy(sizePolicy)
		self.label_title.setMinimumSize(QSize(290, 60))
		self.label_title.setMaximumSize(QSize(290, 60))
		font1 = QFont()
		font1.setFamilies([u"Qwigley"])
		font1.setPointSize(48)
		self.label_title.setFont(font1)
		self.label_title.setScaledContents(False)

		self.title_layout.addWidget(self.label_title)


		self.verticalLayout.addLayout(self.title_layout)

		self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

		self.verticalLayout.addItem(self.verticalSpacer)

		self.sub_title_layout = QHBoxLayout()
		self.sub_title_layout.setObjectName(u"sub_title_layout")
		self.sub_title_layout.setContentsMargins(-1, 0, -1, 0)
		self.label_sub_title = QLabel(self.login_entrys)
		self.label_sub_title.setObjectName(u"label_sub_title")
		sizePolicy.setHeightForWidth(self.label_sub_title.sizePolicy().hasHeightForWidth())
		self.label_sub_title.setSizePolicy(sizePolicy)
		self.label_sub_title.setMinimumSize(QSize(230, 40))
		self.label_sub_title.setMaximumSize(QSize(230, 40))
		font2 = QFont()
		font2.setFamilies([u"Cabin"])
		font2.setPointSize(14)
		self.label_sub_title.setFont(font2)
		self.label_sub_title.setStyleSheet(u"")
		self.label_sub_title.setScaledContents(False)
		self.label_sub_title.setAlignment(Qt.AlignCenter)
		self.label_sub_title.setWordWrap(True)

		self.sub_title_layout.addWidget(self.label_sub_title)


		self.verticalLayout.addLayout(self.sub_title_layout)

		self.cpf_layout = QHBoxLayout()
		self.cpf_layout.setObjectName(u"cpf_layout")
		self.cpf_layout.setContentsMargins(-1, 30, -1, 0)

		
		self.entry_cpf = QLineEdit(self.login_entrys) #Mudei pra line edit, esse role deu um trampo
		self.entry_cpf.setObjectName(u"entry_cpf")
		self.entry_cpf.setEnabled(True)
		sizePolicy.setHeightForWidth(self.entry_cpf.sizePolicy().hasHeightForWidth())
		self.entry_cpf.setSizePolicy(sizePolicy)
		self.entry_cpf.setMinimumSize(QSize(200, 32))
		self.entry_cpf.setMaximumSize(QSize(230, 32))
		self.entry_cpf.setFocusPolicy(Qt.ClickFocus) #Disabilita o focus na entrada da tela
		self.entry_cpf.setFont(font2)
		self.entry_cpf.setPlaceholderText('000.000.000-00')
		self.entry_cpf.setMouseTracking(True)
		self.entry_cpf.setStyleSheet(u"QLineEdit {\n"
			"	background-color: rgba(0,0,0,0);\n"
			"	color: rgb(255, 254, 252);\n"
			"	border-bottom: 2px solid #85311B;\n"
			"	qproperty-frame: false;\n"
			"}\n"
			"QLineEdit:focus {\n"
			"	background-color: rgba(255,199,131, .6);\n"
			"   color: rgb(255, 254, 252);"
			"	border-top-left-radius: 3px;\n"
			"	border-top-right-radius: 3px;\n"
			"}\n"
			"QLineEdit:hover {\n"
			"	background-color: rgba(255,199,131, .6);\n"
			"	border-top-left-radius: 3px;\n"
			"	border-top-right-radius: 3px;\n"
		"}")

		
		self.entry_cpf.setMaxLength(14)
		# validator = QIntValidator().setRange(0, 99999999999) Erro por causa do tamanho do valor. Usar RegEX
		# Essa poha limita a length pra 10. Entao tem que usar o regular expression
		validator = QRegularExpressionValidator("[0-9]*$")
		self.entry_cpf.setValidator(validator) #Deixa entrar somente numeros
		self.entry_cpf.setAlignment(Qt.AlignCenter)
		self.cpf_layout.addWidget(self.entry_cpf)

		########################################################### Cristo senhor amado

		self.entry_senha = QLineEdit(self.login_entrys) #Mudei pra line edit, esse role deu um trampo
		self.entry_senha.setObjectName(u"entry_senha")
		self.entry_senha.setEnabled(True)
		sizePolicy.setHeightForWidth(self.entry_senha.sizePolicy().hasHeightForWidth())
		self.entry_senha.setSizePolicy(sizePolicy)
		self.entry_senha.setMinimumSize(QSize(200, 32))
		self.entry_senha.setMaximumSize(QSize(230, 32))
		self.entry_senha.setFocusPolicy(Qt.ClickFocus) #Disabilita o focus na entrada da tela
		self.entry_senha.setFont(font2)
		self.entry_senha.setMouseTracking(True)
		self.entry_senha.setMaxLength(15)
		self.entry_senha.setEchoMode(QLineEdit.Password)
		self.entry_senha.setAlignment(Qt.AlignCenter)
		self.cpf_layout.addWidget(self.entry_senha)
		self.entry_senha.setStyleSheet(u"QLineEdit {\n"
			"	background-color: rgba(0,0,0,0);\n"
			"	color: rgb(255, 254, 252);\n"
			"	border-bottom: 2px solid #85311B;\n"
			"	qproperty-frame: false;\n"
			"}\n"
			"QLineEdit:focus {\n"
			"	background-color: rgba(255,199,131, .6);\n"
			" color: rgb(255, 254, 252);"
			"	border-top-left-radius: 3px;\n"
			"	border-top-right-radius: 3px;\n"
			"}\n"
			"QLineEdit:hover {\n"
			"	background-color: rgba(255,199,131, .6);\n"
			"	border-top-left-radius: 3px;\n"
			"	border-top-right-radius: 3px;\n"
		"}")
		self.entry_senha.hide()

		########################################################### Cristo senhor amado

		self.verticalLayout.addLayout(self.cpf_layout)

		self.cpf_invalido_layout = QHBoxLayout()
		self.cpf_invalido_layout.setObjectName(u"cpf_invalido_layout")
		self.cpf_invalido = QLabel(self.login_entrys)
		self.cpf_invalido.setObjectName(u"cpf_invalido")
		self.cpf_invalido.setEnabled(True)
		font3 = QFont()
		font3.setFamilies([u"Cabin"])
		font3.setPointSize(12)
		font3.setStyleStrategy(QFont.PreferDefault)
		self.cpf_invalido.setFont(font3)
		self.cpf_invalido.setLayoutDirection(Qt.LeftToRight)
		self.cpf_invalido.setStyleSheet(u"#cpf_invalido {\n"
			"color: red;\n"
		"}")
		self.cpf_invalido.setAlignment(Qt.AlignCenter)

		self.cpf_invalido_layout.addWidget(self.cpf_invalido)


		self.verticalLayout.addLayout(self.cpf_invalido_layout)

		self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

		self.verticalLayout.addItem(self.verticalSpacer_3)

		self.button_layout = QHBoxLayout()
		self.button_layout.setObjectName(u"button_layout")
		self.button_layout.setContentsMargins(-1, 30, -1, -1)
		self.login_button = QPushButton(self.login_entrys)
		self.login_button.setObjectName(u"login_button")
		sizePolicy.setHeightForWidth(self.login_button.sizePolicy().hasHeightForWidth())
		self.login_button.setSizePolicy(sizePolicy)
		self.login_button.setMinimumSize(QSize(180, 40))
		self.login_button.setMaximumSize(QSize(180, 40))
		self.login_button.setFont(font2)

		self.login_button.setCursor(QCursor(Qt.PointingHandCursor))
		self.login_button.setStyleSheet(u"#login_button {\n"
			"	background-color: #85311B;\n"
			"	color: #fffefc;\n"
			"	border-radius: 5px;\n"
			"}\n"
			"#login_button:hover {\n"
			"	background-color: #C1853B;\n"
			"	border: 3px solid #85311B;\n"
			"}\n"
		"")

		self.button_layout.addWidget(self.login_button)


		self.verticalLayout.addLayout(self.button_layout)

		self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

		self.verticalLayout.addItem(self.verticalSpacer_2)


		self.horizontalLayout.addWidget(self.login_entrys)

		login_window.setCentralWidget(self.login_widget)

		self.retranslateUi(login_window)

		QMetaObject.connectSlotsByName(login_window)
# setupUi
	def retranslateUi(self, login_window):
		login_window.setWindowTitle(QCoreApplication.translate("login_window", u"MainWindow", None))
		self.label_logo.setText("")
		self.label_title.setText(QCoreApplication.translate("login_window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:42pt;\">Goublet Restaurant</span></p></body></html>", None))
		self.label_sub_title.setText(QCoreApplication.translate("login_window","Para fazer o login no sistema, entre com seu CPF.", None))
		# self.entry_cpf.setPlaceholderText(QCoreApplication.translate("login_window", u"000.000.000-00", None)) Remove o placeHolder original
		self.login_button.setText(QCoreApplication.translate("login_window", f"Proximo", None))
# retranslateUi

