# Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

# EJECUCIÓN DEL CÓDIGO
def anagrama_searcher(a,b):
    """Función para buscar si una palabra esta compuesta por las mismas letras pero orden diferente(anagramas)

    Args:
        a (str): palabra 1
        b (str): palabra 2

    Returns:
        prints: imprime si son o no son anagramas
    """
    if sorted(a.lower()) == sorted(b.lower()):
        return print(f'La palabras {a} y {b} son anagramas')
    return print(f'Las palabra {a} y {b} no son anagramas')

anagrama_searcher("cara", "arca")
anagrama_searcher("lobo","bolo")
anagrama_searcher("seta","bolo")