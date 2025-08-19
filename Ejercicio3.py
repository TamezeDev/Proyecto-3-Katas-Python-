# Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
list1 = ['La casa', 'el gato', 'el perro', 'casa de Pedro', 'el bosque', 'casa en el pueblo']
# EJECUCIÓN DEL CÓDIGO
def word_search(list, object = "casa"):
    """Función para buscar si un elemento contiene la palabra objetivo

    Args:
        list [lista]: lista con elementos de cualquiere tipo
        object (int, float, string...): dependiendo lo que queramos buscar
    """
    filter_list = []
    for i in list:
        if object in i:
            filter_list.append(i)
        else:
            pass
    print(f'Los elementos que contienen la palabra objetivo son: {filter_list}')

word_search(list1)
word_search(list1, "el")