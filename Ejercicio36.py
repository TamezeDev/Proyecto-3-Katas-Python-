"""    Crea una función llamada procesar_texto

        Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
        Código a seguir:

            Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
            Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
            Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
            Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.

        Caso de uso:
            Verificar el funcionamiento completo de procesar_texto.

    Returns:
        _type_: _description_
    """

# EJECUCIÓN DEL CÓDIGO
def contar_palabras(texto):
    """Función para contar el número de palabras del texto introducido

    Args:
        texto (str): texto que el usuario ha introducido anteriormente
    """
    palabras_texto = texto.split()
    print(f'El texto introducido tiene {len(palabras_texto)} palabras.')
    return       

def reemplazar_palabras(texto):
    """Función para reemplazar las palabras del texto por una nueva. Maneja errores por si la palabra no estuviera

    Args:
        texto (str): texto que el usuario ha introducido anteriormente

    Returns:
        str: texto modificado con el intercambio
    """
    palabra_antigua = input('¿Qué palabra es la que quieres reemplazar?\n')
    palabra_nueva = input('¿Por qué palabra quieres reemplazarla?\n')
    if texto.find(palabra_antigua) != -1:
        texto = texto.replace(palabra_antigua,palabra_nueva)
        (print(f'El texto con la palabra reemplazada es: {texto}'))
        return texto
    else:
        print(f'La palabra {palabra_antigua} no se encuentra en el texto')
        return texto

def eliminar_palabra(texto):
    """Función para eliminar una palabra de un texto. Maneja errores por si la palabra no se encuentra en el texto

    Args:
        texto (str): texto que el usuario ha introducido anteriormente

    Returns:
        str: texto modificado sin la palabra
    """
    palabra_eliminada = input('¿Qué palabra es la que quieres eliminar?\n')
    palabras_texto = texto.split()
    try:
        palabras_texto.remove(palabra_eliminada)
        texto = " ".join(palabras_texto)
        (print(f'El texto con la palabra eliminada es: {texto}'))
        return texto
    except ValueError:
        print(f'La palabra {palabra_eliminada} no se encuentra en el texto')
        return texto
def añadir_palabra(texto):
    """Función para añadir una nueva palabra al texto en la posición que queramos
    Args:
        texto (str): texto que el usuario ha introducido anteriormente
    Returns:
        str: texto modificado con la palabra añadida
    """
    palabra_nueva = input('¿Que palabra quiere añadir?\n')
    try:
        posicion = int(input('¿En qué posición quiere añadir la palabra?\n'))
        texto_lista = texto.split()
        texto_lista.insert(posicion - 1, palabra_nueva)
        texto = " ".join(texto_lista)
        print(f'El texto incluyendo la nueva palabra es: {texto}')
        return texto
    except ValueError:
        print('Debe introcucir un valor numérico en la posición')
        return texto

def seguir_usando_programa():
    """Función para preguntar al usuario si quiere seguir usando el programa cada vez que haga una operación
    Maneja errores por si no introduce una respuesta válida

    Returns:
        str: devuelve la elección de la salida
    """
    while True:
        eleccion_salida = input(('¿Necesita seguir usando el programa?\n'))
        if  eleccion_salida == "no":
            print('Cerrando el programa...') 
            return eleccion_salida
                        
        elif eleccion_salida != "si":
            print('Error: Ha introducido una respuesta incorrecta.\n')
        else:
            return            

def procesar_texto():  
    """Función principal del programa. Pregunta al usuario al texto y llama a las funciones que va necesitando. Maneja posibles errores
    """
    texto_usuario = input('Introduce el texto que guste para guardarlo en el sistema: ')
    while True:
        try: 
            seleccion_usuario = int(input('Elija la opcion que necesite:\n1 - Contar la palabras del texto\n2 - Reemplazar palabras del texto\n3 - Eliminar palabra del texto\n4 - Añadir una palabra al texto\n '))
            if seleccion_usuario == 1: 
                contar_palabras(texto_usuario)               
                if  seguir_usando_programa() == "no":
                    break
                else:
                    pass
            elif seleccion_usuario == 2:
                texto_usuario = reemplazar_palabras(texto_usuario)
                if seguir_usando_programa() == "no":
                    break
                else:
                    pass                
            elif seleccion_usuario == 3:
                texto_usuario = eliminar_palabra(texto_usuario)
                if  seguir_usando_programa() == "no":
                    break
                else:
                    pass
            elif seleccion_usuario == 4:
                texto_usuario = añadir_palabra(texto_usuario)
                if seguir_usando_programa() =="no":
                    break
                else:
                    pass
        except ValueError:
                print('Error: Ha introducido un valor incorrecto.\n')

procesar_texto()