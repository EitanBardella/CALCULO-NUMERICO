clear all
#Primero defino las variables iniciales
h = 0.1,
t(1) = 0,
y(1)=8,

#Escribo ciclo for
for i = 1:20
  y(i+1) = y(i) + h*(t(i)-y(i));
  t(i+1) = t(i) + h;
endfor
plot(t,y,'b');

