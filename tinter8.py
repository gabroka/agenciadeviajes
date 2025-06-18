import tkinter as tk

ventana= tk.Tk()
decimal= tk.DoubleVar(value=3.14)

control_deslizante = tk.Scale(ventana, variable=decimal, from_=0, to=20, resolution=0.1, orient=tk.HORIZONTAL)
control_deslizante.pack()


ventana.mainloop()