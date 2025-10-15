#Ejercicio 3 Guia 1 #Parte b

#Primero defino los valores iniciales

k = 0.5,
T(1) = 20, #Temperatura inicial del cuerpo
Ta = 25, #Temperatura ambiente
h = 0.1, #Avance
t(1) = 0 #Tiempo inicial

#Ley de Enfriamiento de Newton

for i = 1:100
   T(i+1) = T(i) + h*k*(Ta - T(i))
   t(i+1) = t(i) + h
 endfor

# Gráfico
plot(t, T, 'b-o');
xlabel('Tiempo (minutos)');
ylabel('Temperatura (°C)');
title('Método de Euler - Ley de enfriamiento de Newton');
grid on;



