from MaterialBibliografico import MaterialBibliografico as material


class Libro(material):
    
    """Esta clase representa un libro. Donde tendra atributos heredados
    de material bibliografico y propios como puede ser su id"""
    ID_CONTADOR = 0

    def __init__(self): #CONSTRUCTOR SIN INICIALIZAR PARA PODER ASIGNAR VALORES CON SUS GET Y SET
        super().__init__()
        self.__isbn: str = None
        Libro.ID_CONTADOR +=1
        self.__id = Libro.ID_CONTADOR
        
    #CONTRUCTOR CON VALORES PARA INICIALIZAR CON DATOS YA PREDETERMINADO
    def __init__(self, titulo: str, autor: str, fecha: str, isbn:str): 
        super().crear_material(titulo, autor, fecha)
        self.__isbn = isbn
        Libro.ID_CONTADOR +=1
        self.__id = Libro.ID_CONTADOR



    def get_isbn(self)->str:
        return self.__isbn
    
    def set_isbn(self, isbn: str)->None:
        self.__isbn = isbn
    
   
   
    def __str__(self) -> str:
        info = f"isbn: {self.__isbn}\n"\
            f"Id: {self.__id}\n"\
            f"{super().__str__()}"
            
        return info
   