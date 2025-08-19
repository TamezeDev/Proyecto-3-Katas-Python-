# Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.

import datetime
# EJECUCIÓN DEL CÓDIGO

def checker_timer():
    """Función para solicutar la hora a un usuario y dependiendo la hora te devuelve si es por la mañana,por la tarde o por la noche
        Notes: Maneja errores si la hora no está en los parámetros correctos
    """
    while True:
        try:
            user_hour = int(input('Indroduzca la hora para saber si es por la mañana, por la tarde o por la noche:\n'))
            while user_hour >= 24 or user_hour < 0:
                print('Debe un troducir un valor entre 0 y 23 para la hora ')
                user_hour = int(input('Indroduzca la hora para saber si es por la mañana, por la tarde o por la noche:\n'))
            user_minutes = int(input('Indroduzca los minutos para saber si es por la mañana, por la tarde o por la noche:\n'))
            while user_minutes < 0 or user_minutes > 59:
                print('Debe un troducir un valor entre 0 y 23 para la hora y entre 0 y 59 para los minutos')
                user_minutes = int(input('Indroduzca los minutos para saber si es por la mañana, por la tarde o por la noche:\n'))
            else:
                break
        except ValueError:
            print('Debe un troducir un valor entre 0 y 23 para la hora y entre 0 y 59 para los minutos')
    selected_time = datetime.time(user_hour,user_minutes)
    print((f'La hora seleccionada es: {selected_time}'))
    if 6 <= user_hour < 12:
        print('Es por la mañana')
    elif 12 <= user_hour < 22:
        print('Es por la tarde')
    elif 22 <= user_hour >= 23 or 0 <= user_hour < 6:
        print('Es por la noche') 

checker_timer()