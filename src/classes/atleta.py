from datetime import datetime

class Atleta:
	def __init__(self,id:str,descr:str,data_nascita:str,sesso:str):
		'''id: identificativo fidal
			descr: nome e cognome
			data nascita nel formato: gg/mm/aaaa
			sesso: 'M' oppure 'F'
		'''
		self.id = id
		self.descr = descr
		self.data_nascita = datetime. strptime(data_nascita, '%d/%m/%Y')
		self.sesso = sesso
		self.totale_gare = 0
		self.totale_staffette = 0

	def categoria(self) -> str:
		''' Ritorna la categoria dell\'atleta basandosi sulla data di nascita ed il sesso'''
		anno_nascita = self.data_nascita.year
		anno_attuale = datetime.now().year
		if (12 <= (anno_attuale - anno_nascita) <= 13):
			return "R"+self.sesso
		if (14 <= (anno_attuale - anno_nascita) <= 15):
			return "C"+self.sesso
		if (16 <= (anno_attuale - anno_nascita) <= 17):
			return "A"+self.sesso
		if (18 <= (anno_attuale - anno_nascita) <= 19):
			return "J"+self.sesso
		if (20 <= (anno_attuale - anno_nascita) <= 22):
			return "P"+self.sesso
		if (23 <= (anno_attuale - anno_nascita) <= 34):
			return "S"+self.sesso
		if (34 <= (anno_attuale - anno_nascita) <= 39):
			return "S"+self.sesso+"35"
		if (40 <= (anno_attuale - anno_nascita) <= 44):
			return "S"+self.sesso+"40"
		if (45 <= (anno_attuale - anno_nascita) <= 49):
			return "S"+self.sesso+"45"
		if (50 <= (anno_attuale - anno_nascita) <= 54):
			return "S"+self.sesso+"50"
		if (55 <= (anno_attuale - anno_nascita) <= 59):
			return "S"+self.sesso+"55"
		if (60 <= (anno_attuale - anno_nascita) <= 65):
			return "S"+self.sesso+"60"
		return None