# -*- coding: utf-8 -*-
#2) Ingresar números hasta que el último sea cero. Calcular la cantidad de positivos.

positive = 0

numberChosen = True

while numberChosen:
    num = int(input("Ingrese un numero: ")) 
    if num == 0:
        numberChosen = False
    if num > 0:
        positive += 1
    


print(f'La cantidad de positivos ingresados es: {positive}')