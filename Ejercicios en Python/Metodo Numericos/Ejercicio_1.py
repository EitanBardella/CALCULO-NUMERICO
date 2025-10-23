#----------------------------ENUNCIADO----------------------------
# Utilice la iteración simple de punto fijo para localizar la raíz de:
# 
#     f(x) = 2*sin(x) - x
# 
# Haga una elección inicial de: x0 = 0.5
# 
# Itérese hasta que:  ε_a ≤ 0.001%
# 
# Compruebe que el proceso converge en forma lineal.

#----------------------------RESOLUCION----------------------------

import math #Modulo que permite utilizar funciones complejas

#Datos

x = 0.05
error_aprox = 100 #Comienza en 100% pq es el maximo error posible
error_deseado = 0.001 # Mi criterio de Pare
iteracion = 0 # Contador de la cantidad de iteraciones

#Ciclo while para que se itere hasta que se cumpla la condicion
while error_aprox > error_deseado:# El bucle se va a repetir hasta que el error aproximado sea menor al error deseado
    
    x_nuevo = 2*math.sin(x) # Es asi y no con el - x pq buscamos que se cumpla x = G(x), siendo nuestro G(x) = 2*sen(x) 

    iteracion += 1 #Cada vez que se cumple una iteracion se suma 1 al contador ( Poner += 1  es lo mismo que poner = +1 )

    error_aprox = abs((x_nuevo - x)/x_nuevo) * 100 #Calculo el error aprox
    
    print(f"Iteracion: {iteracion}, x = {x_nuevo:.10f}, Error Aproximado = {error_aprox:.6f}%")

    x = x_nuevo #Actualizo X, va al final luego del print, ya que el codigo lo lee de arriba hacia abajo. Osea que cuando
                #Imprime los valores en x pone el recien calculado, y luego este valor pasa a ser x para ser utilizado nuevamente
                #en el calculo del x_nuevo

