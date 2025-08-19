# Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().

# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
string1 = "Vamos a analizar esta función"
string2 = "Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n"
# EJECUCIÓN DEL CÓDIGO
list_string = string1.split()
list_string2 = string2.split()


def filter_strings_length(m, n=5):
    """Función que toma una lista de strings y devuelve las que son mayor o igual que n

    Args:
        m (list): lista de strings
        n (int, optional): numero entero que limita el número de letras de las palabras, por defecto = 5.

    Returns:
        str: devuelve la cadena que cumpla la condición dada
    """
    return len(m) >= n

print(list(filter(filter_strings_length,list_string)))
print(list(filter(filter_strings_length,list_string2)))