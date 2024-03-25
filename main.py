from Libro import Libro
#from BibliotecaItem import Biblioteca
from biblioteca import Biblioteca 
from Revista import Revista
from dvd import DVD as dvd



revista1 = Revista("Pasteleria", "Richard","23/08/2023","Patagonia","cocina")
libro = Libro("El poder", "Byrne", "04/01/2000","123456675")
dvd = dvd("Fuego sagrado", "Los espiritus", "05/01/2005", "Música", "2 horas","Mp3")

Biblioteca.guardad(revista1)
Biblioteca.guardad(libro)
Biblioteca.guardad(dvd)

Biblioteca.imprimir(Biblioteca.materiales_bibliograficos)








