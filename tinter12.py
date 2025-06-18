import tkinter as tk

ventana = tk.Tk()

barra_menu= tk.Menu(ventana)
ventana.config(menu=barra_menu)

archivo_menu= tk.Menu(barra_menu,tearoff=0)
#primer menu en cascada
barra_menu.add_cascade(label='Archivo', menu=archivo_menu)
archivo_menu.add_command(label="Nuevo")
archivo_menu.add_command(label="abrir")
archivo_menu.add_separator()
archivo_menu.add_command(label="salir")
#añadir un nuevo menu de cascada
editar_menu=tk.Menu(barra_menu,tearoff=0)
barra_menu.add_cascade(label='editar', menu=editar_menu)
editar_menu.add_cascade(label='deshacer')
editar_menu.add_cascade(label='rehacer')
ventana.mainloop()