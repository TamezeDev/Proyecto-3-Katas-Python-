# Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.

# EJECUCIÓN DEL PROGRAMA
def div_user(times):
    """Función para capturar los numeros introducidos por el usuario y convertirlos a floats para poder operarlos posteriormente

    Args:
        times (str): indica cada número que le solicito al usuario

    Returns:
        float: convierte a float el input recogido

    Notes:
        -Si el usuario introduce cualquier valor no numérico continuará en bucle hasta conseguir uno
        -Si el segundo valor es igual a 0 se le solitará que lo cambie hasta que el valor sea distito a 0
    """
    while True:
        try:
            num = input(times)
            if  "," in num:
                num = num.replace(',','.')                
            num = float(num)
            return num
        except ValueError:
            print('Error: Para usar el programa debes introcir un número válido: ')
            continue
        
num1 = div_user('Introduce el primer número: ')
num2 = div_user('Introduce el segundo número: ')

while num2 == 0:
    print('Error: No se puede dividir entre 0')
    num2 = div_user('Introduce un número distinto de 0: ')

cociente = round(num1 / num2, 1)
print(f'El cociente de la divión del primer número entre el segundo es: {cociente}')