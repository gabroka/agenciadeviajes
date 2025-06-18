'''

Destinos mas vendidos, menos vendidos, etc


'''
import os
from datetime import datetime
import os.path
import json
from tabulate import tabulate


def clienteById(id:int)->str: #devuelve nombre y apellido del cliente con el id cliente
    nombreClientes="Archivos-Json/clientes.json"
    with open(nombreClientes,"rt",encoding='utf-8') as open_clientes:
        clientes=json.load(open_clientes)
        for cliente in clientes:
            if cliente.get("id") == id:
                return f'{cliente.get('nombre')} {cliente.get('apellido')}'
            
def dniById(id:int)->int: #devuelve dni del cliente con el id cliente
    nombreClientes="Archivos-Json/clientes.json"
    with open(nombreClientes,"rt",encoding='utf-8') as open_clientes:
        clientes=json.load(open_clientes)
        for cliente in clientes:
            if cliente.get("id") == id:
                return f'{cliente.get('dni')}'

def destinoById(id:int)->str: #devuelve nombre del destino con el id destino
    nombreDestinos="Archivos-Json/destinos.json"
    with open(nombreDestinos,"rt",encoding='utf-8') as open_destinos:
        destinos=json.load(open_destinos)
        for destino in destinos:
            if destino.get("id") == id:
                return f'{destino.get('nombre')}'

def mostrarVta(listaVta):
    for lista in listaVta:
        lista['id_cliente']= clienteById(lista['id_cliente'])
        lista['id_destino']=destinoById(lista['id_destino'])

    print(tabulate(lista, headers='keys'))
    """ for lista in listaVta:
        print (f'cliente: {clienteById(lista['id_cliente'])}')
        print(f'dni: {dniById(lista['id_cliente'])} ')
        print(f'destino: {destinoById(lista['id_destino'])}')
        print(f'cantidad: {lista['cantidad']}')
        print(f'total: {lista['total']}')
        print(f'fecha de venta: {lista['fecha']}')
        print('\n') """

def ventasPorPeriodo():
    os.system('cls') #limpia la pantalla
    print("elija el periodo")
    i=True
    while i:
        try:
            perInicial=input("indique dia mes y año inicio en la forma dd/mm/yyyy: ")
            perInicialDT=datetime.strptime(perInicial, "%d/%m/%Y") #cambia la fecha a datetime
                    
            perFinal=input("indique dia mes y año fin en la forma dd/mm/yyyy: ")
            perFinalDT=datetime.strptime(perFinal, "%d/%m/%Y") #cambia la fecha a datetime
            i=False
        except Exception:
            os.system('cls')
            print("Error: ingrese la fecha en el formato indicado")

    print('\n')
    nombreJson = "Archivos-json/ventas.json" #guarda la ruta al archivo ventas.json
    #nombreJson = "Archivos-json/prueba.json"
    listaVta=[]
    if os.path.exists(nombreJson): #verifica si existe ventas.json
        open_ventas=open(nombreJson,"rt",encoding='utf-8') #abre ventas.json
        ventasDic=json.load(open_ventas) # guarda ventas.json como diccionario
        for venta in ventasDic: #recorre los elementos buscando y guardando los que esten entre la fecha inicio y fin que ingresó el usuario
            fechaVentaDT=datetime.strptime(venta.get("fecha"), "%d/%m/%Y")
            #print(type(fechaDT))
            if fechaVentaDT > perInicialDT and perFinalDT > fechaVentaDT:
                listaVta.append(venta)
        mostrarVta(listaVta)
        open_ventas.close()
    else:
        print("no existe el archivo ventas.json")
            


def destinos():
    os.system('cls') #limpia la pantalla
    print('indique la fecha para la busqueda')
    i=True
    while i:
        try:
            fechaInicio=input('fecha inicial en la forma dd/mm/yyyy: ')
            fechaInicioDT=datetime.strptime(fechaInicio, "%d/%m/%Y")
            fechaFin=input('fecha final en la forma dd/mm/yyyy: ')
            fechaFinDT=datetime.strptime(fechaFin, "%d/%m/%Y")
            i=False
        except Exception:
            os.system('cls')
            print("Error: ingrese la fecha en el formato indicado")
    print('\n')
    destinosjson="Archivos-json/destinos.json"
    with open (destinosjson, 'r',encoding='utf-8') as destinos:
        destinoDic=json.load(destinos)
    listaIdDestino=[]
    
    for destinoId in destinoDic:
        listaIdDestino.append(destinoId.get('id'))
    
    ventasJson = "Archivos-json/ventas.json"
    masVendido = {}
    for lista in listaIdDestino:
        masVendido[lista]= 0
    if os.path.exists(ventasJson): #verifica si existe ventas.json
        open_ventas=open(ventasJson,"rt") #abre ventas.json
        ventasDic=json.load(open_ventas) # guarda ventas.json como diccionario
        
        for venta in ventasDic: #recorre las ventas, armando una lista de los mas vendidos
            fechaVtaDT=datetime.strptime(venta['fecha'], "%d/%m/%Y")
            if  fechaVtaDT > fechaInicioDT and fechaFinDT > fechaVtaDT:
                for idDestino in listaIdDestino:
                   if idDestino == venta.get('id_destino'):
                       masVendido[idDestino] += venta.get('cantidad')
        open_ventas.close()
        return masVendido        
    else:
        print('no existe el archivo ventas.json')            

def destinosMasVendidos():
    masVendido = destinos()
    for item in dict(sorted(masVendido.items(), key=lambda item: item[1], reverse=True)):
            print(f'el destino {destinoById(item)} se vendio {masVendido[item]} veces')

def destinosMenosVendidos():
    menosVendido = destinos()
    for item in dict(sorted(menosVendido.items(), key=lambda item: item[1], reverse=False)):
            print(f'el destino {destinoById(item)} se vendio {menosVendido[item]} veces')

def ventasDeUnDestino():
    #tomar las ventas y sumar las que correspondan al destino elegido
    os.system('cls')
    nombreDestinos="Archivos-Json/destinos.json"
    with open(nombreDestinos,"rt",encoding='utf-8') as open_destinos:
        destinos=json.load(open_destinos)
    print('\n')
    #valida que se ingrese una opcion valida
    f=True
    i=True
    while f:
        try:
            while i:
                print("a continuacion tiene la lista de destinos disponible, elija su opcion para mostrar la cantidad vendida")
                for destino in destinos:
                        print(f'{destino.get('id')}-{destino.get('nombre')}')
                idDestino = int(input("ingrese su opcion: "))
                f=False
                
                if idDestino > 0 and idDestino <= destinos[len(destinos)-1]['id']:
                    i=False
                else:
                    os.system('cls')
                    print('elija una entre las opciones disponibles')
        except Exception:
            os.system('cls')
            print('elija una opcion valida')

    ventasJson = "Archivos-json/ventas.json"
    if os.path.exists(ventasJson): #verifica si existe ventas.json
        open_ventas=open(ventasJson,"rt") #abre ventas.json
        ventasDic=json.load(open_ventas) # guarda ventas.json como diccionario
        open_ventas.close()
        contarDestinos=0
        for venta in ventasDic:
            if venta.get('id_destino') == idDestino:
                contarDestinos += venta.get('cantidad')
        print(f'el destino {destinoById(idDestino)} se han vendido {contarDestinos} lugares')
    else:
         print("no existe el archivo ventas.json")


def estadisticas():
    os.system('cls')
    i=True
    #f=True
    #while f:
        #try:
    while i:
                print("=========================================")
                print("1-Ventas por periodo")
                print("2-destinos mas vendidos")
                print("3-destinos menos vendidos")
                print("4-ventas de un destino")
                print("0-volver al menu anterior")
                opcion=int(input("elija su opcion: "))
                match opcion:
                    case 1:
                        ventasPorPeriodo()
                    
                    case 2:
                        destinosMasVendidos()
                    
                    case 3:
                        destinosMenosVendidos()
                    
                    case 4:
                        ventasDeUnDestino()
                    
                    case 0:
                        i=False
                    case _:
                        print("elija una opcion valida")
                f=False        
            #except Exception:
            #os.system('cls')
            #print('debe seleccionar una opcion valida try del menu')         
