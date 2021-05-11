from typing import Sequence
from classes.atleta import Atleta

class Lista_Atleti:
	def __init__(self):
		self.lista_atleti:Sequence[Atleta] = []

	def __repr__(self):
		ret_string = ""
		for atleta in self.lista_atleti:
			ret_string += "descrizione: {}\tdata nascita: {}\n".format(atleta.descr,atleta.data_nascita.strftime("%d/%m/%Y"))
		return ret_string

	def aggiungi_atleta(self,atleta:Atleta) -> Atleta:
		self.lista_atleti.append(Atleta(**atleta))
		return atleta
	
	def get_atleti(self) -> Sequence[Atleta]:
		return self.lista_atleti
