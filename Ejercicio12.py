# Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().

# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
string1= "Tenemos que probar el nuevo programa"

# EJECUCIÓN DEL CÓDIGO
list_string = string1.split()
counter_string = list(map(lambda i: len(i),list_string)) 
print(counter_string)   