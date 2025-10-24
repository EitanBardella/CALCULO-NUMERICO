#Ejercicio depredador conejo
clear all
# valores iniciales
A=0.4; # natalidad conejo
B=0.3; # mortalidad conejo
C=0.05; # tasa depredación zorros a conejos
D=0.37; # mortalidad de zorros
x(1)=5; # conejos población
y(1)=2; # zorros población
t(1)=0;
h=0.1; # avance
#Los valores para poblaciones estables son:
#(y,x) = (0,0) y (7.4,1.33)


#ecuaciones
for i = 1:100
  x(i+1)=x(i)+h*(A*x(i)-B*x(i)*y(i));
  y(i+1)=y(i)+h*(C*x(i)*y(i)-D*y(i));
  t(i+1)=t(i)+h;
endfor
#En funcion de Y
plot(t, y, 'b-o');
xlabel('Tiempo t');
ylabel('P(t)');
title('Método de Euler - Crecimiento logístico');
#En funcion de X
hold on;
plot(t, x , 'r-o');
xlabel('Tiempo t');
ylabel('P(t)');
title('Método de Euler - Crecimiento logístico');

