# Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.

# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
pass1 = 1234564789
pass2 = "2025_ConTraSeña"
# EJECUCIÓN DEL CÓDIGO
def transform_to_hidden_str(x):
    """Función para ocultar los caracteres de una variable excepto los 4 últimos

    Args:
        x (int, str): recibe la contraseña del usuario
    Return:
        (str): devuelve sting con la parte ya oculta
    """
    x = str(x)
    y = ""
    for num in range(len(x) - 4):
        y = y + "#"
    y += x[-4:]
    return y

print(transform_to_hidden_str(pass1))
print(transform_to_hidden_str(pass2))
