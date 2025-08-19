# Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().

# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
list1 = ["caseta", "árbol", "cine", "barrio", "ciudad", "puerta"]
# EJECUCIÓN DEL CÓDIGO
filter_list = list(filter(lambda i : i[0] == "c",list1))
print(filter_list)