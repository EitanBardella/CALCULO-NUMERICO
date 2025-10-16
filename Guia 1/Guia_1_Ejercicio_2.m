#Ejercicio 2 de la Guia N°1

#Primero defino las variables iniciales
h = 0.1,
t(1) = 0,
N(1)=500,
k = 1,

#Ecuacion logical
for i = 1:2
  N(i+1) = N(i) + h*(-k * N(i)),
  t(i+1) = t(i) + h,
endfor

# Gráfico
plot(t, N, "r-o");
xlabel('Tiempo t');
ylabel('N(t)');
title('Método de Euler - Decaimiento exponencial');
grid on;
