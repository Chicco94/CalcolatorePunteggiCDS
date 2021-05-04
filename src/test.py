from classes.atleta import Atleta
from classes.lista_gare import Lista_Gare, Gara,Risultato,Specialita

io = Atleta("ED000118", "Enrico Cominato","07/02/1994","M")
chiara = Atleta("ED000118", "Chiara Arcidiacono","04/04/2007","F")


gara = Gara(1, "Primo meeting", "04/05/2021", "Vicenza")

lista_gare = Lista_Gare()
gara1 = lista_gare.aggiungi_gara(gara)
gara2 = lista_gare.aggiungi_gara(2, "Secondo meeting", "05/05/2021", "Padova")

m100 = Specialita(1, "100 metri", "SM")
m200 = Specialita(2, "200 metri", "SM")
m400 = Specialita(3, "400 metri", "SM")
m800 = Specialita(4, "800 metri", "SM")
m1500 = Specialita(5, "1500 metri", "SM")
gara1.aggiungi_specialità(m100)
gara1.aggiungi_specialità(m200)
gara1.aggiungi_specialità(m400)
gara1.aggiungi_specialità(m800)
gara1.aggiungi_specialità(m1500)
gara2.aggiungi_specialità(m100)
gara2.aggiungi_specialità(m200)
gara2.aggiungi_specialità(m400)
gara2.aggiungi_specialità(m800)
gara2.aggiungi_specialità(m1500)


gara1.aggiungi_iscritto(io, m100)
gara1.aggiungi_iscritto(io, m200)
gara1.aggiungi_iscritto(io, m400)
gara2.aggiungi_iscritto(io, m100)
gara2.aggiungi_iscritto(io, m200)
gara2.aggiungi_iscritto(io, m400)


gara1.aggiungi_risultato(io, m100,'13.10',150)
gara1.aggiungi_risultato(io, m200,'27.5',200)
gara2.aggiungi_risultato(io, m400,'60',200)

print(lista_gare)