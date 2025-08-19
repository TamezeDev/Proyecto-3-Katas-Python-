# Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().

from functools import reduce
# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
list1 = [2,3,4]
list2 = [5,7,2]

# EJECUCIÓN DEL CÓDIGO
print(reduce(lambda a,b: str(a) + str(b),list1))
print(reduce(lambda a,b: str(a) + str(b),list2))