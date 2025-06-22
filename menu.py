
import tkinter as tk
from estadisticas import estadisticas
from tkinter import messagebox
from Clientes import agregar_cliente
from Clientes import cargar_datos_cliente
from Clientes import guardar_datos
from Clientes import eliminar_cliente
from destinos import agregar_destino
from destinos import cargar_destinos
from destinos import guardar_destinos
from destinos import eliminar_destino_tk
from tkinter import ttk

#========== configura los botones de menu ===========#
def configurar_boton(boton):
    boton.configure(
        width=20,
        height=1,
        #bg="lightblue",  # Color de fondo (opcional)
        font=("Arial", 15)  # Fuente (opcional)
    )
#========== fin ===========#

#================================ abm clientes ==============================================#
#========== crear nuevo cliente ===========#
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
    #========== crear nuevo cliente ===========#
#========== FIN crear nuevo cliente ===========#

#========== listar cliente ===========#
def ListarClientes():  
    ventana_listar_clientes= tk.Toplevel(ventana)
    ventana_listar_clientes.geometry('1200x500+100+120')
    clientes = cargar_datos_cliente()
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
#========== fin listar cliente ===========#

#========== buscar cliente y modificar ===========#
def MuestraCliente(vars,campo,*event):
    global cliente_encontrado
    clientes=cargar_datos_cliente()
    if campo == 'id' and vars['id'].get() and vars['id'].get() != '0':
        for c in clientes:
            if int(vars[campo].get()) and c.get('id') == int(vars[campo].get()):
                cliente_encontrado= c
                cliente_encontrado_strvar.set('1')
                break
    else:
        if campo == 'dni' and vars['dni'].get() and vars['dni'].get() != '0':
            for c in clientes:
                if c.get('dni') == vars[campo].get():
                    cliente_encontrado = c
                    cliente_encontrado_strvar.set('1')
                    break
        

def MostrarClienteEncontrado(*args):
    if cliente_encontrado_strvar.get() != '0': 
        for campo in vars_cliente_encontrado:
            vars_cliente_encontrado[campo].set(cliente_encontrado[campo]) 
        cliente_encontrado_strvar.set('0')
    
def GuardarCliente(vars, id, *args):
    clientes=cargar_datos_cliente()
    cliente={'id':id}
    for campo, var in vars.items():
        cliente[campo] = var.get()
    
    nuevos_datos=[]
    for i in clientes:
        if i['id'] == id:
            nuevos_datos.append(cliente)
        else:
            nuevos_datos.append(i)
    guardar_datos(nuevos_datos)
    messagebox.showinfo('Exito',f'El cliente {cliente['nombre']} {cliente['apellido']} se ha actualizado con exito')

def BuscarCliente():
    ventana_buscar_clientes= tk.Toplevel(ventana)
    ventana_buscar_clientes.geometry('400x500+800+120') 
    camposDatos=['id', 'dni'] 
    global cliente_encontrado
    global cliente_encontrado_strvar
    global vars_cliente_encontrado
    cliente_encontrado_strvar= tk.StringVar(value='0')

    vars_cliente_encontrado={}
    cliente_encontrado = {} 
    vars_entrada = {campo: tk.StringVar(value='0') for campo in camposDatos} 
    listar_cliente_marco= tk.LabelFrame(ventana_buscar_clientes, text='Listar Clientes')
    listar_cliente_marco.configure(padx=5, pady=5, width=500, height=200)
    listar_cliente_marco.pack(side='top')

    row=0
    for campo in camposDatos:
        tk.Label(listar_cliente_marco, text=f"{campo}:").grid(row=row,column=0,padx=5, pady=5)
        tk.Entry(listar_cliente_marco, textvariable=vars_entrada[campo]).grid(row=row,column=1,padx=5, pady=5)
        row += 1
        
    for campo, var  in vars_entrada.items():
        var.trace_add("write", lambda *args, campo=campo : MuestraCliente(vars_entrada,campo, *args))
    
    cliente_encontrado_strvar.trace_add('write', MostrarClienteEncontrado)

    marco_busqueda= tk.LabelFrame(ventana_buscar_clientes, text='cliente encontrado')
    marco_busqueda.config(width=100,height=100)
    marco_busqueda.pack()
    datos=['apellido','nombre','dni','telefono','email','direccion','ciudad','codigo_postal','provincia','pais']
    vars_cliente_encontrado={k: tk.StringVar(value='0') for k in datos}
    row=0
    for i in datos:
        tk.Label(marco_busqueda, text=f'{i}').grid(row=row,column=0)
        tk.Entry(marco_busqueda, width=20, textvariable=vars_cliente_encontrado[i]).grid(row=row,column=1)
        row += 1
    
    btn_guardar = tk.Button(
        ventana_buscar_clientes,
        text="Guardar Cambios",
        command=lambda var=vars_cliente_encontrado.copy(): GuardarCliente(var, cliente_encontrado['id']))
    btn_guardar.pack(pady=10)
    
#========== FIN buscar cliente y modificar ===========#

#========== eliminar cliente ===========#
def FuncionParaEliminarCliente(tree):
    item_seleccionado = tree.focus()
    #print(item_seleccionado)
    if not item_seleccionado:
        messagebox.showwarning("Advertencia", "Selecciona un producto para eliminar.")
        return
    id_eliminar=tree.item(item_seleccionado, "values")[0]
    
    resultado=eliminar_cliente(int(id_eliminar))
    if resultado:
        messagebox.showinfo('Exito'," Cliente eliminado exitosamente.")
        clientes=cargar_datos_cliente()
        for item in tree.get_children():
            tree.delete(item)
        for c in clientes:
            tree.insert("", "end", values=(c['id'], c["nombre"], c["apellido"],  c["dni"],c["telefono"], c["email"], c["direccion"], c["ciudad"], c["codigo_postal"], c["provincia"], c["pais"]))
    else:
        messagebox.showerror('Error',resultado)


def EliminarCliente():
    ventana_eliminar_clientes= tk.Toplevel(ventana)
    ventana_eliminar_clientes.geometry('1200x500+100+120')
    clientes = cargar_datos_cliente()
    tree_frame = tk.LabelFrame(ventana_eliminar_clientes, text="Lista de Clientes", padx=10, pady=10)
    tree_frame.pack(pady=10, padx=10, fill="both", expand=True)

    datos=["ID", "Nombre", "Apellido",'DNI','Telefono','Email', 'Direccion','Ciudad','Codigo Postal','Provincia','Pais']
    tree = ttk.Treeview(tree_frame, columns=("ID", "Nombre", "Apellido",'DNI','Telefono','Email', 'Direccion','Ciudad','Codigo Postal','Provincia','Pais'), show="headings")
    for i in datos:
        tree.heading(i, text=i)
    
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
    boton_confirmar= tk.Button(ventana_eliminar_clientes, text='Eliminar Cliente', padx=5, pady=5, command=lambda tree=tree: FuncionParaEliminarCliente(tree)).pack()
    for c in clientes:
        tree.insert("", "end", values=(c['id'], c["nombre"], c["apellido"],  c["dni"],c["telefono"], c["email"], c["direccion"], c["ciudad"], c["codigo_postal"], c["provincia"], c["pais"]))
#========== FIN eliminar cliente ===========#
#================================ FIN abm clientes ==========================================#

#================================ abm destinos ==============================================#
#========== crear nuevo destino ===========#
def CrearNuevoDestino(datos):
    valores = {k: v.get() for k, v in datos.items()}
    resultado = agregar_destino(valores)
    if resultado == True:
        messagebox.showinfo("Información", "Operación completada con éxito.")
    else:
        messagebox.showerror('Error',resultado)

def NuevoDestino():
    camposDatos=['Nombre', 'Precio', 'Disponibilidad']
    vars_entrada = {campo: tk.StringVar() for campo in camposDatos}

    #========== definicion de la ventana de nuevo destino ===========#
    ventana_destinos = tk.Toplevel(ventana)
    ventana_destinos.geometry('400x500+800+120')

    #========== definicion del marco para ingreso de nuevos datos ===========#
    nvo_destino_marco= tk.LabelFrame(ventana_destinos, text=' Nuevo Destino')
    nvo_destino_marco.configure(padx=5, pady=5, width=500, height=200)
    nvo_destino_marco.pack(side='top')
    
    #========== definicion de entrada de datos ===========#
    row=0
    for campo in camposDatos:
        tk.Label(nvo_destino_marco, text=f"{campo}:").grid(row=row,column=0,padx=5, pady=5)
        tk.Entry(nvo_destino_marco, textvariable=vars_entrada[campo]).grid(row=row,column=1,padx=5, pady=5)
        row += 1

    #========== boton crear nuevo destino ===========#
    btn_crear_nuevo_destino= tk.Button(ventana_destinos, text='Crear Nuevo Destino', command=lambda: CrearNuevoDestino(vars_entrada)).pack()

    #========== boton cerrar ===========#
    btn_cerrar= tk.Button(ventana_destinos, text='Cerrar', command= ventana_destinos.destroy).pack(side='top')
#========== FIN crear nuevo destino ===========#

#========== listar destinos ===========#
def ListarDestinos():
    ventana_listar_destinos= tk.Toplevel(ventana)
    ventana_listar_destinos.geometry('800x500+100+120')
    destinos = cargar_destinos()
    tree_frame = tk.LabelFrame(ventana_listar_destinos, text="Lista de Destinos", padx=10, pady=10)
    tree_frame.pack(pady=10, padx=10, fill="both", expand=True)

    tree = ttk.Treeview(tree_frame, columns=("ID", "Nombre", "Precio",'Disponibilidad'), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Precio", text="Precio")
    tree.heading("Disponibilidad", text="Disponibilidad")
    

    tree.column("ID", width=30, anchor="center")
    tree.column("Nombre", width=100, anchor="center")
    tree.column("Precio", width=100, anchor="center")
    tree.column("Disponibilidad", width=50, anchor="center")
    
    tree.pack(fill="both", expand=True)
    for c in destinos:
        tree.insert("", "end", values=(c['id'], c["nombre"], c["precio"],  c["disponibilidad"]))
#========== FIN listar destinos ===========#

#========== buscar destinos y modificar ===========#
def MuestraDestino(vars,campo,*event):
    global destino_encontrado
    destinos=cargar_destinos()
    if campo == 'id' and vars['id'].get() and vars['id'].get() != '0':
        for c in destinos:
            if int(vars[campo].get()) and c.get('id') == int(vars[campo].get()):
                destino_encontrado= c
                destino_encontrado_strvar.set('1')
                break
    else:
        if campo == 'nombre' and vars['nombre'].get() and vars['nombre'].get() != '0':
            for c in destinos:
                #print("c.get('nombre'): ",type(c.get('nombre')),"-vars[campo].get(): ",type(vars[campo].get()))
                if c.get('nombre') is not None and (c.get('nombre')).lower() == (vars[campo].get()).lower():
                    destino_encontrado = c
                    destino_encontrado_strvar.set('1')
                    break
        
def MostrarDestinoEncontrado(*args):
    if destino_encontrado_strvar.get() != '0': 
        for campo in vars_destino_encontrado:
            vars_destino_encontrado[campo].set(destino_encontrado[campo]) 
        destino_encontrado_strvar.set('0')
    
def GuardarDestino(vars, id, *args):
    destinos=cargar_destinos()
    destino={'id':id}
    for campo, var in vars.items():
        destino[campo] = var.get()
    
    nuevos_datos=[]
    for i in destinos:
        if i['id'] == id:
            nuevos_datos.append(destino)
        else:
            nuevos_datos.append(i)
    guardar_destinos(nuevos_datos)
    messagebox.showinfo('Exito',f'El destino {destino['nombre']} se ha actualizado con exito')

def BuscarDestino():
    ventana_buscar_destinos= tk.Toplevel(ventana)
    ventana_buscar_destinos.geometry('400x500+800+120') 
    camposDatos=['id', 'nombre'] 
    global destino_encontrado
    global destino_encontrado_strvar
    global vars_destino_encontrado
    destino_encontrado_strvar= tk.StringVar(value='0')

    vars_destino_encontrado={}
    destino_encontrado = {} 
    vars_entrada = {campo: tk.StringVar(value='0') for campo in camposDatos} 
    listar_destino_marco= tk.LabelFrame(ventana_buscar_destinos, text='Listar Destinos')
    listar_destino_marco.configure(padx=5, pady=5, width=500, height=200)
    listar_destino_marco.pack(side='top')

    row=0
    for campo in camposDatos:
        tk.Label(listar_destino_marco, text=f"{campo}:").grid(row=row,column=0,padx=5, pady=5)
        tk.Entry(listar_destino_marco, textvariable=vars_entrada[campo]).grid(row=row,column=1,padx=5, pady=5)
        row += 1
        
    for campo, var  in vars_entrada.items():
        var.trace_add("write", lambda *args, campo=campo : MuestraDestino(vars_entrada,campo, *args))
    
    destino_encontrado_strvar.trace_add('write', MostrarDestinoEncontrado)

    marco_busqueda= tk.LabelFrame(ventana_buscar_destinos, text='Destino Encontrado')
    marco_busqueda.config(width=100,height=100)
    marco_busqueda.pack()
    datos=['nombre','precio','disponibilidad']
    vars_destino_encontrado={k: tk.StringVar(value='0') for k in datos}
    row=0
    for i in datos:
        tk.Label(marco_busqueda, text=f'{i}').grid(row=row,column=0)
        tk.Entry(marco_busqueda, width=20, textvariable=vars_destino_encontrado[i]).grid(row=row,column=1)
        row += 1
    
    btn_guardar = tk.Button(
        ventana_buscar_destinos,
        text="Guardar Cambios",
        command=lambda var=vars_destino_encontrado.copy(): GuardarDestino(var, destino_encontrado['id']))
    btn_guardar.pack(pady=10)
    
#========== FIN buscar destinos y modificar ===========#

#========== eliminar destinos ===========#

def FuncionParaEliminarDestino(tree):
    item_seleccionado = tree.focus()
    #print(item_seleccionado)
    if not item_seleccionado:
        messagebox.showwarning("Advertencia", "Selecciona un producto para eliminar.")
        return
    id_eliminar=tree.item(item_seleccionado, "values")[0]
    
    resultado=eliminar_destino_tk(int(id_eliminar))
    if resultado:
        messagebox.showinfo('Exito'," Cliente eliminado exitosamente.")
        destinos=cargar_destinos()
        for item in tree.get_children():
            tree.delete(item)
        for c in destinos:
            tree.insert("", "end", values=(c['id'], c["nombre"], c["disponibilidad"]))
    else:
        messagebox.showerror('Error',resultado)


def EliminarDestino():
    ventana_eliminar_destino= tk.Toplevel(ventana)
    ventana_eliminar_destino.geometry('1200x500+100+120')
    destinos = cargar_destinos()
    tree_frame = tk.LabelFrame(ventana_eliminar_destino, text="Lista de Destino", padx=10, pady=10)
    tree_frame.pack(pady=10, padx=10, fill="both", expand=True)

    datos=["ID", "Nombre","Disponibilidad"]
    tree_eliminar_destino = ttk.Treeview(tree_frame, columns=("ID", "Nombre", "Disponibilidad"), show="headings")
    for i in datos:
        tree_eliminar_destino.heading(i, text=i)
    
    tree_eliminar_destino.column("ID", width=30, anchor="center")
    tree_eliminar_destino.column("Nombre", width=100, anchor="center")
    tree_eliminar_destino.column("Disponibilidad", width=100, anchor="center")
    

    tree_eliminar_destino.pack(fill="both", expand=True)
    boton_confirmar= tk.Button(ventana_eliminar_destino, text='Eliminar Destino', padx=5, pady=5, command=lambda tree=tree_eliminar_destino: FuncionParaEliminarDestino(tree)).pack()
    for c in destinos:
        tree_eliminar_destino.insert("", "end", values=(c['id'], c["nombre"], c["disponibilidad"]))
#========== FIN eliminar destinos ===========#

#================================ FIN abm destinos ==========================================#

#================================ ventas ====================================================#


#================================ FIN ventas ================================================#
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
btn_listar_cliente= tk.Button(marco_abm_clientes, text='Listar Clientes', command=ListarClientes)
configurar_boton(btn_listar_cliente)
btn_find_cliente= tk.Button(marco_abm_clientes, text='Buscar Cliente', command=BuscarCliente)
configurar_boton(btn_find_cliente)
btn_eliminar_cliente= tk.Button(marco_abm_clientes, text='Eliminar Cliente', command=EliminarCliente)
configurar_boton(btn_eliminar_cliente)

#========== botones del marco destinos ===========#
btn_nvo_destino= tk.Button(marco_abm_destinos, text='Nuevo Destino', command=NuevoDestino)
configurar_boton(btn_nvo_destino)
btn_listar_destino= tk.Button(marco_abm_destinos, text='Listar Destino', command=ListarDestinos)
configurar_boton(btn_listar_destino)
btn_find_destino= tk.Button(marco_abm_destinos, text='Buscar Destino', command=BuscarDestino)
configurar_boton(btn_find_destino)
btn_eliminar_destino= tk.Button(marco_abm_destinos, text='Eliminar Destino', command= EliminarDestino)
configurar_boton(btn_eliminar_destino)

#========== botones del marco ventas ===========#
btn_nva_venta= tk.Button(marco_abm_ventas, text='Nueva Venta', command=ventas)
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