from classes.specialita import Specialita

class Risultato:
	def __init__(self,atleta,specialita,gara,prestazione=None,punteggio=None):
		'''Se il dato mi arriva da db sono gli id, quindi sono degli interi
		 Se il dato è inserito manualmente sono degli oggetti'''
		self.atleta = atleta
		self.specialita = specialita
		self.gara = gara
		self.prestazione = prestazione
		self.punteggio = punteggio

	def __repr__(self):
		return "{} {} {} {}".format(self.atleta.descr, self.specialita.descr, self.prestazione if self.prestazione else "", self.punteggio if self.punteggio else "")