import math
import tkinter as tk
from tkinter import ttk, messagebox


v = tk.Tk()
v.title("METODOS NUMERICOS")
v.geometry("525x525")

# Icono
try:
    v.iconbitmap("ccc.ico")  # coloca el archivo icono.ico en la misma carpeta
except:
    print("No se pudo cargar el icono, asegúrese de que icono.ico exista.")

#------------------Frames------------------
#Inicial
inicial_frame = tk.Frame(v)
inicial_frame.rowconfigure(0, minsize=50)
inicial_frame.columnconfigure(0, minsize=50)
inicial_frame.columnconfigure(1, minsize=50)

#Punto Fijo
pf_frame = tk.Frame(v)
pf_frame.rowconfigure(0, minsize=50)
pf_frame.columnconfigure(0, minsize=50)
pf_frame.columnconfigure(1, minsize=50)

#Newton Raphson
nr_frame = tk.Frame(v)
nr_frame.rowconfigure(0, minsize=50)
nr_frame.columnconfigure(0, minsize=50)
nr_frame.columnconfigure(1, minsize=50)
#------------------Variables de acceso global------------------

error_aproximado = 100
iteracion = 0

#------------------------------------FUNCIONES------------------------------------

#------------------Frame: Inicial------------------
def mostrar_frame(frame):
    #Oculta todos los frames y muestra solo el indicado
    for f in (inicial_frame, pf_frame, nr_frame):
        f.grid_forget()
    frame.grid(row=0, column=0, sticky="nsew")

def btn_pf():
    mostrar_frame(pf_frame)

def btn_nr():
    mostrar_frame(nr_frame)
#------------------M.PUNTO FIJO------------------

def g(x):
        #Evalúa la función g(x) escrita por el usuario
        expresion = entry_x_gx.get()
        try:
            return eval(expresion, {"x": x, "math": math})
        except Exception as e:
            print("Error al evaluar g(x):", e)
        return None
    

def calcular_pf():
    # Reiniciar variables por ejecución
    iteracion = 0
    error_aproximado = float('inf')

    # Limpiar la tabla antes de comenzar
    for i in listapf.get_children():
        listapf.delete(i)

    # Tomar los datos de las entradas
    try:
        x = float(entry_inicial.get())
        error_deseado = float(entry_error_deseado.get())
    except ValueError:
        messagebox.showerror("Entrada inválida", "Ingrese números válidos en valor inicial y error deseado.")
        return

    max_iter = 1000
    while error_aproximado > error_deseado and iteracion < max_iter:
        x_nuevo = g(x)
        if x_nuevo is None:
            messagebox.showerror(
                "Error al ingresar G(x)",
                "Asegurese de ingresar la función correctamente. Use math.sin(x), math.cos(x), math.sqrt(x), y potencias con **."
            )
            return

        iteracion += 1
        # Evitar división por cero si x_nuevo == 0
        if x_nuevo != 0:
            error_aproximado = abs((x_nuevo - x) / x_nuevo) * 100
        else:
            error_aproximado = abs(x_nuevo - x) * 100

        listapf.insert("", "end", values=(iteracion, f"{x:.10f}", f"{x_nuevo:.10f}", f"{error_aproximado:.6f}%"))
        x = x_nuevo

    if iteracion >= max_iter:
        messagebox.showwarning("No converge", "Se alcanzó el límite de iteraciones sin convergencia.")

#------------------M.NEWTON RAPHSON------------------


def calcular_nr():
    # Reiniciar variables por ejecución
    iteracion = 0
    error_aproximado = float('inf')

    # Limpiar la tabla antes de comenzar
    for i in listanr.get_children():
        listanr.delete(i)

    # Tomar los datos de las entradas
    try:
        x = float(entry_inicial.get())
        error_deseado = float(entry_error_deseado.get())
    except ValueError:
        messagebox.showerror("Entrada inválida", "Ingrese números válidos en valor inicial y error deseado.")
        return

    max_iter = 1000
    while error_aproximado > error_deseado and iteracion < max_iter:
        # Evaluar f(x) y f'(x)
        try:
            entorno = {"__builtins__": None, "math": math, "x": x}
            f_val = eval(entry_fx.get(), entorno)
            df_val = eval(entry_fx_d.get(), entorno)

        except Exception:
            messagebox.showerror(
                "Error en f o f'",
                "Revise las expresiones de f(x) y f'(x). Use math.sin(x), math.cos(x), math.sqrt(x), y potencias con **."
            )
            return

        # Verificar derivada cero
        if df_val == 0:
            messagebox.showerror("Derivada cero", "La derivada es cero en x; Newton-Raphson falla.")
            return

        # Paso de Newton-Raphson: x_{n+1} = x - f(x)/f'(x)
        x_nuevo = x - (f_val / df_val)

        iteracion += 1
        if x_nuevo != 0:
            error_aproximado = abs((x_nuevo - x) / x_nuevo) * 100
        else:
            error_aproximado = abs(x_nuevo - x) * 100

        listanr.insert("", "end", values=(iteracion, f"{x:.10f}", f"{x_nuevo:.10f}", f"{error_aproximado:.6f}%"))
        x = x_nuevo


    if iteracion >= max_iter:
        messagebox.showwarning("No converge", "Se alcanzó el límite de iteraciones sin convergencia.")

#------------------------------------Widgets------------------------------------

#------------------FRAME: INICIAL------------------

titulo = tk.Label(inicial_frame, text="METODO NUMÉRICOS")
titulo.grid(row=0, column= 2,pady=10, padx=20, sticky="nsew")

txt = tk.Label(inicial_frame, text="Seleccione un metodo numérico")

btn_ptof = tk.Button(inicial_frame, text="Metodo de Punto Fijo", command=btn_pf)
btn_ptof.grid(row=2, column= 2,pady=10, padx=20, sticky="nsew")

btn_nr1 = tk.Button(inicial_frame, text="Metodo de Newton Raphson",command=btn_nr)
btn_nr1.grid(row=3, column= 2,pady=10, padx=20, sticky="nsew")

#------------------FRAME: METODO PUNTO FIJO------------------
#Titulo
titulo = tk.Label(pf_frame, text="METODO DE PUNTO FIJO")
titulo.grid(row=0, column= 1,pady=10, padx=20, sticky="nsew")

#Entries
valor_inicial = tk.Label(pf_frame, text="Ingrese el valor inicial")
valor_inicial.grid(row=2, column=0, pady=10, padx=20, sticky="nsew")
entry_inicial = tk.Entry(pf_frame)
entry_inicial.grid(row=2, column=1, pady=10, padx=20, sticky="nsew")

error_deseado = tk.Label(pf_frame, text="Ingrese el error deseado")
error_deseado.grid(row=3, column=0, pady=10, padx=20, sticky="nsew")
entry_error_deseado = tk.Entry(pf_frame)
entry_error_deseado.grid(row=3, column=1, pady=10, padx=20, sticky="nsew")

x_gx = tk.Label(pf_frame, text="Ingrese g(x)")
x_gx.grid(row=4, column=0, pady=10, padx=20, sticky="nsew")
entry_x_gx = tk.Entry(pf_frame)
entry_x_gx.grid(row=4, column=1, pady=10, padx=20, sticky="nsew")

#Botones
calcular1 = tk.Button(pf_frame, text="CALCULAR", command= calcular_pf)
calcular1.grid(row=5, column=1, pady=10, padx=20, sticky="nsew")

volver_inicio = tk.Button(pf_frame, text="VOLVER AL INICIO", command=lambda: mostrar_frame(inicial_frame))
volver_inicio.grid(row=5, column=2, pady=10, padx=20, sticky="nsew")

#Lista

listapf = ttk.Treeview(pf_frame, columns=("Iteracion", "Xn", "X_nuevo", "Error"), show="headings")
listapf.heading("Iteracion", text="Iteraciones")  # Define el nombre de las columnas
listapf.heading("Xn", text="Xn")
listapf.heading("X_nuevo", text="X_nuevo")
listapf.heading("Error", text="Error")
listapf.column("Iteracion", width=150) # Define el ancho para cada columna
listapf.column("Xn", width=150)
listapf.column("X_nuevo", width=100)
listapf.column("Error", width=100)
listapf.grid(row=6, column=0, columnspan=3, sticky="nsew")

#------------------FRAME: METODO NEWTON RAPHSON------------------
#Titulo
titulo = tk.Label(nr_frame, text="METODO NEWTON RAPHSON")
titulo.grid(row=0, column= 1,pady=10, padx=20)

#Entries
valor_inicial = tk.Label(nr_frame, text="Ingrese el valor inicial")
valor_inicial.grid(row=2, column=0, pady=10, padx=20)
entry_inicial = tk.Entry(nr_frame)
entry_inicial.grid(row=2, column=1, pady=10, padx=20)
nr_frame
error_deseado = tk.Label(nr_frame, text="Ingrese el error deseado")
error_deseado.grid(row=3, column=0, pady=10, padx=20)
entry_error_deseado = tk.Entry(nr_frame)
entry_error_deseado.grid(row=3, column=1, pady=10, padx=20)

fx = tk.Label(nr_frame, text="Ingrese f(x)")
fx.grid(row=4, column=0, pady=10, padx=20)
entry_fx = tk.Entry(nr_frame)
entry_fx.grid(row=4, column=1, pady=10, padx=20)

fx_d = tk.Label(nr_frame, text="Ingrese f^(x)")
fx_d.grid(row=5, column=0, pady=10, padx=20)
entry_fx_d = tk.Entry(nr_frame)
entry_fx_d.grid(row=5, column=1, pady=10, padx=20)

#Botones
calcular1 = tk.Button(nr_frame, text="CALCULAR", command= calcular_nr)
calcular1.grid(row=6, column=1, pady=10, padx=20)

volver_inicio = tk.Button(nr_frame, text="VOLVER AL INICIO", command=lambda: mostrar_frame(inicial_frame))
volver_inicio.grid(row=6, column=2, pady=10, padx=20)

#Lista

listanr = ttk.Treeview(nr_frame, columns=("Iteracion", "Xn", "X_nuevo", "Error"), show="headings")
listanr.heading("Iteracion", text="Iteraciones")  # Define el nombre de las columnas
listanr.heading("Xn", text="Xn")
listanr.heading("X_nuevo", text="X_nuevo")
listanr.heading("Error", text="Error")
listanr.column("Iteracion", width=150) # Define el ancho para cada columna
listanr.column("Xn", width=150)
listanr.column("X_nuevo", width=100)
listanr.column("Error", width=100)
listanr.grid(row=7, column=0, columnspan=3)

#Mostrar el frame al iniciar el programa
mostrar_frame(inicial_frame)


v.mainloop()