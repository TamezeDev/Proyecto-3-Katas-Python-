# Crea una función que calcule el promedio de una lista de números.

# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
list1 = (10,20,30,40,50,60)
list2 = (12.4,14.6,18.9)
# EJECUCIÓN DEL CÓDIGO
def media_calculate(x):
    """Función que calcula el promedio de una lista de números

    Args:
        x (list): lista de numeros 

    Returns:
        float: media aritmética redondeada a 1 cifra de la lista dada
    """
    total_sum = 0
    for i in x:
        total_sum += i
    return round(total_sum / len(x),1)

print(media_calculate(list1))
print(media_calculate(list2))