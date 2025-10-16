#Ejercicio 1 Guia 2
clear all
#--------------Datos (Inventados)--------------
#Constates de proporcion
a = 0.4;
b = 0.3;
c = 0.05;
d = 0.37;
#Poblaciones iniciales
A(1) = 5;
B(1) = 2;

#Tiempo inicial
t(1) = 0;
h = 0.1; #Avance

#Ecuacion que representa la evolucion
for i = 1:200
  A(i+1) = A(i) + h*(a*A(i)-b*A(i)*B(i)); #Poblacion A

  B(i+1) = B(i) + h*(c*A(i)*B(i)-d*B(i)); #Poblacion B

  t(i+1) = t(i) + h;#Avance del tiempo
endfor

#Graficos
plot(t, A, "r-o");
hold on;
plot(t, B, "b-o");
xlabel("Tiempo");
ylabel("Población");
legend("A", "B");
title("Evolución de las poblaciones");
grid on;
