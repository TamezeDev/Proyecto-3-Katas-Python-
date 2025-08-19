# Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).

# EJECUCIÓN DEL CÓDIGO
def calcular_area(figura, datos):
    """Función para calcular el área de un círculo, rectángulo o triángulo. Si no es uno de estos lanza un mensaje de error

    Args:
        figura (str): figura que queremos calcular el área
        datos (tuple): tupla con los datos necesarios para cada cálculo

    Returns:
        print: devuelve mensaje con el cálculo realizado
    """
    if figura == 'círculo':
        if len(datos) == 1:
            return print(f'El área del rectángulo es  {(datos[0]**2)*3.14}')
        else:
            print('Necesito un dato con la medida del radio para calcular el area del círculo')
    elif figura == "rectángulo":
        if len(datos) == 2:
            return print(f'El area del rectángulo es  {datos[0]*datos[1]}')
        else:
            print('Necesito dos datos con las medidas de los lados mayor y menor para calcular el area del rectángulo')
    elif figura == 'triángulo':
        if len(datos) == 2:
            return print(f'El área del triángulo es {(datos[0]*datos[1])/2}')
        else:
            print('Necesito dos datos con las medidas de la base y la altura para calcular el area del triángulo')
    else:
        print('Error: solo puedo calcular el area del triángulo, rectángulo o círculo')


calcular_area("cuadrado",1)
calcular_area("rectángulo", (2,4))
calcular_area("círculo", (2,))
calcular_area("triángulo", (10,8))
calcular_area("triángulo", (10,))