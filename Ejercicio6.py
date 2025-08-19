# Escribe una función que calcule el factorial de un número de manera recursiva.

# EJECUCIÓN DEL CÓDIGO
def fact_calculate(num):
    """Función que calcula el fatorial de cualquier número entero

    Args:
        num (int): valor de tipo integer

    Returns:
        int: devuelve el factorial del numero de tipo integer
    """
    counter = 1
    while num > 0:
        counter *= num
        num -= 1
    return counter
def get_user_num():
    """Función para solicitar al usuario el número que quiere introducir. Se maneja el error en caso que introduzca cualquier cosa que no sea un número entero
    """
    try:
        save_num = int(input('Elige un número entero para calcular su factorial: '))
        print(f'El factorial de {save_num} es {fact_calculate(save_num)}')
    except ValueError:
        print('El número entrducido no es de tipo entero')
        get_user_num()

get_user_num()