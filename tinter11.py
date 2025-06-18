import tkinter as tk

def abrirArchivo():
    print('archivo abierto')

ventana = tk.Tk()
menuboton = tk.Menubutton(ventana, text="archivo")
menuboton.pack()

menu = tk.Menu(menuboton)
menuboton.config(menu=menu)
menu.add_command(label='abrir', command=abrirArchivo)
menu.add_command(label='guardar')
ventana.mainloop()