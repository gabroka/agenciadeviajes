import tkinter as tk
from tkinter.scrolledtext import ScrolledText
ventana= tk.Tk()
texto=tk.Text(ventana, width=40, height=10, wrap='word', bg='lightgray', fg='black', padx=10, pady=10, font=('helvetica', 12))
texto.insert('1.0', 'bienvenido a nuesto editor de texto')
texto.insert('end', '\n\neste es un ejemplo de texto resaltado', 'resaltado')
texto.tag_configure('resaltado', background='yellow', foreground='black')
contenido=texto.get('1.0', 'end')
texto.delete('1.0','end')
print(contenido)

def actualizar():
    print(texto.get())
texto.pack()

texto.bind('write', actualizar)
texto_desplazable = ScrolledText(ventana)
texto_desplazable.pack()

ventana.mainloop()