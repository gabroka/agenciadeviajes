import tkinter as tk

ventana= tk.Tk()
ventana.geometry('600x600')
frame= tk.Frame(ventana,bg="blue",width=300, height=200, padx=5, pady=10)
#frame.config(width=300, height=200)
""" label1= tk.Label(ventana, text='etiqueta 1')
label2= tk.Label(ventana, text='etiqueta 2')
label3= tk.Label(ventana, text='etiqueta 3')
label4= tk.Label(ventana, text='etiqueta 4')
label1.grid(row=0,column=0, padx=5,pady=5)
label2.grid(row=0,column=1, padx=5,pady=5)
label3.grid(row=1,column=0, padx=5,pady=5)
label4.grid(row=1,column=1, padx=5,pady=5) """

""" label5= tk.Label(frame, text='etiqueta 5')
label6= tk.Label(frame, text='etiqueta 6')
label7= tk.Label(frame, text='etiqueta 7')
frame.pack()
label5.pack(side="left", padx=5)
label6.pack(side="left", padx=5)
label7.pack(side="left", padx=5) """

label1= tk.Label(ventana, text='etiqueta 1')
label2= tk.Label(ventana, text='etiqueta 2')
label3= tk.Label(ventana, text='etiqueta 3')
label4= tk.Label(ventana, text='etiqueta 4')
label1.place(x=50, y=100)
label2.place(x=150, y=200)
label3.place(relx=0.25, rely=0.20)#es un porcentaje del contenedor %25 %20
label4.place(relx=0.50, rely=0.50)

ventana.mainloop()