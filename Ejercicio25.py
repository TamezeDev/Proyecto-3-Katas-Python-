# Crea una función que cuente el número de caracteres en una cadena de texto dada.

# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
string1 = "Tenemos que contar la cantidad de caracteres de esta cadena"
# EJECUCIÓN DEL CÓDIGO
def counter_strings(x):
    """Función para contar caracteres de una cadena

    Args:
        x (str): palabra, frase ---> cadena de caracteres a contar

    Returns:
        int: devuelve el valor numérico de los caracteres que la contienen
    """
    counter = 0
    for i in x:
        counter += len(i)
    return counter
print(counter_strings(string1))
