import time
import tkinter as tk

def actualizar_ventana():
    label.configure(text=time.strftime('%H:%M:%S'))
    ventana.after(1000, actualizar_ventana)

def agregarTexto():
    labelframe.configure(text=entradaDatos.get())

ventana = tk.Tk()

ventana.title('sistema de agencia de viajes')
#ventana.geometry('ancho x alto')
ventana.geometry('600x200')
#ventana.geometry('600x200+100+20') inicializa la ventana en la posicion dada por +100+20
ventana.minsize(200,100)
ventana.maxsize(1000,800)
#ventana.resizable(False,False)
#ventana.iconbitmap('icono.ico')
#ventana.attributes('-alpha',0.5)hace que la ventana sea transparente
ventana.configure(bg='pale green')


frame1= tk.Frame(ventana)
frame1.configure(bg='blue',bd=10,width=150, height=150)
frame1.pack()
frame2=tk.Frame(frame1)
frame2.configure(bg='gold',bd=10,width=50, height=50)

boton= tk.Button(frame1, text = 'hola')
boton.pack()

labelframe= tk.LabelFrame(ventana, text='opciones', bg='yellow', padx=10,pady=10)
labelframe.configure(width=200,height=200)
labelframe.pack()

boton1 =tk.Button(labelframe, text='ventas por periodo')
boton1.pack()
label= tk.Label(ventana)
label.pack()
actualizar_ventana()

entradaDatos= tk.Entry(ventana)
entradaDatos.pack()
boton2=tk.Button(ventana, text='aceptar',command=agregarTexto)
boton2.pack()
ventana.mainloop()


