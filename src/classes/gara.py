from datetime import datetime

class Gara:
	def __init__(self,_id,_descr,_data,_luogo,_fl_x_cds=False):
		'''id: identificativo fidal
			descr: nome manifestazione
			data nascita nel formato: gg/mm/aaaa
			luogo: luogo manifestazione
			fl_x_cds: True se valido per i CdS
		'''
		self.id = _id
		self.descr = _descr
		self.data = datetime. strptime(_data, '%d/%m/%Y')
		self.luogo = _luogo
		self.fl_x_cds = _fl_x_cds
		self.lista_specialita = []
		self.lista_iscritti = []
		self.lista_risultati = []

	
	def __repr__(self):
		ret_string = "id: {}\ndescrizione: {}\nluogo: {}\ndata: {}\n".format(self.id,self.descr,self.luogo,self.data)
		for specialita in self.lista_specialita:
			ret_string += "\t" + specialita.__repr__() + "\n"
		return ret_string

	def aggiungi_specialità(self,specialita):
		self.lista_specialita.append(specialita)
