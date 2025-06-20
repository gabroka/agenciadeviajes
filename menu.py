
import tkinter as tk
from estadisticas import estadisticas
from tkinter import messagebox
from Clientes import agregar_cliente
from Clientes import cargar_datos
from tkinter import ttk



def configurar_boton(boton):
    boton.configure(
        width=20,
        height=1,
        #bg="lightblue",  # Color de fondo (opcional)
        font=("Arial", 15)  # Fuente (opcional)
    )

def crear_nuevo_cliente(datos):
    valores = {k: v.get() for k, v in datos.items()}
    resultado = agregar_cliente(valores)
    if resultado == True:
        messagebox.showinfo("Información", "Operación completada con éxito.")
    else:
        messagebox.showerror('Error',resultado)

def NvoCliente():
    camposDatos=['Nombre', 'Apellido', 'DNI', 'Telefono','Email','Direccion', 'Ciudad', 'Codigo Postal', 'Provincia', 'Pais']
    vars_entrada = {campo: tk.StringVar() for campo in camposDatos}

    #========== definicion de la ventana de nuevo cliente ===========#
    ventana_clientes = tk.Toplevel(ventana)
    ventana_clientes.geometry('400x500+800+120')

    #========== definicion del marco para ingreso de nuevos datos ===========#
    nvo_cliente_marco= tk.LabelFrame(ventana_clientes, text=' Nuevo Cliente')
    nvo_cliente_marco.configure(padx=5, pady=5, width=500, height=200)
    nvo_cliente_marco.pack(side='top')
    
    #========== definicion de entrada de datos ===========#
    row=0
    for campo in camposDatos:
        tk.Label(nvo_cliente_marco, text=f"{campo}:").grid(row=row,column=0,padx=5, pady=5)
        tk.Entry(nvo_cliente_marco, textvariable=vars_entrada[campo]).grid(row=row,column=1,padx=5, pady=5)
        row += 1

    #========== boton crear nuevo cliente ===========#
    btn_crear_nuevo_cliente= tk.Button(ventana_clientes, text='Crear Nuevo Cliente', command=lambda: crear_nuevo_cliente(vars_entrada)).pack()

    #========== boton cerrar ===========#
    btn_cerrar= tk.Button(ventana_clientes, text='Cerrar', command= ventana_clientes.destroy).pack(side='top')
    
def listar_clientes():  
    ventana_listar_clientes= tk.Toplevel(ventana)
    ventana_listar_clientes.geometry('1200x500+100+120')
    clientes = cargar_datos()
    tree_frame = tk.LabelFrame(ventana_listar_clientes, text="Lista de Clientes", padx=10, pady=10)
    tree_frame.pack(pady=10, padx=10, fill="both", expand=True)

    tree = ttk.Treeview(tree_frame, columns=("ID", "Nombre", "Apellido",'DNI','Telefono','Email', 'Direccion','Ciudad','Codigo Postal','Provincia','Pais'), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Apellido", text="Apellido")
    tree.heading("DNI", text="DNI")
    tree.heading("Telefono", text="Telefono")
    tree.heading("Email", text="Email")
    tree.heading("Direccion", text="Direccion")
    tree.heading("Ciudad", text="Ciudad")
    tree.heading("Codigo Postal", text="Codigo Postal")
    tree.heading("Provincia", text="Provincia")
    tree.heading("Pais", text="Pais")

    tree.column("ID", width=30, anchor="center")
    tree.column("Nombre", width=100, anchor="center")
    tree.column("Apellido", width=100, anchor="center")
    tree.column("DNI", width=50, anchor="center")
    tree.column("Telefono", width=100, anchor="center")
    tree.column("Email", width=200, anchor="center")
    tree.column("Direccion", width=100, anchor="center")
    tree.column("Ciudad", width=100, anchor="center")
    tree.column("Codigo Postal", width=100, anchor="center")
    tree.column("Provincia", width=100, anchor="center")
    tree.column("Pais", width=100, anchor='center')

    tree.pack(fill="both", expand=True)
    for c in clientes:
        tree.insert("", "end", values=(c['id'], c["nombre"], c["apellido"],  c["dni"],c["telefono"], c["email"], c["direccion"], c["ciudad"], c["codigo_postal"], c["provincia"], c["pais"]))
    #tree.bind("<<TreeviewSelect>>", load_selected_product)

def otros():
    ventana_listar_clientes= tk.Toplevel(ventana)
    ventana_listar_clientes.geometry('400x500+800+120') 
    camposDatos=['Nombre', 'Apellido', 'DNI', 'Telefono','Email','Direccion', 'Ciudad', 'Codigo Postal', 'Provincia', 'Pais']  
    vars_entrada = {campo: tk.StringVar() for campo in camposDatos} 

    listar_cliente_marco= tk.LabelFrame(ventana_listar_clientes, text='Listar Clientes')
    listar_cliente_marco.configure(padx=5, pady=5, width=500, height=200)
    listar_cliente_marco.pack(side='top')

    row=0
    for campo in camposDatos:
        tk.Label(listar_cliente_marco, text=f"{campo}:").grid(row=row,column=0,padx=5, pady=5)
        tk.Entry(listar_cliente_marco, textvariable=vars_entrada[campo]).grid(row=row,column=1,padx=5, pady=5)
        row += 1

ventana= tk.Tk()
ventana.geometry('600x430')

#========== definicion de los marcos ===========#
marco_abm_clientes= tk.LabelFrame(ventana)
marco_abm_clientes.configure(text='ABM Clientes', padx=5, pady=5)

marco_abm_destinos= tk.LabelFrame(ventana)
marco_abm_destinos.configure(text='ABM Destinos', padx=5, pady=5)

marco_abm_ventas= tk.LabelFrame(ventana)
marco_abm_ventas.configure(text='Ventas', padx=5, pady=5)

marco_abm_estadisticas= tk.LabelFrame(ventana)
marco_abm_estadisticas.configure(text='ABM Estadisticas', padx=5, pady=5)

#========== botones del marco clientes ===========#
btn_nvo_cliente= tk.Button(marco_abm_clientes, text='Nuevo Cliente', command=NvoCliente)
configurar_boton(btn_nvo_cliente)
btn_listar_cliente= tk.Button(marco_abm_clientes, text='Listar Clientes', command=listar_clientes)
configurar_boton(btn_listar_cliente)
btn_find_cliente= tk.Button(marco_abm_clientes, text='Buscar Cliente')
configurar_boton(btn_find_cliente)
btn_eliminar_cliente= tk.Button(marco_abm_clientes, text='Eliminar Cliente')
configurar_boton(btn_eliminar_cliente)

#========== botones del marco destinos ===========#
btn_nvo_destino= tk.Button(marco_abm_destinos, text='Nuevo Destino')
configurar_boton(btn_nvo_destino)
btn_listar_destino= tk.Button(marco_abm_destinos, text='Listar Destino')
configurar_boton(btn_listar_destino)
btn_find_destino= tk.Button(marco_abm_destinos, text='Buscar Destino')
configurar_boton(btn_find_destino)
btn_eliminar_destino= tk.Button(marco_abm_destinos, text='Eliminar Destino')
configurar_boton(btn_eliminar_destino)

#========== botones del marco ventas ===========#
btn_nva_venta= tk.Button(marco_abm_ventas, text='Nueva Venta')
configurar_boton(btn_nva_venta)

#========== botones del marco estadisticas ===========#
btn_venta_por_periodo= tk.Button(marco_abm_estadisticas, text='Venta De Un Periodo')
configurar_boton(btn_venta_por_periodo)
btn_mas_vendido= tk.Button(marco_abm_estadisticas, text='Destino Mas Vendido')
configurar_boton(btn_mas_vendido)
btn_menos_vendido= tk.Button(marco_abm_estadisticas, text='Destino Menos Vendido')
configurar_boton(btn_menos_vendido)
btn_vta_de_un_destino= tk.Button(marco_abm_estadisticas, text='Venta De Un Destino')
configurar_boton(btn_vta_de_un_destino)

#========== inicializa los botones ===========#
btn_nvo_cliente.grid(row=0,column=0)
btn_listar_cliente.grid(row=1,column=0)
btn_find_cliente.grid(row=0,column=1)
btn_eliminar_cliente.grid(row=1,column=1)

btn_nva_venta.grid(row=0,column=0)

btn_nvo_destino.grid(row=0,column=0)
btn_listar_destino.grid(row=1,column=0)
btn_find_destino.grid(row=0,column=1)
btn_eliminar_destino.grid(row=1,column=1)

btn_venta_por_periodo.grid(row=0,column=0)
btn_mas_vendido.grid(row=0,column=1)
btn_menos_vendido.grid(row=1,column=0)
btn_vta_de_un_destino.grid(row=1,column=1)

#========== inicializa los marcos ===========#
marco_abm_clientes.pack(pady=5)
marco_abm_destinos.pack(pady=5)
marco_abm_ventas.pack(pady=5)
marco_abm_estadisticas.pack(pady=5)




ventana.mainloop()