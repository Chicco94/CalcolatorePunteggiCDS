class Specialita:
	def __init__(self,id:str,descr:str,categoria:str, tipologia:str="singola"):
		'''id: identificativo fidal
			descr: nome specialità
			categoria: codice categoria fidal (ES: 'JF' per junior donne)
		'''
		self.id = id
		self.descr = descr
		self.categoria = categoria
		self.tipologia = tipologia

	def __repr__(self):
		return "{} {}".format(self.descr, self.categoria)