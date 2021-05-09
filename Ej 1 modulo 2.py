# -*- coding: utf-8 -*-
# while, bucles, mientras se cumpla una condición
    #repetir instrucciones

# != distinto // == exactamente igual
semana = 1
gastoTotal = 0

while semana != 5: 
    gasto = float(input('¿Cuál fue el gasto?'))
    gastoTotal = (gastoTotal + gasto)
    print('El promedio de gasto semanal es {}'.format(gastoTotal/(semana)))
    #gasto total = 0 + valor ingresado
    semana = semana + 1
    #semana = 1 + 1
