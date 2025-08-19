# Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

from functools import reduce
# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
list1 = [1,2,3,4,5,6,7,8,9]
list2 = []
list3 = [10,10,10,10,10,10]
# EJECUCIÓN DEL CÓDIGO
def make_media(nums):
    """Función que hace la media de una de una lista e informa si la lista está vacía manejando el error

    Args:
        nums (list): Lista que recibe para hacer el promedio

    Returns:
        float: devuelve el resultado calculado 
    """
    try:
        suma = round(reduce(lambda x,y: x + y, nums),2)
        return print(f'El promedio de la lista es: {suma / len(nums)}')
    except TypeError:
        print('Error: La lista introducidad está vacía')
make_media(list1)
make_media(list2)
make_media(list3)