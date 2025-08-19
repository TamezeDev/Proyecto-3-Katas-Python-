# Crea una función lambda que sume 3 a cada número de una lista dada.

# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
list1 = [0,3,6,9,12,15,18]

# EJECUCIÓN DEL CÓDIGO
sum_list = list(map(lambda i: i + 3, list1))
print(sum_list)