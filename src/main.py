from tinydb import TinyDB, Query
from classes.lista_gare import Lista_Gare, Gara,Risultato,Specialita
from classes.lista_atleti import Lista_Atleti, Atleta

db = TinyDB('./db.json') 
atleti = db.table('atleti')
lista_atleti = Lista_Atleti()
for atleta in atleti.all():
	lista_atleti.aggiungi_atleta(atleta)

gare = db.table('gare')
lista_gare = Lista_Gare()
for gara in gare.all():
	lista_gare.aggiungi_gara(gara)

print(lista_gare)