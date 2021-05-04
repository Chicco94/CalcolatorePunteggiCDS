from classes.atleta import Atleta
from tinydb import TinyDB, Query
from classes.lista_gare import Lista_Gare, Gara,Risultato,Specialita

db = TinyDB('./db.json') 
atleti = db.table('atleti')
for atleta in atleti.all():
	Atleta(**atleta)

gare = db.table('gare')
lista_gare = Lista_Gare()
for gara in gare.all():
	lista_gare.aggiungi_gara(Gara(**gara))

print(lista_gare)