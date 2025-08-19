"""Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe:
    a. Solicitar al usuario el precio original de un artículo.
    b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
    c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
    d. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido (mayor a cero).
    e. Mostrar el precio final de la compra, considerando o no el descuento.
    f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones.
"""

# EJECUCIÓN DEL CÓDIGO
def get_price_article():
    """Función para solicitar el precio de un artículo al usuario manejando los errores posibles

    Returns:
        float: devuelve el valor decimal que introduce el usuario
    """
    while True:
        try:
            while True:
                real = float(input('Introduce el precio del articulo: '))
                if real <= 0:
                    print('El artículo tiene que tener un valor mayor a 0')
                else:
                    return real
        except ValueError:
            print('Debe introducir un valor numérico')

def get_discount_price(original):
    """Función para preguntar y solicitar el valor de un cupón de descuento en caso  de tenerlo

    Args:
        original (float): precio del artículo original anteriormente solicitado

    Returns:
        float/ str: devuelve valor en caso de ser válido el cupón o cadena = "no" en caso de no tenerlo
    """
    while True:
        answer_dicount = input('¿Tiene un cupón de descuento? --->  (si/no)\n')
        if answer_dicount == "si":
            while True:
                try:
                    discount_value = float(input('¿De cuanto es el cupón de descuento?\n '))
                    if discount_value <= 0:
                        print('El descuento no puede ser 0 o inferior')
                    elif discount_value > original:
                        print('El descuento no puede ser superior al precio original')
                    else:
                        return discount_value
                except ValueError:
                    print('El descuento tiene que tener un valor numérico')
        if answer_dicount == "no":
            return answer_dicount
        else:
            print('La respuesta tiene que ser si o no')

def make_discount(original, discount):
    """Función que hace el cálculo del precio del producto original menos el descuento.

    Args:
        original (float): precio del producto original
        discount (float/ str): valor del descuento o cadena = "no" en caso de no tenerlo

    Returns:
        print: Imprime el resultado por consola
    """
    if discount == "no":
        return print(f'El precio final es de {original} ya que no tiene ningún descuento')
    else:
        return print(f'El precio final aplicando el cupón de  descuento es de {original - discount}')
    


def calculate_prize_discount():
    """Función principal del programa
    """
    original_price = get_price_article()
    discount = get_discount_price(original_price)
    make_discount(original_price,discount)


calculate_prize_discount()