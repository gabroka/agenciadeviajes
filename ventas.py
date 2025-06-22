
import json
import os
from Clientes import cargar_datos_cliente as leer_clientes
from tabulate import tabulate
from datetime import datetime
import requests  # ==> Importo la biblioteca requests para poder hacer solicitudes HTTP a APIs externas


'''
Rutas a los archivos json:

'''
json_clientes = "Archivos-Json/clientes.json"
json_destinos = "Archivos-Json/destinos.json"
json_ventas = "Archivos-Json/ventas.json"

'''
Funciones responsables de obtener los datos desde los archivos JSON existentes

'''

def leer_destinos():
    if not os.path.exists(json_destinos):
        return []
    with open(json_destinos, "r", encoding='utf-8') as destinos:
        return json.load(destinos)

def leer_ventas():
    if not os.path.exists(json_ventas):
        return[]
    with open(json_ventas, 'r', encoding='utf-8') as ventas:
        return json.load(ventas)
    
'''
Funciones para guardar en los archivos json las modificaciones realizadas

'''
    
# Guarda las ventas en el archivo json de ventas
def guardar_ventas(ventas):
    with open(json_ventas, 'w', encoding='utf-8') as v:
        json.dump(ventas, v, indent=2)
    
# Guarda los destinos en el archivo json de destinos
def guardar_destinos(destinos):
    with open(json_destinos, 'w', encoding='utf-8') as d:
        json.dump(destinos, d, indent=2)
    
'''
Leo los datos guardados en los archivos json y los almaceno en variables para trabajar con ellos en el programa

'''
clientes = leer_clientes()
destinos = leer_destinos()
ventas = leer_ventas()


'''
Funciones auxiliares:

'''

# Busca cliente por su dni
def buscar_clienteDNI():
    dni = input("\nIngrese el DNI del cliente: ")
    global clientes
    for c in clientes:
        if c['dni'] == dni:
            print(f"\n✅ El cliente seleccionado es: {c['nombre'].title()} {c['apellido'].title()}\n")
            return c
    
    print("\n❌ Cliente no encontrado \n")
    return None


# Muestro una tabla con todos los destinos
def mostrar_destinos():
    tabla = []
    for d in destinos:
        fila = [d['id'], d['nombre'], f"$ {d['precio']}", d['disponibilidad']]
        tabla.append(fila)

    headers = ["Id", "Nombre", "Precio", "Disponiblidad"]

    print(tabulate(tabla, headers, tablefmt="fancy_grid"))



# Buscar destino por ID (y valida que ingrese un numero)
def buscar_destinoID():
    try:
        id = int(input("\nIngrese el ID del destino: "))
    except ValueError:
        print("\n❌ Error. Debe ingresar un numero entero\n")
        return None

    for d in destinos:
        if d['id'] == id:
            print(f"\n🏝️   El destino seleccionado es: {d['nombre']}")
            return d
    
    print("\n❌ Destino no encontrado\n")
    return None
        

'''
mostrar_clima_destino(nombre_destino) ==> Función para consultar y mostrar el clima actual de un destino turístico consultando a la API de wttr.in

'''

def mostrar_clima_destino(nombre_destino):
    try:
        # Construyo la URL de la API con el nombre del destino y en español
        url = f"https://wttr.in/{nombre_destino}?format=3&lang=es"

        # Hago la solicitud GET a la API y verifico que la solicitud sea exitosa
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            print(f"\n🌤️ Clima actual en {nombre_destino.title()}: {respuesta.text}")
        else:
            print(f"\n⚠️ No se pudo obtener el clima de {nombre_destino.title()}.")

        # Capturo si hubo un error cuando intento hacer la solicitud
    except:
        print(f"\n⚠️ Error al consultar el clima")



'''
registrar_venta ==> Funcion principal para registrar las ventas de destinos turisticos para un determinado cliente:

'''
def registrar_venta():

    cliente = buscar_clienteDNI()
    if cliente is None:
        return

    # Muestro todas las opciones de destinos para seleccionar por id
    print("🏝️   Los destinos disponibles son: \n")
    mostrar_destinos()

    destino = buscar_destinoID()
    if destino is None:
        return
    
    # Muestro el clima actual del destino seleccionado
    mostrar_clima_destino(destino['nombre'])

    
    # Si ingresa un valor distinto a un numero entero mostrara el error
    try:
        cantidad = int(input("\nIndique la cantidad de reservas: "))
    except ValueError:
        print("\n❌ Error. Debe ingresar un numero entero\n")
        return
    
    # Valido que haya suficientes lugares disponibles para la cantidad solicitada
    if cantidad > destino['disponibilidad']:
        print(f"\n❌ Lo sentimos, solo quedan {destino['disponibilidad']} lugares disponibles\n")
        return
    elif cantidad <= 0:
        print("❌ Cantidad invalida. Debe ingresar al menos 1 reserva")
        return

    # Calculo el precio total de la reserva despues de haber seleccionado la cantidad
    total = cantidad * destino["precio"]

    # Actualizo la cantidad de lugares disponibles en el diccionario
    destino['disponibilidad'] -= cantidad
    # Guardo los cambios en el json destinos
    guardar_destinos(destinos)
    print("\n📋 Archivo de destinos actualizado con éxito.")



    # Fecha actual en formato dd/mm/yyyy
    fecha_venta = datetime.today().strftime("%d/%m/%Y")

    # Establezco el id de la venta
    if not ventas:
        id = 1
    else:
        id = max(v['id'] for v in ventas) + 1

    # Registrar la venta
    nueva_venta = {
        "id": id,
        "id_cliente": cliente["id"],
        "id_destino": destino["id"],
        "cantidad": cantidad,
        "total": total,
        "fecha": fecha_venta
    }

    # Agrego la venta realizada al diccionario
    ventas.append(nueva_venta)

    # Guardo los cambios en el archivo json de ventas
    guardar_ventas(ventas)

    print("\n✅ Venta registrada con éxito! 🎉\n")

    print(f"""
    📑 Informe de la venta realizada: \n
        ID: {id}
        Cliente: {cliente['nombre'].title()} {cliente['apellido'].title()}
        Destino: {destino['nombre']}
        Cantidad: {cantidad}
        Total: $ {total}
        Fecha de venta: {fecha_venta}
        """)



'''
Permite ejecutar esta funcion directamente desde este archivo y evita que se ejecute automáticamente si lo importo desde otro módulo (menu)

'''

if __name__ == "__main__":
    registrar_venta()

