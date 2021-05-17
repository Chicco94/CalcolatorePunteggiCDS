from tinydb import TinyDB, Query
from classes.lista_gare import Lista_Gare, Gara,Risultato,Specialita
from classes.lista_atleti import Lista_Atleti, Atleta

def stampa_punteggio_migliore(lista_gare:Lista_Gare,lista_atleti:Lista_Atleti):
	punteggio_migliore = lista_gare.get_best_mappa_specialita_risultati_di_atleti(lista_atleti)
	totale_punteggio = 0
	totale_gare = 0
	for specialita,risultato in punteggio_migliore.items():
		print("\n   ---   {}   ---".format(specialita))
		totale_gare += 1
		if (type(risultato) == list):
			for i,ris in enumerate(risultato):
				if (i == 3):
					print("{}".format(ris))
					totale_punteggio += ris.punteggio
				else:
					print("{0: <30}".format(ris.atleta.descr))
		else:
			print("{}".format(risultato))
			totale_punteggio += risultato.punteggio
	print("TOTALE GARE: {}/18\nTOTALE PUNTI: {}\nOBIETTIVO: 13406".format(totale_gare, totale_punteggio))


db = TinyDB('./db.json') 

# prendo gli atleti dal database
atleti = db.table('atleti')
lista_atleti = Lista_Atleti()
for atleta in atleti.all():
	lista_atleti.aggiungi_atleta(atleta)

# prendo le gare dal database
gare = db.table('gare')
lista_gare = Lista_Gare()
for gara in gare.all():
	lista_gare.aggiungi_gara(gara)

stampa_punteggio_migliore(lista_gare,lista_atleti)
