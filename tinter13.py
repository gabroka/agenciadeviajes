import tkinter as tk

ventana = tk.Tk()

def mostrar_menu_contextual(event):
    menu_contextual.tk_popup(event.x_root, event.y_root)

menu_contextual= tk.Menu(ventana, tearoff=0)
menu_contextual.add_command(label='cortar')
menu_contextual.add_command(label='copiar')
menu_contextual.add_command(label='pegar')

entrada = tk.Entry(ventana)
entrada.pack()

#menu contextual a la ventana
ventana.bind('<Button-3>', mostrar_menu_contextual)

#menu contextual al entry
entrada.bind('<Button-3>', mostrar_menu_contextual)


ventana.mainloop()