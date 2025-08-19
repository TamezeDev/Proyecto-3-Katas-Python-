# Crea una función lambda que filtre los números impares de una lista dada.

# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
list1 = [0,1,2,3,4,5,6,7,8,9,10]

# EJECUCIÓN DEL CÓDIGO
even_list = list(filter(lambda x: x  % 2  != 0, list1))
print(even_list)