from Empleado import Empleado
from datetime import datetime
from abc import abstractmethod

class EmpleadoFijo(Empleado):
   

    def __init__(self, dni: str, apellido: str, fecha: str, sueldo_basico: float):
        super().__init__(dni, apellido, fecha)
        assert sueldo_basico>0, f"El sueldo básico para un empleado tiene que ser mayor a 0."
        self.__sueldo_base = sueldo_basico
        
        
       
        

    @property
    def sueldo_base(self):
        return self.__sueldo_base
    @sueldo_base.setter
    def sueldo_base(self, value):
        self.__sueldo_base = value

    def get_antiguedad(self):
        return super().get_antiguedad()
    



    
    def obtener_salario(self):
       porcentaje = self.porcentajes_por_antiguedad(self.get_antiguedad())
       return self.__sueldo_base + porcentaje

    
    #obtenemos el porcentaje de salario segun su antiguedad
    def porcentajes_por_antiguedad(self, antiguedad):
        if antiguedad<2 :
            return 0
        
        if 2 <= antiguedad <=5:
            return self.__sueldo_base*0.05
        
        if antiguedad>5:
            return self.__sueldo_base*0.1
      
    
    
    
