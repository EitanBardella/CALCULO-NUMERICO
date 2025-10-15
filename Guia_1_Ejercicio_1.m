#Ejercicio 1 de la Guia N°1

#Resolucion por metodo de Euler
# Ejercicio 1 - Método de Euler

# Datos iniciales
h = 0.1;      # Paso
r = 0.1;
k = 5;
P(1) = 1;     # Condición inicial: P(0) = 1
t(1) = 0;     # Tiempo inicial

# Ciclo (por ejemplo, 20 pasos)
for i = 1:2 #2 iteraciones
  P(i+1) = P(i) + h*(r*P(i)*(1 - P(i)/k));  # Ecuación logística
  t(i+1) = t(i) + h;
endfor

# Gráfico
plot(t, P, 'b-o');
xlabel('Tiempo t');
ylabel('P(t)');
title('Método de Euler - Crecimiento logístico');
grid on;


