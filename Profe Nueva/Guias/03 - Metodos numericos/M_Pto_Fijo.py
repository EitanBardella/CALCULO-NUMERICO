
import math #Modulo que permite utilizar funciones complejas

#Datos
x = 0.08 #Lo autoimpongo
error_aprox = 100 #Comienza en 100% pq es el maximo error posible
error_deseado = 0.01 # Mi criterio de Pare
iteracion = 0 # Contador de la cantidad de iteraciones

#F(x) = x**2 + 2*x -3 ---> x = g(x) = raiz(-2*x +3)

#Funcion g(x)

def g(x): #Recibe el x = x_nuevo por parametro y lo retorna
    return math.exp(-x) * (math.log(x) + 1.3) 

print(f"X0 = {x}")
#Ciclo while para que se itere hasta que se cumpla la condicion
while error_aprox > error_deseado:# El bucle se va a repetir hasta que el error aproximado sea menor al error deseado
    
    x_nuevo = g(x) #Aca ejecuta la funcion (Osea dentro de esta variable se guarda el valor que retorna la funcion luego de ser ejecutada)

    iteracion += 1 #Cada vez que se cumple una iteracion se suma 1 al contador ( Poner += 1  es lo mismo que poner = +1 )

    error_aprox = abs((x_nuevo - x)/x_nuevo) * 100 #Calculo el error aprox
    
    print(f"Iteracion: {iteracion}, x = {x_nuevo:.10f}, Error Aproximado = {error_aprox:.6f}%")

    x = x_nuevo #Actualizo X, va al final luego del print, ya que el codigo lo lee de arriba hacia abajo. Osea que cuando
                #Imprime los valores en x pone el recien calculado, y luego este valor pasa a ser x para ser utilizado nuevamente
                #en el calculo del x_nuevo