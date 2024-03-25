from MaterialBibliografico import MaterialBibliografico as material

class Revista(material):
    ID_CONTADOR = 0


    def __init__(self): #CONSTRUCTOR VACÍO
        super().__init__()
        Revista.ID_CONTADOR +=1
        self.__id = Revista.ID_CONTADOR
        self.__editorial: str = None
        self.__articulos: str = None

    #CONSTRUCTOR CON DATOS PASADOS COMO ARGUMENTOS
    def __init__(self, titulo: str, autor: str, fecha: str, editorial: str, articulos: str):
        super().crear_material(titulo, autor, fecha)
        self.__editorial = editorial
        self.__articulos = articulos
        Revista.ID_CONTADOR +=1
        self.__id = Revista.ID_CONTADOR
        

        



    def get_editorial(self)->str:
        return self.__editorial
    def set_editorial(self, editorial: str):
        self.__editorial = editorial
        pass

    def get_articulos(self)->str:
        return self.__articulos
    def set_articulos(self, articulos:str)->None:
        self.__articulos = articulos


    def __str__(self)->str:
        info = f"Id: {self.__id}\n"\
            f"Artículos: {self.__articulos}\n"\
            f"Editorial: {self.__editorial}\n"\
            f"{super().__str__()}"

        return info