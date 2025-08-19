# Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().

# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
lista_mascotas = ["Perro", "Gato", "Tigre", "Hamster", "Oso", "Loro", "Ardilla"]
lista_mascotas_excluidas =  ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
# EJECUCIÓN DEL CÓDIGO
lista_mascotas_filtradas = list(filter(lambda i: not i in lista_mascotas_excluidas, lista_mascotas))
print(f'La lista sin las mascotas exluidas es {lista_mascotas_filtradas}')