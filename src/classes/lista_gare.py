from datetime import datetime
from classes.gara import Gara,Risultato,Specialita

class Lista_Gare:
	def __init__(self):
		self.lista_gare = []

	def __repr__(self):
		ret_string = ""
		for gara in self.lista_gare:
			ret_string += "descrizione: {}\tluogo: {}\tdata: {}\n".format(gara.descr,gara.luogo,gara.data.strftime("%d/%m/%Y"))
			ret_string += "ISCRITTI/RISULTATI\n"
			for risultato in gara.lista_risultati:
				ret_string += "\t" + risultato.__repr__() + "\n"
		return ret_string

	def aggiungi_gara(self,gara):
		self.lista_gare.append(gara)
		return gara
