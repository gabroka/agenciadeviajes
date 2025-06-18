import tkinter as tk

def habilitar():
    if variable_chek.get():
        boton1.config(state='normal') 
    else:
        boton1.config(state='disabled')

def btn_activado():
    if variable_chek.get():
        print('comando habilitado')

ventana = tk.Tk()
ventana.title('chekbuton')

variable_chek = tk.BooleanVar()
chek1 = tk.Checkbutton(ventana, text='habilitar', variable=variable_chek, command=habilitar)
chek1.pack()
boton1 = tk.Button(ventana, text = 'boton', state='disabled', command=btn_activado)
boton1.pack()
ventana.mainloop()