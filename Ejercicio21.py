# Crea una función que calcule el cubo de un número dado mediante una función lambda.

# EJECUCIÓN DEL CÓDIGO
def receive_num():
    while True:
        try:
            num = int(input("Introduzca un número para calcular su potencia elevada a 3: "))
            return num
        except ValueError:
            print('Error: Debe introducir un valor numérico')
            continue
user_num = receive_num()
cube_num = lambda i : i*i*i
print(f'El cubo del número {user_num} es {cube_num(user_num)}')