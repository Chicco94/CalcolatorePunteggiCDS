from datetime import datetime

class Specialita:
	def __init__(self,_id,_descr,_categoria):
		'''id: identificativo fidal
			descr: nome specialità
			categoria: codice categoria fidal (ES: 'JF' per junior donne)
		'''
		self.id = _id
		self.descr = _descr
		self.categoria = _categoria

	def __repr__(self):
		return "{} {}".format(self.descr, self.categoria)