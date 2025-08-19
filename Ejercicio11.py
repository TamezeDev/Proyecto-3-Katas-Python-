# Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

# EJECUCIÓN DEL CÓDIGO
def age_checker():
    """Función para solicitar la edad el usuario. Si no está comprendido entre 0 y 120 se manejan los diversos errores

    Returns:
        int: devuelve un valor de tipo entero
    """
    while True:
        try:
            age_user = int(input('Intruduzca su edad: '))
            if 0 <= age_user <= 120:
                return age_user
            else:
                print('La debe esta comprendida entre 0 y 120')
        except ValueError:
            print('Error: Debe introducir un valor numérico')
            continue
        
print(f'Usted ha indicado que tiene {age_checker()} años')