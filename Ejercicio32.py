# Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
empleados = [{
    'Nombre': 'Javier Gómez',
    'Edad':  28,
    'Posición': 'Gerente'
},{
    'Nombre': 'José Luarte',
    'Edad':  33,
    'Posición': 'Operario'
},{
    'Nombre': 'Carmen Ruiz',
    'Edad':  30,
    'Posición': 'Responsable de planta'
},{
    'Nombre': 'Paco Bueno',
    'Edad':  41,
    'Posición': 'Administrativo'
},{
    'Nombre': 'Iván Molina',
    'Edad':  38,
    'Posición': 'Mantenimiento'
}]

# EJECUCIÓN DEL CÓDIGO
def searcher_position(company,name):
    """Función que recoje una lista de trajadores de una empresa y un nombre en particular. Evalúa si esa persona trabaja en la empresa y devuelve su posición laboral en caso que esté en plantilla
       De lo contrario lanza un mensaje que indicando que no trabaja allí

    Args:
        company (list): lista  compuesta de diccionarios con los empleados
        name (str): Nombre del empleado a buscar

    Returns:
        print: devuelve la posición si trabaja o aviso de que no
    """
    for e in company:
        if name == e['Nombre']:
            return print(f'{e['Nombre']} trabaja en la posición de: {e['Posición']}')  
        else:
            continue    
    return{print(f'{name} no trabaja en esta empresa')}   

searcher_position(empleados, "Paco Bueno")
searcher_position(empleados, "Carmen Ruiz")
searcher_position(empleados, "Pedro Navarro")