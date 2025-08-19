# Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
string1 = 'Crea una función que busque y devuelva el primer elemento duplicado en una lista dada'
string2 = 'Implementar el método quitar rama para eliminar una rama en una posición específica.'
string3 = 'Crea una función lambda que calcule el resto de la división entre dos números dados'
# EJECUCIÓN DEL CÓDIGO
def get_first_repeat_element(x):
    """Función para indicar la primera palabra que se repite en una cadena de texto

    Args:
        x (str): texto en el que queremos encontrar la primera palabra repetida

    Returns:
        str: string con la palabra repetida
    """
    list1 = x.split()
    save_word = set()
    for i in list1:
       if i in save_word:
            return print(f' La primera palabra repetida es {i}')
       else:              
        save_word.add(i)       
    return print('No se ha encontrado nunguna palabra repetida')


get_first_repeat_element(string1)
get_first_repeat_element(string2)
get_first_repeat_element(string3)

