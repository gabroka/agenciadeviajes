import tkinter as tk

ventana = tk.Tk()

booleano = tk.BooleanVar(value=True)
casilla = tk.Checkbutton(ventana, text='Aceptar', variable=booleano)
casilla.pack()

def actualizar(*args):
    print(booleano.get())

booleano.trace_add('write', actualizar)    

ventana.mainloop()