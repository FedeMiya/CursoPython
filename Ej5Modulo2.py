#5) Ingresar 10 números mayores a 3 y menores a 8. Mostrar el valor ingresado en
#número y letras.
numeros = {4:'cuatro',5:'cinco',6:'seis',7:'siete'}
numerosIngresados = 0
while numerosIngresados <= 10:
    for i in numeros:
        number = int(input('Ingrese un número (el mismo debe ser mayor a 3 y menor a 8): '))
        if number in numeros:
            print(f'{number} --> {numeros.get(number)}')
            numerosIngresados = numerosIngresados + 1
        else:
            print('El número ingresado es incorrecto: ')
    