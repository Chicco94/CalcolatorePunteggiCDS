from datetime import datetime
from typing import Sequence
from classes.atleta import Atleta
from classes.gara import Gara,Risultato,Specialita

class Lista_Gare:
	def __init__(self,lista_gare:Sequence[Gara] = []):
		self.lista_gare:Sequence[Gara] = lista_gare

	def __repr__(self):
		ret_string = ""
		for gara in self.lista_gare:
			ret_string += "descrizione: {}\tluogo: {}\tdata: {}\n".format(gara.descr,gara.luogo,gara.data.strftime("%d/%m/%Y"))
			ret_string += "ISCRITTI/RISULTATI\n"
			for risultato in gara.lista_risultati:
				ret_string += "\t" + risultato.__repr__() + "\n"
		return ret_string

	def aggiungi_gara(self,gara:Gara)->Gara:
		self.lista_gare.append(Gara(**gara))
		return gara

	def get_totale_gare_atleta(self,atleta:Atleta)->Atleta:
		'''ritorna in quante gare è stato usato l'atleta'''
		for gara in self.lista_gare:
			for risultato in gara.lista_risultati:
				if (atleta.id == risultato.atleta.id):
					pass
		return atleta