# Crea una función lambda que sume elementos correspondientes de dos listas dadas.

# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
list1 = [2,4,6,8,10]
list2 = [1,3,5,7,11] 
list3 = ["la","el", "un","una"]
list4 = ["casa","coche","vaso","silla"]

# EJECUCIÓN DEL CÓDIGO
join_lists = list(map(lambda i: i[0] + i[1], zip(list1,list2)))
join_lists2 = list(map(lambda i: i[0]  + " " + i[1], zip(list3,list4)))

print(join_lists)
print(join_lists2)