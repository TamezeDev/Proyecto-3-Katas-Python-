# Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.

# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
list1 = [2.6,6.4,7.4,4.6,7]
list2 = [4.3,5.5,4.7,3,6.9]
# EJECUCIÓN DEL CÓDIGO
def pass_checker(list,passed = 5):
    """Función para comprobar si un alumno está aprobado al final de curso

    Args:
        list (lista): lista de números tipos int o float
        passed (int/float): valor mínimo para un aprobar, por defecto 5

    Returns:
        tuple: devuelve una tupla con el estado del alumno y su nota media
    """
    status = []
    media = sum(list) / len(list)
    if media >= passed:
        status.append('Aprobado')
        status.append(media)
    elif passed > media > 4.5:
        status.append('Casi apruebas')
        status.append(media)
    else:
        status.append('Suspendido')
        status.append(media)
    return tuple(status)

print(pass_checker(list1))
print(pass_checker(list2))

