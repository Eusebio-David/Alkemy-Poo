from sucursal import Sucursal
from instrumento import Instrumento
from tipoInstrumento import Tipo
from fabrica import Fabrica
sucursal_A = Sucursal()
sucursal_A._nombre = 'Sucursal Avenida Livertador'

instrumento1 = Instrumento()

instrumento1._nombre = 'Guitarra'
instrumento1._tipo = Tipo.CUERDA.value
instrumento1._precio = 35000

instrumento2 = Instrumento()

instrumento2._nombre = 'Violin'
instrumento2._tipo = Tipo.CUERDA.value
instrumento2._precio = 35000


instrumento3 = Instrumento()

instrumento3._nombre = 'Flauta'
instrumento3._tipo = Tipo.VIENTO.value
instrumento3._precio = 35000

sucursal_A.guardar_instrumento(instrumento1)
sucursal_A.guardar_instrumento(instrumento1)
sucursal_A.guardar_instrumento(instrumento2)
sucursal_A.guardar_instrumento(instrumento3)

sucursal_B = Sucursal()
sucursal_B._nombre = 'Sucursal Los pericos'
sucursal_B.guardar_instrumento(instrumento1)
sucursal_B.guardar_instrumento(instrumento2)
sucursal_B.guardar_instrumento(instrumento3)


fabrica = Fabrica("luttier")
fabrica.agregar_sucursal(sucursal_A)
fabrica.agregar_sucursal(sucursal_B)
fabrica.mostrar_sucursales()

sucursal_B.mostrar_instrumentos()



