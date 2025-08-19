# Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.

# EJECUCIÓN DEL CÓDIGO
def checker_user_words():
    """Función que solicita tantas palabras como el usuario quiera. Después busca una palabra dentro de su propia lista

    Returns:
        print: devuelve si la palabra está o no en la lista
    """
    user_list = []
    while True:
        user_list.append(input('Introduzca la palabra: '))
        answer = input('¿Quiere seguir introduciendo palabras? (no = deja de solicitar palabras)  --> ')
        if answer == "no":
                key_word = input('Introduce una palabra para buscar en su lista: ')
                if key_word in user_list:                
                    return print(f'La palabra {key_word} está en la su lista')                
                else:
                    return print(f'La palabra {key_word} no está en la su lista')
        continue

checker_user_words()