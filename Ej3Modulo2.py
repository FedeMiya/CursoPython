#3) Al terminar un día en un colegio secundario se hace una estadística de faltas sabiendo
#de cada curso:
#    Curso (1-5)
#    Presentes
#    Ausentes
# Calcular
#    Por cada curso el porcentaje de presentes sobre el total
#    Cantidad de ausentes en el colegio
#    Curso con mayor cantidad de ausente

curso = 1
mayorAusente = 0
totalAusentes = 0
mayorAusenteCurso = 0


while curso < 6:
    cantPresentes = int(input(f'Ingrese la cantidad de presentes del curso {curso}: '))
    cantAusentes = int(input(f'Ingrese la cantidad de ausentes del curso {curso}: '))
    porcentajePresentes = int((cantPresentes*100)/(cantPresentes+cantAusentes))
    print(f'El porcentaje de asistencia del curso {curso} fue de {porcentajePresentes}%')
    totalAusentes += cantAusentes
    if cantAusentes > mayorAusente:
        mayorAusente = cantAusentes
        mayorAusenteCurso = curso
    curso += 1

print(f'El total de ausentes del colegio fue de {totalAusentes}')
print(f'El curso con mayores ausentes fue el {mayorAusenteCurso}')