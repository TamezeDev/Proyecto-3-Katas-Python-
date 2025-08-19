"""    Crea la clase UsuarioBanco

        Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
        Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
        Código a seguir:

            Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
            Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.
            Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
            Implementar agregar_dinero para aumentar el saldo del usuario.

        Caso de uso:
                a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
                b. Agregar 20 unidades al saldo de Bob.
                c. Transferir 80 unidades de Bob a Alicia.
                d. Retirar 50 unidades del saldo de Alicia.
    """

# DEFINIENDO VARIABLES, LISTAS, DICCIONARIOS, SETS, TUPLAS...
class UsuarioBanco:
    """Clase que representa un Banco y los movimentos de saldo de sus uruarios

          Args:
            nombre (str): nombre de usuario .
            saldo (int): salario inicial
            cuentra_corriente (bool): indica si tiene o no cuenta con ellos 
    """
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente
    def retirar_dinero(self,cantidad):
        """
        Método para sacar dinero de la cuenta
        Maneja errores por si no hubiese la cantidad o no se tiene cuenta en el banco
        """        
        if  self.cuenta_corriente != True:
            print(f'El usuario {self.nombre} no tiene cuenta corriente en este banco')
        elif 0 < self.saldo >= cantidad:
            self.saldo -= cantidad        
        else:
            print(f'Usted no tiene suficiente saldo para sacar {cantidad}')
    def transferir_dinero(self,cantidad,usuario_2):
        """
        Método para pasar dinero de un usuario a otro
        Maneja errores si alguno no tiene cuenta con el banco y si hay saldo en la cuenta del otro usuario
        """        
        self.usuario_2 = usuario_2
        if self.usuario_2.cuenta_corriente != True:
            print(f'El usuario {self.usuario_2.nombre} no tiene cuenta corriente en este banco')
        elif self.cuenta_corriente != True:
            print(f'El usuario {self.nombre} no tiene cuenta corriente en este banco')
        elif 0 < self.usuario_2.saldo >= cantidad:
            self.usuario_2.saldo -= cantidad
            self.saldo += cantidad
        else:
            print(f'El usuario {self.usuario_2.nombre} no tiene suficiente saldo para transferirle {cantidad}')
    def agregar_dinero(self,cantidad):
        """
        Método para aumentar el saldo
        """                
        self.saldo += cantidad


# EJECUCIÓN DEL CÓDIGO
user1 = UsuarioBanco("Alicia", 100, True)
user2 = UsuarioBanco("Bob", 50, True)
user3 = UsuarioBanco("Joe", 150, False)

user2.agregar_dinero(20)
user1.transferir_dinero(80,user2)
user1.retirar_dinero(50)

user3.transferir_dinero(20,user1)
user2.retirar_dinero(150)

