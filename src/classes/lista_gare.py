from datetime import datetime
from typing import Dict, Sequence
from classes.lista_atleti import Lista_Atleti,Atleta
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

	def get_lista_risutlati_per_atleta(self,atleta:Atleta)->Sequence[Gara]:
		'''ritorna la lista di risultati dell'atleta'''
		lista_risultati:Sequence[Risultato] = []
		for gara in self.lista_gare:
			for risultato in gara.lista_risultati:
				if (atleta.id == risultato.atleta.id):
					lista_risultati.append(risultato)
		return lista_risultati

	def get_mappa_atleti_risultati(self,lista_atleti:Lista_Atleti)->Dict:
		'''Ritorna una mappa atleta:[lista di risultati dell'alteta]'''
		res_dict = {}
		for atleta in lista_atleti.get_atleti():
			res_dict[atleta.descr] = self.get_lista_risutlati_per_atleta(atleta)
		return res_dict

	def get_mappa_atleti_risultati_migliori(self,lista_atleti:Lista_Atleti)->Dict:
		temp_dict = self.get_mappa_atleti_risultati(lista_atleti)
		res_dict = {}
		for atleta, lista_risultati in temp_dict.items():
			res_dict[atleta] = []
			for best_risultato in lista_risultati:
				is_best = True
				for risultato in lista_risultati:
					if (risultato.specialita.id == best_risultato.specialita.id and risultato.punteggio > best_risultato.punteggio):
						is_best = False
				if (is_best):
					res_dict[atleta].append(best_risultato)
		return res_dict