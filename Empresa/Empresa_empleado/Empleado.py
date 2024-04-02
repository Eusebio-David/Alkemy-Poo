from datetime import datetime
from abc import ABC, abstractclassmethod, abstractmethod

class Empleado(ABC):

    def __init__(self, dni:str, apellido:str , fecha: str):
        #Validamos que el dni sea de 8 numeros
        assert len(dni)!=8, f"Error, no puede tener mas de 8 dígitos"
       
        self.__dni  = dni
        self.__apellido  = apellido
        self.__fecha_de_ingreso = fecha
        self.__antiguedad = self.obtener_antiguedad()
        

    @abstractmethod
    def obtener_salario(self):
        pass


   
    def get_dni(self):
        return self.__dni
    
    
    def set_dni(self, value):
        self.__dni = value
    
  
    def get_apellido(self):
        return self.__apellido
    
   
    def set_apellido(self, value):
        self.__apellido = value

    
    def get_fecha_de_ingreso(self):
        return self.__fecha_de_ingreso
    
    
    def set_fecha_de_ingreso(self, value):
        self.__fecha_de_ingreso = value
   
    def get_antiguedad(self):
        return self.__antiguedad
    

    def __repr__(self) -> str:
        return f"({self.__apellido} de DNI: {self.__dni} es: {self.__class__.__name__}, ingreso: {self.__fecha_de_ingreso}, y su antiguedad es: {self.__antiguedad})"
    
   
    def obtener_antiguedad(self):
        fecha = datetime.strptime(self.__fecha_de_ingreso, "%d/%m/%Y")#convierte un string a un objeto datetime
        fecha_actual= datetime.now()
        antiguedad = ((fecha_actual - fecha).days )/365
        return int(antiguedad)

    
    
    @staticmethod
    def corroborar_dni(num: str):
        pass