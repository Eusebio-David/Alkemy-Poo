
class Empresa():

    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__empleados = []

    def agregar_empleado(self, empleado):
        lista = list(filter(lambda emp: emp.get_dni() == empleado.get_dni(), self.__empleados))
        if lista:  
            print(f"El empleado {lista[0].get_apellido()} con dni {lista[0].get_dni()} ya fue registrado")
            return 

        self.__empleados.append(empleado)

    def mostrar_empleados(self):

        for empleado in self.__empleados:
            print(empleado)
            

    def eliminar_empleado(self, empleado):
        for e in self.__empleados:
            if e.dni == empleado.get_dni():
                self.__empleados.remove(empleado)
                return 
        print(f"El empleado {empleado.get_apellido()} no se encuntra en la empresa")

