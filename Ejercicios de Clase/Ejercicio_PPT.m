
#Valores Iniciales
clear all;
X(1)=5;
Y(1)=6;
t(1) = 0;
h = 0.1;

#Ecuaciones
for i = 1:10
  X(i+1) = X(i) + h*(-3*X(i) + Y(i)),
  Y(i+1) = Y(i) + h*(-4*X(i)-3*Y(i)),
  t(i+1) = t(i) + h,
endfor

# Gráfico
#En funcion de Y
plot(t, Y, 'b-o');
xlabel('Tiempo t');
ylabel('P(t)');
title('Método de Euler - Crecimiento logístico');
#En funcion de X
hold on;
plot(t, X , 'r-o');
xlabel('Tiempo t');
ylabel('P(t)');
title('Método de Euler - Crecimiento logístico');
grid on;
