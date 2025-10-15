clear all
#Ejercicio 4 Guia 1

#Valores iniciales
Y(1) = 2, #Pto inicial
t(1) = 0, #Tiempo inicial
h = 0.1, #Avance

#Ecuacion diferencial dY/dt = t - Y
for i = 1:50
  Y(i+1) = Y(i) + h*( t(i) - Y(i) ),
  t(i+1) = t(i) + h
endfor




#Grafico
plot(t, Y, 'b-o');
xlabel('Tiempo t');
ylabel('Y(t)');
title('Método de Euler ');
grid on;
