from MaterialBibliografico import MaterialBibliografico as material

class Biblioteca():

    materiales_bibliograficos = set()

    def guardad(objeto):
        if isinstance(objeto, material):
            Biblioteca.materiales_bibliograficos.add(objeto)
            return Biblioteca.materiales_bibliograficos
        
        raise Exception(f"El objeto ingresado no pertenece a un material bibliografico")

    def imprimir(lista: set):
        for item in lista:
            print(item)
            print("-----------------------------")
 

