from classes.specialita import Specialita
from classes.atleta import Atleta

class Risultato:
	def __init__(self,atleta:Atleta,specialita:Specialita,prestazione:str=None,punteggio:int=None):
		'''Se il dato mi arriva da db sono gli id, quindi sono degli interi
		 Se il dato è inserito manualmente sono degli oggetti'''
		self.atleta:Atleta = Atleta(**atleta)
		self.specialita:Specialita = Specialita(**specialita)
		self.prestazione:str = prestazione
		self.punteggio:int = punteggio

	def __repr__(self):
		return "{} {} {} {}".format(self.atleta.descr, self.specialita.descr, self.prestazione if self.prestazione else "", self.punteggio if self.punteggio else "")