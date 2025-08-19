# Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.

# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
student1 = {
    'nombre': "Luis",
    'edad': 25,
    'calificación': 120
}
student2 = {
    'nombre': "Pedro",
    'edad': 23,
    'calificación': 80
}
student3 = {
    'nombre': "Sara",
    'edad': 20,
    'calificación': 110
}
student4 = {
    'nombre': "Antonio",
    'edad': 30,
    'calificación': 80
}

# EJECUCIÓN DEL CÓDIGO
filter_list = []
filter_list.extend([student1,student2,student3,student4])


new_list = list(filter(lambda i: i['calificación'] >= 90, filter_list))
print(new_list)