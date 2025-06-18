import tkinter as tk

def on_clik(event):
    print("boton presioando")

def on_clik2(event):
    print("boton presioando ruedita")

def on_clik3(event):
    print("boton presioando derecho")

def on_key_press(event):
    if event.char =='a':
        print("tecla a presioanda")

def on_resize(event):
    print(f"la ventana ha sido redimensionada {event.width}x{event.height}")

def on_mouse_move(event):
    #los valores de x e y estan en relacion al objeto sobre el que se mueve el mouse
    print(f"raton movido a la posicion {event.x}, {event.y}")

def on_clickx3(event):
        print(f"boton {event.widget['text']} presionado")

ventana = tk.Tk()
#eventos y funciones callback
boton = tk.Button(ventana, text='haz clik aqui boton izquierdo')
boton.pack()

boton.bind("<Button-1>",  on_clik)#la funcion se ejecuta cuando ocurre el evento, Button-1 asocial el boton izquierdo del mouse

boton1=tk.Button(ventana,text='haz clik aqui con la ruedita')
boton1.pack()

boton1.bind('<Button-2>',on_clik2)

boton2=tk.Button(ventana, text='haz clik aqui boton derecho')
boton2.pack()

boton2.bind('<Button-3>', on_clik3)


ventana.bind('<KeyPress>', on_key_press)

ventana.bind('<Configure>', on_resize)

ventana.bind('<Motion>', on_mouse_move)
botones3= [tk.Button(ventana, text=f'boton {i}') for i in range(3)]

for boton in botones3:
    boton.pack()
    boton.bind('<Button-1>', on_clickx3)

ventana.mainloop()