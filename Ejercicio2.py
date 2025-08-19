# Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().

# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
list1 = [2,4,6,8,10,12,14,16,18,20]

# EJECUCIÓN DEL CÓDIGO
list_double = list(map(lambda i: i*2, list1))  #modo1
list_double2 = [element *2 for element in list1] #modo2

print(list_double)
print(list_double2)