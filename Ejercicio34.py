"""Crea la clase Arbol
        Define un árbol genérico con un tronco y ramas como atributos.
        Métodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.
        Código a seguir:

            Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
            Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
            Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
            Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
            Implementar el método quitar_rama para eliminar una rama en una posición específica.
            Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y sus longitudes.

        Caso de uso:
                a. Crear un árbol.
                b. Hacer crecer el tronco una unidad.
                c. Añadir una nueva rama.
                d. Hacer crecer todas las ramas una unidad.
                e. Añadir dos nuevas ramas.
                f. Retirar la rama situada en la posición 2.
                g. Obtener información sobre el árbol.
                """

# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
class Arbol:
    """Clase que representa un árbol y su evolución.

          Args:
            tronco (int): numero de troncos iniciales .
            ramas (list): lista que almacena el numero de ramas y sus longitudes
    """
    def __init__(self,tronco ,ramas):
        self.tronco = tronco
        self.ramas = ramas 
    def crecer_tronco(self):
        """
        Método para hacer crecer una unidad al tronco
        """
        self.tronco += 1
    def nueva_rama(self):
        """
        Método añadir una nueva rama
        """
        self.ramas.append(1)
    def crecer_ramas(self):
        """
        Método para hacer crecer una unidad a cada rama
        """
        self.ramas = [rama + 1 for rama in self.ramas]
    def quitar_rama(self, posicion):
        """
        Método para eliminar la rama de la posiciñon que le digamos
        En caso que sea mayor a las que o menor que 0 lanza mensaje de error
        """
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print(f'No se puede eliminar la rama en la posición {posicion}: posición inválida')
    def info_arbol(self):
        """
        Método para mostrar la incormaciíon comple actual del árbol
        Return: (dict): devuelve un diccionario con la info
        """
        return{
            'longitud de tronco': self.tronco,
            'número de ramas': len(self.ramas),
            'longitud de ramas': self.ramas
        }

# EJECUCIÓN DEL CÓDIGO
manzano = Arbol(1,[])
manzano.crecer_tronco()
manzano.nueva_rama()
manzano.crecer_ramas()
manzano.quitar_rama(2)

info = manzano.info_arbol()
print(info)