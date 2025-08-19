# Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
string1 = "Estoy haciendo los ejercicios de python"
string2 = "Esto es una verificacion de la funcion para contar caracteres"
# EJECUCIÓN DEL CÓDIGO
def characters_counter(list):
    """Función para contar el número de veces que se repiten los caracteres

    Args:
        list (strings): cadena de caracteres
    """
    dict_characters = {}
    for element in list:
        if element == ' ':
            continue
        elif element  not in dict_characters:
            dict_characters.update({element:1})
        elif element in dict_characters:
            dict_characters[element]  += 1
        else:
            pass
    print(dict_characters.items())


characters_counter(string1)
characters_counter(string2)




