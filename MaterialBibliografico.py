
class MaterialBibliografico():
   
    def __init__(self):
       
        self.__titulo : str = None
        self.__autor: str = None
        self.__fechaPublicacion: str = None
        
    def crear_material(self, titulo: str, autor: str, fecha: str):
        self.__titulo = titulo
        self.__autor = autor
        self.__fechaPublicacion = fecha
    
    
    
    
    def get_titulo(self)->str:
        return self.__titulo

    def set_titulo(self, titulo:str)->None:
        self.__titulo = titulo
    
    def get_autor(self)->str:
        return self.__autor
    def set_autor(self, autor:str)->None:
        self.__autor = autor
    
    
    def get_fecha_publicacion(self)->str:
        return self.__fechaPublicacion
    def set_fecha_publicacion(self, fecha:str)->None:
        self.__fechaPublicacion = fecha
    

    def __str__(self) -> str:
        info = f"Título: {self.__titulo}\n"\
            f"Autor: {self.__autor}\n"\
            f"Fecha publicación: {self.__fechaPublicacion}"\
        
        return info

    