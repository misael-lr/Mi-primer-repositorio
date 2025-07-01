# VARIABLES Y TIPOS DE DATOS.
# Ejemplo de tipos de datos

nombre = 'Jose'                 # str (cadena de texto)
edad = 21                       # int (entero)
altura = 5.6                    # float (decimal)
es_estudiante = True            # bool (booleano)

# Estructuras de datos

lista = [1, 2, 3, 4]
diccionario = {"nombre": 'Ana', 'edad': 18}
conjunto = {1, 2, 3}
tupla = (10, 20, 30)

#--------------------------------------------------------------
# CONDICIONALES: if / elif / else

edad = 18

if edad >= 18:
    print('Eres mayor de edad')
elif edad == 17:
    print('Casi eres mayor de edad')
else:
    print("Eres menor de edad")

#--------------------------------------------------------------
#BUCLES: for y while

nombre_clientes = ['Ana', 'Luis', 'Jose']         #recoriendo una lista
x = 0

for i in nombre_clientes:
    print('Hola', i)

while x < 5:
    print('Valor de x', x)
    x += 1

#-----------------------------------------------------------------
#FUNSIONES 

def sumar(a, b):
    resultado = a + b
    return resultado

print(sumar(5, 4))



