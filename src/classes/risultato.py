from classes.specialita import Specialita
from classes.atleta import Atleta

class Risultato:
	def __init__(self,atleta,specialita,prestazione=None,punteggio=None):
		'''Se il dato mi arriva da db sono gli id, quindi sono degli interi
		 Se il dato è inserito manualmente sono degli oggetti'''
		self.atleta = Atleta(**atleta)
		self.specialita = Specialita(**specialita)
		self.prestazione = prestazione
		self.punteggio = punteggio

	def __repr__(self):
		return "{} {} {} {}".format(self.atleta.descr, self.specialita.descr, self.prestazione if self.prestazione else "", self.punteggio if self.punteggio else "")