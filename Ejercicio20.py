# Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().

# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
list1 = ["manzana",22,"fresas", 10,45, "sandia"]

# EJECUCIÓN DEL CÓDIGO
filter_list = list(filter(lambda i: type(i) == int,list1))
print(filter_list)