from classes.atleta import Atleta
from classes.specialita import Specialita
from classes.gara import Gara

test = Atleta("ED000118", "Enrico Cominato","07/02/1994","M")
print(test.categoria())
test = Atleta("ED000118", "Chiara Arcidiacono","04/04/2007","F")
print(test.categoria())

gara = Gara(1, "Primo meeting", "04/05/2021", "Vicenza")

gara.aggiungi_specialità(Specialita(1, "100 metri", "SM"))
gara.aggiungi_specialità(Specialita(2, "200 metri", "SM"))
gara.aggiungi_specialità(Specialita(3, "400 metri", "SM"))
gara.aggiungi_specialità(Specialita(4, "800 metri", "SM"))
gara.aggiungi_specialità(Specialita(5, "1500 metri", "SM"))
print(gara)