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
		'''Ritorna una mappa atleta:[lista dei migliori risultati dell'atleta]'''
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


	def get_mappa_specialita_risultati_di_atleti(self,lista_atleti:Lista_Atleti)->Dict:
		'''Ritorna una mappa specialità:[lista dei migliori risultati per quella specialità di ogni atleta]'''
		temp_dict = self.get_mappa_atleti_risultati_migliori(lista_atleti)
		res_dict = {}
		for _, lista_risultati in temp_dict.items(): 
			for risultato in lista_risultati:
				specialita:Specialita = risultato.specialita
				if specialita.descr in res_dict:
					res_dict[specialita.descr].append(risultato)
				else:
					res_dict[specialita.descr] = [risultato]
		return res_dict

	def copri_gara(self,specialita:Specialita,atleta:Atleta) -> bool:
		if (specialita.tipologia == "staffetta"):
			atleta.totale_staffette += 1
		else:
			atleta.totale_gare += 1
		return atleta.pieno()
	
	def get_best_mappa_per_staffette(self,lista_atleti:Lista_Atleti)->Dict:
		temp_dict = self.get_mappa_specialita_risultati_di_atleti(lista_atleti)
		res_dict = {}
		# per ogni specialità, se ha solo un punteggio, prendo quello
		for specialita,risultati in temp_dict.items():
			if (risultati[0].specialita.tipologia == "staffetta"):
				if (len(risultati) == 4):
					res_dict[specialita] = []
					for risultato in risultati:
						res_dict[specialita].append(risultato)
						self.copri_gara(risultato.specialita,lista_atleti.get_atleta_by_id(risultato.atleta.id))
		return res_dict

	def get_best_mappa_specialita_risultati_di_atleti(self,lista_atleti:Lista_Atleti)->Dict:
		'''Ritorna la migliore mappa specialità:[lista dei migliori risultati per quella specialità di ogni atleta]
		che garantisce il più alto punteggio possibile'''
		temp_dict = self.get_mappa_specialita_risultati_di_atleti(lista_atleti)
		res_dict = self.get_best_mappa_per_staffette(lista_atleti)
		# rimuovo le specialità concluse
		for key in res_dict:
			temp_dict.pop(key,None)

		# per ogni specialità, se ha solo un punteggio, prendo quello
		for specialita,risultati in temp_dict.items():
			if (len(risultati) == 1):
				risultato:Risultato = risultati[0]
				res_dict[specialita] = risultato
				self.copri_gara(risultato.specialita,lista_atleti.get_atleta_by_id(risultato.atleta.id))
		
		# rimuovo le specialità concluse
		for key in res_dict:
			temp_dict.pop(key,None)

		# per ogni altra specialità, prendo il miglior punteggio per quella specialità se l'atleta non è pieno
		for specialita,risultati in temp_dict.items():
			# trovo il miglio punteggio tra quelli proposti
			best_risultato:Risultato = None
			best_punteggio:int = 0
			for risultato in risultati:
				if (risultato.punteggio > best_punteggio and not lista_atleti.get_atleta_by_id(risultato.atleta.id).pieno()):
					best_risultato = risultato
					best_punteggio = risultato.punteggio
			if (not lista_atleti.get_atleta_by_id(best_risultato.atleta.id).pieno()):
				res_dict[specialita] = best_risultato
				self.copri_gara(best_risultato.specialita,lista_atleti.get_atleta_by_id(best_risultato.atleta.id))

		return res_dict