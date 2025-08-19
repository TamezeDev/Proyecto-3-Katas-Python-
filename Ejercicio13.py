# Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().

# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
list_characters = "learning python"

# EJECUCIÓN DEL CÓDIGO
def strings_transform(x):
    """Función para transformar caracteres no consecutivos en mayuscula

    Args:
        x (string): cadena de caracteres aleatoria

    Returns:
        list: devuelve una lista con la transformación de cada letra
    """
    update_list = []
    if x == " ":
        pass
    elif list_characters.index(x) % 2 == 0:
        update_list.append(x.upper())
    else:
        update_list.append(x.lower())
    return update_list

tuple_string = tuple(map(strings_transform, list_characters))
print(tuple_string)