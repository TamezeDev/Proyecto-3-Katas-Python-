# Calcula la diferencia total en los valores de una lista. Usa la función reduce().

from functools import reduce
# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
list1 = [90,5,8,7,6,21]

# EJECUCIÓN DEL CÓDIGO
total_difference = reduce(lambda x,y: x-y, list1)
print(total_difference)