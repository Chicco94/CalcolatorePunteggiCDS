from datetime import datetime
from classes.risultato import Risultato,Specialita

class Gara:
	def __init__(self,id,descr,data,luogo,fl_x_cds=False):
		'''id: identificativo fidal
			descr: nome manifestazione
			data nascita nel formato: gg/mm/aaaa
			luogo: luogo manifestazione
			fl_x_cds: True se valido per i CdS
		'''
		self.id = id
		self.descr = descr
		self.data = datetime. strptime(data, '%d/%m/%Y')
		self.luogo = luogo
		self.fl_x_cds = fl_x_cds
		self.lista_specialita = []
		self.lista_risultati = []

	
	def __repr__(self):
		ret_string = "id: {}\ndescrizione: {}\nluogo: {}\ndata: {}\n".format(self.id,self.descr,self.luogo,self.data)
		ret_string += "SPECIALITA'\n"
		for specialita in self.lista_specialita:
			ret_string += "\t" + specialita.__repr__() + "\n"

		ret_string += "ISCRITTI/RISULTATI\n"
		for risultato in self.lista_risultati:
			ret_string += "\t" + risultato.__repr__() + "\n"
		return ret_string

	def aggiungi_iscritto(self,atleta,specialita):
		risultato = Risultato(atleta, specialita, self, None, None)
		self.lista_risultati.append(risultato)
	
	def lista_iscritti(self):
		return lista_risultati

	def aggiungi_specialità(self,specialita):
		self.lista_specialita.append(specialita)

	def aggiungi_risultato(self,atleta,specialita,prestazione,punteggio=None):
		for risultato in self.lista_risultati:
			# Cerco il risultato che mi serve
			if (risultato.atleta.id == atleta.id and risultato.specialita.id == specialita.id):
				# quando lo trovo aggiorno la lista ed interrompo la ricerca
				risultato.prestazione = prestazione
				risultato.punteggio = punteggio
				break
