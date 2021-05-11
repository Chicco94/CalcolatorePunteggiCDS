class Specialita:
	def __init__(self,id,descr,categoria):
		'''id: identificativo fidal
			descr: nome specialità
			categoria: codice categoria fidal (ES: 'JF' per junior donne)
		'''
		self.id = id
		self.descr = descr
		self.categoria = categoria

	def __repr__(self):
		return "{} {}".format(self.descr, self.categoria)