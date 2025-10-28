#----------------------------ENUNCIADO----------------------------
# Utilice los métodos de: a) Iteración de punto fijo

# para determinar una raíz de: f(x) = -x**2 + 1.8*x + 2.5
# usando x0 = 5
# Hacer el cálculo hasta que el error aproximado sea menor que:
# ea <= 0.05%
# Asimismo, realizar una comprobación del error de la respuesta final.

#----------------------------RESOLUCION----------------------------

#Despeje de la X:

#-x**2 + 1.8*x + 2.5 = 0 -----> x = (-2.5+x**2)/1.8 Este Despeje no se puede usar porque hace que x de valores que tienden al infinito rompiendo el programa

#Por lo que se utiliza x = raiz(1.8x +2.5)

import math #Modulo que permite utilizar funciones complejas

#Datos
x = 5
error_aprox = 100 #Comienza en 100% pq es el maximo error posible
error_deseado = 0.05 # Mi criterio de Pare
iteracion = 0 # Contador de la cantidad de iteraciones

#Funcion g(x)

def g(x):
    return math.sqrt(1.8*x + 2.5) #En este ejercicio utilizo una funcion en lugar de meterlo dentro del while para modulizar mas el script.
                                #En si la funcionalidad es la misma pero sirve para disminuir posibles errores con funciones mas pesadas.


#Ciclo while para que se itere hasta que se cumpla la condicion
while error_aprox > error_deseado:# El bucle se va a repetir hasta que el error aproximado sea menor al error deseado
    
    x_nuevo = g(x) 

    iteracion += 1 #Cada vez que se cumple una iteracion se suma 1 al contador ( Poner += 1  es lo mismo que poner = +1 )

    error_aprox = abs((x_nuevo - x)/x_nuevo) * 100 #Calculo el error aprox
    
    print(f"Iteracion: {iteracion}, x = {x_nuevo:.10f}, Error Aproximado = {error_aprox:.6f}%")

    x = x_nuevo #Actualizo X, va al final luego del print, ya que el codigo lo lee de arriba hacia abajo. Osea que cuando
                #Imprime los valores en x pone el recien calculado, y luego este valor pasa a ser x para ser utilizado nuevamente
                #en el calculo del x_nuevo