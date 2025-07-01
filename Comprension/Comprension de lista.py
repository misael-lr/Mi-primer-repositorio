cuadrado = [i*i for i in range (1, 11)]
print(cuadrado)

circulo = []
for i in range (1, 11):
    circulo.append(i*i)
print(circulo)

estudiantes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
estudiantes_aprobados = list(filter(lambda x: x >= 8, estudiantes))
print(estudiantes_aprobados)