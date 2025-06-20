'''

Menu de opciones e interaccion con el usuario

'''
import tkinter as tk
from estadisticas_2 import estadisticas

def configurar_boton(boton):
    boton.configure(
        width=20,
        height=1,
        #bg="lightblue",  # Color de fondo (opcional)
        font=("Arial", 15)  # Fuente (opcional)
    )


ventana= tk.Tk()
ventana.geometry('800x800')

#========== definicion de los marcos ===========#
marco_abm_clientes= tk.LabelFrame(ventana)
marco_abm_clientes.configure(text='ABM Clientes', padx=5, pady=5)

marco_abm_destinos= tk.LabelFrame(ventana)
marco_abm_destinos.configure(text='ABM Destinos', padx=5, pady=5)

marco_abm_ventas= tk.LabelFrame(ventana)
marco_abm_ventas.configure(text='ABM Ventas', padx=5, pady=5)

marco_abm_estadisticas= tk.LabelFrame(ventana)
marco_abm_estadisticas.configure(text='ABM Estadisticas', padx=5, pady=5)


#========== botones del marco clientes ===========#
btn_nvo_cliente= tk.Button(marco_abm_clientes, text='Nuevo Cliente')
configurar_boton(btn_nvo_cliente)
btn_listar_cliente= tk.Button(marco_abm_clientes, text='Listar Clientes')
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
marco_abm_clientes.pack()
marco_abm_destinos.pack()
marco_abm_ventas.pack()
marco_abm_estadisticas.pack()




ventana.mainloop()