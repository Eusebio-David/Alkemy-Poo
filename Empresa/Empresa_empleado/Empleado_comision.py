from Empleado import Empleado
from abc import abstractmethod
class EmpleadoComision(Empleado):
    COMSION = 0.15
    lista_empleados = []

    def __init__(self, dni: str, apellido: str, fecha: str, salrio : float):
        super().__init__(dni, apellido, fecha)
        self.__clientes_captados: int = 0
        self.__salario_minimo: float = salrio
        self.__monto_Cliente : float = self.__salario_minimo * EmpleadoComision.COMSION
        

        EmpleadoComision.lista_empleados.append(self)

    def get_clientes_captados(self):
        return self.__clientes_captados
    
    def set_clientes_captados(self, value):
        self.__clientes_captados = value

    def get_salario_minimo(self):
        return self.__salario_minimo
    def set_salario_minimo(self, value):
        self.__salario_minimo = value

    #method
    
    def obtener_salario(self):
        salario = self.__clientes_captados * self.__monto_Cliente
        return salario + self.__salario_minimo


    @classmethod
    def empleado_con_mas_clientes(cls):
        # empleado_por_comision = [e for e in lista_epleados if isinstance(e, cls)]
        # empleado_con_mas_clientes = max(empleados_por_comision, key=lambda emp: emp.get_clientes_captados())
        lista_ordenada = sorted(EmpleadoComision.lista_empleados, key=lambda emp: emp.get_clientes_captados())

        empleado = lista_ordenada[-1]
        print(f"El Empleado con mas clientes es : {empleado} con {empleado.get_clientes_captados()} clientes captados.")
        

        



    