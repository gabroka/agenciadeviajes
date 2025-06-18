import tkinter as tk

ventana = tk.Tk()
ventana.geometry('300x300')

entero = tk.IntVar(value=42)

print(entero.get())
#el valor selecconado es 1, deseleccionado es 0
casilla= tk.Checkbutton(ventana, text='aceptar', variable=entero, onvalue=1, offvalue=0)
casilla.pack()

def actualizar (*args):
    print(*args)
    print(args[1])
    print(args[2])
    print(entero.get())

entero.trace_add('write', actualizar)    

ventana.mainloop()