from Libro import Libro
from Revista import Revista
from dvd import DVD



class Biblioteca():
    BibliotecaItem = {}
    lista_libros = set()
    lista_revistas = set()
    listas_dvd = set()


    def crear_material_biliografico():
        libro = Libro()
        titulo = input("Ingrese titulo: ")
        existencia = Biblioteca.corroborar_existencia(Biblioteca.lista_libros,titulo)
        if existencia: 
            return print("Este título ya existe")
        
        libro.set_titulo(titulo)
        libro.set_autor(input("Ingrese autor: "))
        libro.set_fecha_publicacion(input("Ingrese fecha de publicación: "))
        libro.set_isbn(input("Ingrese isbn: "))

        return libro
  
    @staticmethod
    def guardar(objeto):
        if  isinstance(objeto, Libro):
            Biblioteca.lista_libros.add(objeto)
            Biblioteca.BibliotecaItem["libro"]=Biblioteca.lista_libros
            return "Libro guardado con exito"
        elif isinstance(objeto, Revista):
            Biblioteca.lista_revistas.add(objeto)
            Biblioteca.BibliotecaItem["revista"]=Biblioteca.lista_revistas
            return "Revista guardada con exito"
        elif isinstance(objeto, DVD):
            Biblioteca.lista_dvd.add(objeto)
            Biblioteca.BibliotecaItem["DVD"]=Biblioteca.lista_dvd
            return "DVD guardado con exito"
        

        return "Error No se encontro ningun objeto Libro, Revista o DVD" 

    @staticmethod
    def imprimir()->None:
        diccionario = Biblioteca.BibliotecaItem
        for item,value in diccionario.items():
            print(item)
            for objeto in value:
                print(objeto)
            print("-------")

    
    def buscar_seccion(seccion: str)->None:
        item = Biblioteca.BibliotecaItem[seccion]
        for obj in item:
            print(obj.__str__())
           

    
    def corroborar_existencia(lista, titulo: str, isbn=""):
        for item in lista:
            if item.get_titulo() == titulo:
                return True
        return False