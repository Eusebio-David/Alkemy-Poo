from sucursal import Sucursal

class Fabrica():
    """
        creamos una clase fábrica donde tiene como atributo un nombre y una lista de sucursales
        luego agregamos un método para agregar una sucursal, para mostrarlas y para mostrar los instrumentos y de que tipo hay en cada sucursal, con el porcentaje que representaría, faltaría agregar algún método para eliminar y actualizar
    """
    def __init__(self, nombre):
        self.__nombre : str = nombre
        self.__sucursales = []

    def agregar_sucursal(self, sucursal):
        elemento_existente = list(
            filter(lambda suc: suc._id == sucursal._id, self.__sucursales))
        if elemento_existente:
            print(f'la sucursal con el id: {sucursal._id} ya se encuentra registrado')
            return 
        self.__sucursales.append(sucursal)


    """
    En este método guardamos en una variable llamada lista_instrumentos la lista de instrumentos que tiene cada sucursal.
    creamos un diccionario vácio, recorremos con un for la lista anteriormente creada
    y agregamos al diccionario una clave que se va a llamar según el tipo de instrumento con un valor, que representa la cantidad, este caso usamos la funcion get que comprueba si no hay valores anteriormente agregados le asigna 0 y si ya tiene un valor le suma 1, simulando un contador.

    Para saber el porcentaje de cada uno, creamos un diccionario llamado 
    updated_diccionario, recorremos el diccionario anteriormente creado y le agregamos como clave el nombre porcentaje + el tipo, con un valor calculado que seria la cantidad o el valor dividio el total que es el tamaño de la lista_instrumento de cada sucursal, lo multiplicamos por 100 y lo casteamos a int para obtener un entero. 
    Actualizamos el diccionario_instrumentos con la funcion update() pasandole el diccionario updated_diccionario como parametro o argumento.

    """
    def cantidad_por_tipo(self, sucursal):
        lista_instrumentos = sucursal.get_lista_instrumentos()
        total = len(lista_instrumentos)
        diccionario_instrumentos = {}

        for key in lista_instrumentos:
           diccionario_instrumentos[key._tipo]=diccionario_instrumentos.get(key._tipo, 0) + 1

        updated_diccionario = {}
        for item, value in diccionario_instrumentos.items():
            porc = int(value / total * 100)
            updated_diccionario[f'porcentaje:{item}'] = f'{porc}%'
        
        diccionario_instrumentos.update(updated_diccionario)
        return diccionario_instrumentos
    

    #Mostramos las sucursales y el diccionario con la cantidad y el porcentaje
    def mostrar_sucursales(self):
        for sucursal in self.__sucursales:
            print(sucursal)
            print(f'{self.cantidad_por_tipo(sucursal)}\n')


    