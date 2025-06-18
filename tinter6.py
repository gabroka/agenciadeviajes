import tkinter as tk

ventana= tk.Tk()
texto = tk.StringVar(value='hola mundo')
print(texto.get())
texto = tk.StringVar()
texto.set('nuevo texto')
print(texto.get())

etiqueta = tk.Label(ventana)
etiqueta.pack()

entri = tk.Entry(ventana, textvariable=texto)
entri.pack()
def actualizar_etiqueta(*args):
    etiqueta.config(text=texto.get())

texto.trace_add('write',actualizar_etiqueta)
ventana.mainloop()