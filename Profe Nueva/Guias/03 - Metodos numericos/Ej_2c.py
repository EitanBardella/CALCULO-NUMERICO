# Ejercicio 2 – Método de Punto Fijo
#
# Se desea aplicar el método de punto fijo para encontrar soluciones de la ecuación:
#
#     x = h(x) = e^(-x) * (log(x) + 1.3)
#
# Esta función tiene dos puntos fijos en el intervalo (0,1].
#
# a) Analizar cuál de los dos puntos fijos puede ser encontrado mediante iteraciones de punto fijo.
#    Justificar la elección en base al comportamiento de la función y la convergencia esperada.
#
# b) Realizar las tres primeras iteraciones del método de punto fijo partiendo de la semilla x0 = 0.3.
#    Mostrar los valores obtenidos y el error aproximado en cada paso.
#
# c) Programar un algoritmo que realice 10 o más iteraciones del método de punto fijo,
#    partiendo de las siguientes semillas: x0 = 0.05, x0 = 0.3, x0 = 0.8.
#    Analizar los resultados obtenidos para cada caso y confirmar lo expresado en el punto a).

# En este script realizo el pto c.

import math 

#Datos
x = 0.3 #Lo actualizo con cada X0
error_aprox = 100 #Comienza en 100% pq es el maximo error posible
error_deseado = 0.01 # Mi criterio de Pare
iteracion = 0 # Contador de la cantidad de iteraciones


#Funcion g(x)

def g(x): #Recibe el x = x_nuevo por parametro y lo retorna
    return math.exp(-x) * (math.log10(x) + 1.3) 

print(f"X0 = {x}")
#Ciclo while para que se itere hasta que se cumpla la condicion
while error_aprox > error_deseado:# El bucle se va a repetir hasta que el error aproximado sea menor al error deseado
    
    x_nuevo = g(x) #Aca ejecuta la funcion (Osea dentro de esta variable se guarda el valor que retorna la funcion luego de ser ejecutada)

    iteracion += 1 #Cada vez que se cumple una iteracion se suma 1 al contador ( Poner += 1  es lo mismo que poner = +1 )

    error_aprox = abs((x_nuevo - x)/x_nuevo) * 100 #Calculo el error aprox
    
    print(f"Iteracion: {iteracion}, x(n) = {x} ,x(n+1) = {x_nuevo:.10f}, Error Aproximado = {error_aprox:.6f}%")

    x = x_nuevo #Actualizo X, va al final luego del print, ya que el codigo lo lee de arriba hacia abajo. Osea que cuando
                #Imprime los valores en x pone el recien calculado, y luego este valor pasa a ser x para ser utilizado nuevamente
                #en el calculo del x_nuevo

#Resultados:
# X0 = 0.3 -->    Iteracion: 1, x(n) = 0.3 ,x(n+1) = 0.5757055852, Error Aproximado = 47.890031%
                # Iteracion: 2, x(n) = 0.5757055851753644 ,x(n+1) = 0.5961591616, Error Aproximado = 3.430892%
                # Iteracion: 3, x(n) = 0.5961591615513107 ,x(n+1) = 0.5924424120, Error Aproximado = 0.627360%
                # Iteracion: 4, x(n) = 0.5924424119953302 ,x(n+1) = 0.5931465442, Error Aproximado = 0.118711%
                # Iteracion: 5, x(n) = 0.5931465441976687 ,x(n+1) = 0.5930140962, Error Aproximado = 0.022335%
                # Iteracion: 6, x(n) = 0.5930140962226119 ,x(n+1) = 0.5930390439, Error Aproximado = 0.004207%
                #|Este X0 converge en el pto fijo

# X0 = 0.05 --> Iteracion: 1, x(n) = 0.05 ,x(n+1) = -0.0009797622, Error Aproximado = 5203.279233%
                #|Este X0 diverge y no se acerca a ninguna raiz, no se puede hacer Log(<0)

#X0 = 0.8 -->     Iteracion: 1, x(n) = 0.8 ,x(n+1) = 0.5405831776, Error Aproximado = 47.988327%
                # Iteracion: 2, x(n) = 0.5405831775948916 ,x(n+1) = 0.6015479208, Error Aproximado = 10.134644%
                # Iteracion: 3, x(n) = 0.6015479208334076 ,x(n+1) = 0.5913999116, Error Aproximado = 1.715930%
                # Iteracion: 4, x(n) = 0.5913999116192918 ,x(n+1) = 0.5933418180, Error Aproximado = 0.327283%
                # Iteracion: 5, x(n) = 0.5933418180232372 ,x(n+1) = 0.5929772861, Error Aproximado = 0.061475%
                # Iteracion: 6, x(n) = 0.5929772860614654 ,x(n+1) = 0.5930459746, Error Aproximado = 0.011582%
                # Iteracion: 7, x(n) = 0.593045974575934 ,x(n+1) = 0.5930330408, Error Aproximado = 0.002181%
                #|Este X0 converge en el pto fijo

