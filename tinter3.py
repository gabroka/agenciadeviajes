import tkinter as tk

def chek():
    if variable_chek1.get():
            print('la opcion elegida es la 1')

    if variable_chek2.get():
            print('la opcion elegida es la 2')

ventana = tk.Tk()
ventana.title('checkbuton')

variable_chek1= tk.BooleanVar()
variable_chek2= tk.BooleanVar()
check1= tk.Checkbutton(ventana, text='opcion 1', font=('Arial', 14), fg="blue", bg='lightgray',variable=variable_chek1 ,command=chek)
check2= tk.Checkbutton(ventana, text='opcion 2', font=('Arial', 14), fg="blue", bg='lightgray',variable=variable_chek2 ,command=chek)

check1.pack()
check2.pack()

ventana.mainloop()