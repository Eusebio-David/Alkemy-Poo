from MaterialBibliografico import MaterialBibliografico as material

class DVD(material):
    ID_CONTADOR = 0
    
    def __init__(self): #CONSTRUCTOR VACÍO
        super.__init__()
        DVD.ID_CONTADOR +=1
        self.__id = DVD.ID_CONTADOR
        self.__contenido: str = None
        self.__duracion: str = None
        self.__formato : str = None

    #CONSTRUCTOR CON DATOS PASADOS COMO ARGUMENTOS
    def __init__(self, titulo:str, autor: str, fecha: str, contenido: str, duracion: str, formato: str):
        super().crear_material(titulo, autor, fecha)
        self.__contenido = contenido
        self.__duracion = duracion
        self.__formato = formato
        DVD.ID_CONTADOR +=1
        self.__id = DVD.ID_CONTADOR

   
        
    
    def set_contenido(self, contenido : str)->None:
        self.__contenido = contenido
    def  get_contenido(self)->str:
        return self.__contenido
    
    def set_duracion(self, duracion: str)->None:
        self.__duracion = duracion
    def get_duracion(self)->str:
        return self.__duracion
    
    def set_formato(self, formato: str)->None:
        self.__formato = formato
    def get_formato(self):
        return self.__formato
    
    def __str__(self) -> str:
        info = f"Id: {self.__id}\n"\
        f"Contenido: {self.get_contenido()}\n"\
        f"Duración: {self.get_duracion()}\n"\
        f"Formato: {self.get_formato()}\n"\
        f"{super().__str__()}\n"

        return info
