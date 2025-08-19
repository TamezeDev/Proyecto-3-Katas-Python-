# Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().

# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
tupla1 = ('verde',23,88.4,'rojo')
# EJECUCIÓN DEL CÓDIGO
strings = list(map(str, tupla1))
print(strings)