from instrumento import Instrumento
from abc import abstractclassmethod
class Sucursal():
    ID = 0
    def __init__(self):
        Sucursal.ID +=1
        self.__id = Sucursal.ID
        self.__nombre :str
        self.__lista_instrumentos = []

    @property
    def _nombre(self):
        return self.__nombre
    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value
    @property
    def _id(self):
        return self.__id
    def get_lista_instrumentos(self):
        return self.__lista_instrumentos

    def __repr__(self) -> str:
        return f'Sucursal : {self.__nombre}'
        
    """"
    Definimos los metodos para mostrar instrumentos, guardar y eliminar según un id
    En el metodo guardar_insrumento crea una variable llamada 'elemento_existente' donde se busca si hay algun objeto con id coicidentes. si los hay muestra un mensaje y de lo contrario lo guarda en la lista_instrumentos

    La función next()en Python se utiliza para obtener el siguiente elemento de un iterador. Un iterador es un objeto que implementa el protocolo de iteración, lo que significa que puede ser recorrido elemento por elemento.


    """
    def guardar_instrumento(self, instrumento : Instrumento):
        
        try:
            elemento_existente = next(filter(lambda inst: inst._id == instrumento._id, self.__lista_instrumentos))
            print(f'El {elemento_existente} con el id: {instrumento._id} ya se encuentra registrado')
        except StopIteration:
            self.__lista_instrumentos.append(instrumento)


    def mostrar_instrumentos(self):
        for instrumento in self.__lista_instrumentos:
            print(instrumento)
            print('-----------')

    """Filtramos por tipo, buscamos si hay elemento coicidentes con la funcion filter y los guardamos en una lista para luego imprimirlos"""
    
    def mostrar_por_tipo(self, tipo : str):
        lista = list(filter(lambda inst: inst._tipo == tipo, self.__lista_instrumentos))
        for instrumento in lista:
            print(instrumento)
        #return lista
    
    
    #utilizamos las mismas funciones nombradas anteriormente para buscar un instrumento por #id, y eliminarlo
    
    def borrar_instrumento(self, id : int):
        instrumento = next(filter(lambda inst: inst._id == id, self.__lista_instrumentos))
        if instrumento is None:
            print(f"El instrumento con el id: {id} no fue encontrado con exito")
            return
        self.__lista_instrumentos.remove(instrumento)
        print(f"El instrumento con id: {instrumento._id} de nombre: {instrumento._nombre} fue eliminado con exito")
