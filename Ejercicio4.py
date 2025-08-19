# Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().

# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
list1 = [2,4,6,8,10,12,14]
list2 = [1,3,5,7,9,11,13]
# EJECUCIÓN DEL CÓDIGO
def sum_nums(x,y): 
    """Función para calcular la diferencia entre dos listas numéricas

    Args:
        x,y [lista]: lista con elementos de tipo int o float
         
    """
    return x - y

difference = sum(map(sum_nums,list1,list2))
print(difference)
