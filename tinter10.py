import tkinter as tk

""" def abrir_ventana():
    ventana_toplevel= tk.Toplevel(ventana)
    ventana_toplevel.title('ventana toplevel')
    ventana_toplevel.geometry('400x200+300+600') """

def eliminar_ventana(ventana):
    ventana.destroy()

ventana = tk.Tk()
ventana.title('ventana principal')
ventana.geometry('600x400')

ventana_toplevel= tk.Toplevel(ventana)
ventana_toplevel.title('ventana toplevel')
ventana_toplevel.geometry('400x200+300+600')
#btn = tk.Button(ventana, text='abrir ventana tl', command=abrir_ventana)
#btn.pack()
btn_destroy= tk.Button(ventana,text='eliminar ventana', command=lambda: eliminar_ventana(ventana_toplevel))
btn_destroy.pack()
ventana.mainloop()