# Concatena una lista de palabras. Usa la función reduce().

from functools import reduce
# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
list1 = ["Estamos","haciendo", "el", "ejercicio", "usando", "la", "función", "reduce"]
# EJECUCIÓN DEL CÓDIGO
new_phrase = reduce(lambda a,b: a + " " + b, list1)
print(new_phrase)