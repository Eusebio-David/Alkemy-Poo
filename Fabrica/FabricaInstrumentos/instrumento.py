from tipoInstrumento import Tipo

class Instrumento():
    ID = 0
    def __init__(self) -> None:
        Instrumento.ID +=1
        self.__nombre : str
        self.__id : int = Instrumento.ID
        self.__precio : float
        self.__tipo = ''

    """
    En el ejemplo, hemos definido una clase llamada Instrumento con atributos especificos. El decorador @property se aplica al método o a los atributos, lo que permite acceder a la propiedad como si fuera un atributo en lugar de un método. El decorador ejemplo @_nombre.setter se aplica al método _nombre, lo que permite establecer el valor de la propiedad.
    basicamente al utilizar esos decoradores lo que hace es que los atributos se pueden llamar y modificar desde afuera sin la necesidad de llamar a un metodo en especial. 
    es de preferencia usarlos, yo en este caso quise probar como era su funcionamiento
    """

    @property
    def _nombre(self):
        return self.__nombre
    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _id (self):
        return self.__id


    @property
    def _precio(self):
        return self.__precio

    @_precio.setter
    def _precio(self, value):
        self.__precio  = value

    @property
    def _tipo(self):
        return self.__tipo

    @_tipo.setter
    def _tipo(self, value):
        self.__tipo = value


    """"
    La función __repr__ en Python es un método especial que se utiliza para representar objetos de una clase como una cadena de texto. Proporciona una representación legible de un objeto que puede ser utilizado para recrear el objeto si es necesario.


    Cuando define el método __repr__ en una clase, puede personalizar la representación de cadena de texto de los objetos de esa clase. Por lo general, se utiliza para proporcionar una representación detallada y precisa del objeto, que es útil para fines de depuración y desarrollo.
    """
    def __repr__(self) -> str:
        return f"Nombre del instrumento: {self.__nombre}\n"\
            f"Precio: {self.__precio}\n"\
            f"Tipo : {self.__tipo}"