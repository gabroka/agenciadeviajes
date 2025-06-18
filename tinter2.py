import tkinter as tk

def mostrar_seleccion():
    print("opcion seleccionada: ",variable_control.get())

def cambiar_color():
    color_seleccionado= variable_color.get()
    if color_seleccionado == 1:
        ventana.config(bg="Red")
    elif color_seleccionado == 2:
        ventana.config(bg="Blue")

ventana= tk.Tk()
ventana.title('radiobuton')

variable_control = tk.IntVar()#variable que almacenara la opcion elegida
opcion1= tk.Radiobutton(ventana, text='opcion 1', font=('Arial', 14), fg='blue', bg='lightgray',variable=variable_control, value=1)

opcion2= tk.Radiobutton(ventana, text='opcion 2', font=('Arial', 14), fg='blue', bg='lightgray',variable=variable_control, value=2)
opcion1.pack()
opcion2.pack()
boton1= tk.Button(ventana, text='mostrar seleccion', command=mostrar_seleccion)
boton1.pack()

variable_color= tk.IntVar()#variable que almacena el value de la opcion elegida
opcion3= tk.Radiobutton(ventana, text='rojo', variable=variable_color, value=1, command=cambiar_color)
opcion4= tk.Radiobutton(ventana, text='azul', variable=variable_color, value=2, command=cambiar_color)
opcion3.pack()
opcion4.pack()

ventana.mainloop()