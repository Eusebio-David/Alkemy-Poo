from Empleado_fijo import EmpleadoFijo
from datetime import datetime
from Empleado_comision import EmpleadoComision
from Empresa import Empresa


empresa = Empresa("joshon")
empleado = EmpleadoFijo("403636085456","eusebio", "25/10/2000",300000)

empresa.agregar_empleado(empleado)


empleado_comision = EmpleadoComision("40363608546","eusebio", "25/10/2000",80000)
empleado_comision1 = EmpleadoComision("4036365456","perez", "25/10/2000",80000)
empleado_comision2 = EmpleadoComision("40363085456","rodriguez", "25/10/2000",80000)

empleado_comision.set_clientes_captados(3)
empleado_comision1.set_clientes_captados(5)
empleado_comision2.set_clientes_captados(2)

empresa.agregar_empleado(empleado_comision)
empresa.agregar_empleado(empleado_comision2)


print("Lista de empleados")
empresa.mostrar_empleados()