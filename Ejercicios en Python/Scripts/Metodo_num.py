import math
import tkinter as tk
from tkinter import ttk, messagebox

v = tk.Tk()
v.title("METODOS NUMERICOS")
v.geometry("650x600")

#------------------Frames------------------

#------------------Variables de acceso global------------------

error_aproximado = 100
iteracion = 0

#------------------Funciones------------------

def g(x):
        #Evalúa la función g(x) escrita por el usuario
        expresion = entry_x_gx.get()
        try:
            return eval(expresion, {"x": x, "math": math})
        except Exception as e:
            print("Error al evaluar g(x):", e)
        return None
    

def calcular():
    global error_aproximado, iteracion

    # Limpiar la tabla antes de comenzar
    for i in lista.get_children():
        lista.delete(i)

    # Tomar los datos de las entradas
    try:
        x = float(entry_inicial.get())
        error_deseado = float(entry_error_deseado.get())
    except ValueError:
        print("Error: asegúrese de ingresar números válidos.")
        return
    
    while error_aproximado > error_deseado:
        x_nuevo = g(x)  # Calcular g(x)

        if x_nuevo is None:
            messagebox.showerror("Error al ingresar G(x)","Asegurese de que esta ingresando la funcion correctamente.\n En caso de ingresar senos, cosenos o raises ingresarlo como math.sin(x),cos(x), sqrt(x). \n Si ingresa una potencia escribala como **")
            
            return

        iteracion += 1
        error_aproximado = abs((x_nuevo - x) / x_nuevo) * 100  # Calcular error
        print(f"Iteración {iteracion}: x = {x_nuevo:.10f}, Error = {error_aproximado:.6f}%")

        # Agregar fila a la tabla
        lista.insert("", "end", values=(iteracion, f"{x:.10f}", f"{x_nuevo:.10f}", f"{error_aproximado:.6f}%"))

        # Actualizar x para la siguiente iteración
        x = x_nuevo

        # Por seguridad: evitar bucles infinitos
        if iteracion > 1000:
            print("El método no converge o supera el límite de iteraciones.")
            break
    return 

#------------------Widgets------------------

#Titulo
titulo = tk.Label(v, text="METODO DE PUNTO FIJO")
titulo.grid(row=0, column= 1,pady=10, padx=20)

#Entries
valor_inicial = tk.Label(v, text="Ingrese el valor inicial")
valor_inicial.grid(row=2, column=0, pady=10, padx=20)
entry_inicial = tk.Entry(v)
entry_inicial.grid(row=2, column=1, pady=10, padx=20)

error_deseado = tk.Label(v, text="Ingrese el error deseado")
error_deseado.grid(row=3, column=0, pady=10, padx=20)
entry_error_deseado = tk.Entry(v)
entry_error_deseado.grid(row=3, column=1, pady=10, padx=20)

x_gx = tk.Label(v, text="Ingrese g(x)")
x_gx.grid(row=4, column=0, pady=10, padx=20)
entry_x_gx = tk.Entry(v)
entry_x_gx.grid(row=4, column=1, pady=10, padx=20)

#Botones
calcular1 = tk.Button(v, text="CALCULAR", command= calcular)
calcular1.grid(row=5, column=1, pady=10, padx=20)

#Lista

lista = ttk.Treeview(v, columns=("Iteracion", "Xn", "X_nuevo", "Error"), show="headings")
lista.heading("Iteracion", text="Iteracionea")  # Define el nombre de las columnas
lista.heading("Xn", text="Xn")
lista.heading("X_nuevo", text="X_nuevo")
lista.heading("Error", text="Error")
lista.column("Iteracion", width=150) # Define el ancho para cada columna
lista.column("Xn", width=150)
lista.column("X_nuevo", width=100)
lista.column("Error", width=100)
lista.grid(row=6, column=0, columnspan=3)


v.mainloop()