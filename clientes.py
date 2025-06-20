
import json
import os

ARCHIVO = 'Archivos-Json/clientes.json'

def cargar_datos():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, 'r', encoding='utf-8') as f:
        return json.load(f)

def guardar_datos(clientes):
    with open(ARCHIVO, 'w') as f:
        json.dump(clientes, f, indent=4)

def validar_dni(dni):
    if len(dni) < 7 or len(dni) > 8:
        return False
    return True


def validar_telefono(telefono):
     return  len(telefono) >=8


def validar_email(email):
    if "@" not in email:
        return False
    return True


def agregar_cliente(datos):
    clientes = cargar_datos()
    nuevo_id = max([c['id'] for c in clientes], default=0) + 1
    """ apellido = input("Apellido: ")
    nombre = input("Nombre: ") """

    #dni = input("DNI: ")
    while not validar_dni(datos['DNI']):
        return "DNI inválido. Debe tener entre 7 y 8 dígitos."
        dni = input("DNI: ")

    #telefono = input("Teléfono: ")
    while not validar_telefono(datos['Telefono']):
        return "Teléfono inválido "
        telefono = input("Teléfono: ")

    #email = input("Email: ")
    while not validar_email(datos['Email']):
        return "Email inválido."
        email = input("Email: ")

    #direccion = input("Dirección: ")
    #ciudad = input("Ciudad: ")
    #codigo_postal = input("Código Postal: ")
    #provincia = input("Provincia: ")
    #pais = input("País: ")

    clientes.append({
        'id': nuevo_id,
        'apellido': datos['Apellido'],
        'nombre': datos['Nombre'],
        'dni': datos['DNI'],
        'telefono': datos['Telefono'],
        'email': datos['Email'],
        'direccion': datos['Direccion'],
        'ciudad': datos['Ciudad'],
        'codigo_postal': datos['Codigo Postal'],
        'provincia': datos['Provincia'],
        'pais': datos['Pais']
    })

    guardar_datos(clientes)
    return True
    #print(" Cliente agregado exitosamente.\n")


def listar_clientes():
    clientes = cargar_datos()
    if not clientes:
        print(" No hay clientes registrados.\n")
        return
    for c in clientes:
        print(
            f"ID: {c['id']} | Apellido: {c['apellido']} | Nombre: {c['nombre']} | DNI: {c['dni']} "
            f"| Tel: {c['telefono']} | Email: {c['email']} | Dirección: {c['direccion']} | Ciudad: {c['ciudad']} | "
            f"Código Postal: {c['codigo_postal']} | Provincia: {c['provincia']} | País: {c['pais']}"
        )
    print()




def buscar_cliente():
    clientes = cargar_datos()
    termino = input("Buscar por nombre, apellido o DNI: ").lower()
    encontrados = [
        c for c in clientes
        if termino in c['nombre'].lower() or
           termino in c['apellido'].lower() or
           termino in c['dni']
    ]
    if not encontrados:
        print(" No se encontró ningún cliente.\n")
    else:
        for c in encontrados:
            print(
                f"ID: {c['id']} | Apellido: {c['apellido']} | Nombre: {c['nombre']} | DNI: {c['dni']} "
                f"| Tel: {c['telefono']} | Email: {c['email']} | Dirección: {c['direccion']}, {c['ciudad']}, "
                f"{c['codigo_postal']}, {c['provincia']}, {c['pais']}"
            )
        print()

def eliminar_cliente():
    clientes = cargar_datos()
    try:
        id_eliminar = int(input("Ingrese el ID del cliente a eliminar: "))
    except ValueError:
        print(" ID inválido.\n")
        return

    clientes_filtrados = [c for c in clientes if c['id'] != id_eliminar]
    if len(clientes) == len(clientes_filtrados):
        print(" No se encontró un cliente con ese ID.\n")
    else:
        guardar_datos(clientes_filtrados)
        print(" Cliente eliminado exitosamente.\n")

def menu():
    while True:
        print("=== Menú de Clientes ===")
        print("1. Agregar cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Eliminar cliente")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            agregar_cliente()
        elif opcion == '2':
            listar_clientes()
        elif opcion == '3':
            buscar_cliente()
        elif opcion == '4':
            eliminar_cliente()
        elif opcion == '5':
            print(" Saliendo del programa.")
            break
        else:
            print(" Opción inválida. Intente de nuevo.\n")

if __name__ == "__main__":
    menu()
