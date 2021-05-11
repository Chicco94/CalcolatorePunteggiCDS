from typing import Sequence
from classes.atleta import Atleta

class Lista_Atleti:
	def __init__(self):
		self.lista_atleti:Sequence[Atleta] = []

	def __repr__(self):
		ret_string = ""
		for atleta in self.lista_atleti:
			ret_string += "descrizione: {}\tdata nascita: {}\ttot gare: {}\tpieno: {}\n".format(atleta.descr,atleta.data_nascita.strftime("%d/%m/%Y"),atleta.totale_gare+atleta.totale_staffette,atleta.pieno())
		return ret_string

	def aggiungi_atleta(self,atleta:Atleta) -> Atleta:
		self.lista_atleti.append(Atleta(**atleta))
		return atleta
	
	def get_atleti(self) -> Sequence[Atleta]:
		return self.lista_atleti

	def get_atleta_by_id(self,idatleta:str) -> Atleta:
		for a in self.lista_atleti:
			if (a.id == idatleta):
				return a
		return None

	def add_gara_to_atleta(self,atleta:Atleta) -> Atleta:
		for a in self.lista_atleti:
			if (a.id == atleta.id):
				a.totale_gare += 1
				return a
		return None

	def add_staffetta_to_atleta(self,atleta:Atleta) -> Atleta:
		for a in self.lista_atleti:
			if (a.id == atleta.id):
				a.totale_staffette += 1
				return a
		return None

