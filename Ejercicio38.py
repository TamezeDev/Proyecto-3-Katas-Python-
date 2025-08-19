"""    Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.

        Reglas:
                0 - 69: insuficiente
                70 - 79: bien
                80 - 89: muy bien
                90 - 100: excelente
"""

# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
calificacion1= 67
calificacion2 = 83

# EJECUCIÓN DEL CÓDIGO
def comprobar_calificaciones(qualify):
    """Función para calificar la nota de un alumno segun lo que haya sacado

    Args:
        qualify (int): Recibe la nota del la calificación en int

    Returns:
        str: devuelve la categoría a la nota correspondiente
    """
    if 0 <= qualify > 70:
        return print('Insufuciente')
    elif 70 <= qualify >80:
        return print('Bien')
    elif 80 <= qualify > 90:
        return print('Muy bien')
    elif qualify <= 100:
        return print('Excelente')
    
comprobar_calificaciones(calificacion1)
comprobar_calificaciones(calificacion2)