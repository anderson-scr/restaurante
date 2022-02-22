login = {
	'064.956.901-69' : '0169',
	'123.456.789-10' : '8910' }

class Login_Verification():
	def cpf_validation(self, cpf):
		if cpf in login.keys():
			return True
		else: False

	def password_validation(self, cpf, password):
		if password == login[cpf]:
			return True
		else: False