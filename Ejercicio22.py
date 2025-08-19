# Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().

from functools import reduce
# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
list1 = [1,2,3,4,5,6]

# EJECUCIÓN DEL CÓDIGO
total = reduce(lambda x,y: x*y, list1)
print(total)