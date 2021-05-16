#8. Leer un número y calcular la suma de los números naturales hasta ese número.
#Modificar el algoritmo para que se pueda procesar muchos números. Dar por terminada la
#entrada cuando el número sea 0.

n = int(input('Ingrese un número: '))
nSum = 0
while n != 0:
        nSum += n
        n += -1
print (nSum)