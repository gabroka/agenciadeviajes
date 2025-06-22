import json
import os

ARCHIVO_DATOS = 'Archivos-Json/destinos.json'

# Limpiar pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Pausar pantalla
def pausar():
    input("\nPresione Enter para continuar...")




# Cargar destinos desde el archivo JSON
def cargar_destinos()->list:
    try:
        with open(ARCHIVO_DATOS, 'r', encoding='utf-8') as f:
            destinos = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        destinos = []
    return destinos


# Guardar destinos en el archivo JSON
def guardar_destinos(destinos):
    with open(ARCHIVO_DATOS, 'w') as f:
        json.dump(destinos, f, indent=4)

# Agregar un nuevo destino
def agregar_destino(destino):
    if destino:
        lugar=destino['Nombre']
        precio=destino['Precio']
        cupo=destino['Disponibilidad']
    else:
        limpiar_pantalla()
        print("=== Agregar Nuevo Destino ===")
        lugar = input("Ingrese el nombre del destino: ")
        precio = float(input("Ingrese el precio del paquete: "))
        cupo = int(input("Ingrese los cupos disponibles: "))
    destinos=cargar_destinos()
    nuevo_id = max([d["id"] for d in destinos], default=0) + 1

    nuevo_destino = {
        "id": nuevo_id,
        "nombre": lugar,
        "precio": int(precio),
        "disponibilidad": int(cupo)
    }

    destinos.append(nuevo_destino)
    guardar_destinos(destinos)
    return True
    #pausar()

# Listar todos los destinos
def listar_destinos(destinos):
    limpiar_pantalla()
    print("=== Lista de Destinos ===")
    if not destinos:
        print("No hay destinos cargados.")
    else:
        for d in destinos:
            print(f"ID: {d['id']:<3} | Lugar: {d['lugar']:<12} | Precio: ${d['precio']:<10} | Cupos disponibles: {d['disponibilidad']}")
    pausar()





#listar destinos por precio
def listar_destinos_por_precio(destinos):
    limpiar_pantalla()
    print("=== Lista de Destinos por Precio (menor a mayor) ===")

    if not destinos:
        print("No hay destinos cargados.")
    else:
        # Ordena los destinos por precio ascendente
        destinos_ordenados = sorted(destinos, key=lambda d: d['precio'])

        print(f"{'ID':<5} {'Lugar':<20} {'Precio':>10}")
        print("-" * 40)
        for d in destinos_ordenados:
            print(f"{d['id']:<5} {d['lugar']:<20} ${d['precio']:>10,.2f}")
    pausar()


# Eliminar destino por ID
def eliminar_destino_tk(id):
    destinos= cargar_destinos()
    lista =[k for k in destinos if k['id'] != id]
    guardar_destinos(lista)
    return True


def eliminar_destino(destinos):
    limpiar_pantalla()
    print("=== Eliminar Destino ===")
    listar_destinos(destinos)
    try:
        id_eliminar = int(input("\nIngrese el ID del destino a eliminar: "))
        destino = next((d for d in destinos if d["id"] == id_eliminar), None)

        if destino:
            print(f"\nDestino seleccionado:")
            print(f"ID: {destino['id']} | Lugar: {destino['lugar']} | Precio: ${destino['precio']}")
            confirmacion = input("\n¿Seguro que desea eliminar este destino? (S/N): ").strip().upper()

            if confirmacion == 'S':
                destinos.remove(destino)
                guardar_destinos(destinos)
                print("\nDestino eliminado con éxito.")
            else:
                print("\nEliminación cancelada.")
        else:
            print("\nNo se encontró un destino con ese ID.")
    except ValueError:
        print("ID inválido.")
    pausar()



#modificar destino por id
def modificar_destino(destinos):
    limpiar_pantalla()
    print("=== Modificar Destino por ID ===")
    try:
        id_modificar = int(input("Ingrese el ID del destino a modificar: "))
        destino = next((d for d in destinos if d["id"] == id_modificar), None)

        if destino:
            print(f"\nDestino actual:")
            print(f"ID: {destino['id']} | Lugar: {destino['lugar']} | Precio: ${destino['precio']}")

            confirmacion = input("\n¿Seguro que desea modificar este destino? (S/N): ").strip().upper()

            if confirmacion == 'S':
                nuevo_lugar = input("Nuevo nombre del destino (Enter para mantener): ")
                if nuevo_lugar:
                    destino['lugar'] = nuevo_lugar

                try:
                    nuevo_precio = input("Nuevo precio del paquete (Enter para mantener): ")
                    if nuevo_precio:
                        destino['precio'] = float(nuevo_precio)
                except ValueError:
                    print("Precio inválido, se mantiene el valor anterior.")

                guardar_destinos(destinos)
                print("\nDestino modificado con éxito.")
            else:
                print("\nModificación cancelada.")
        else:
            print("\nNo se encontró un destino con ese ID.")
    except ValueError:
        print("ID inválido.")
    pausar()

#por nombre total o parcial
def buscar_destino(destinos):
    limpiar_pantalla()
    print("=== Buscar Destino por Nombre ===")
    termino = input("Ingrese el nombre o parte del nombre del destino: ").lower()

    resultados = [d for d in destinos if termino in d["lugar"].lower()]

    if resultados:
        print("\nResultados encontrados:")
        for d in resultados:
            print(f"ID: {d['id']} | Lugar: {d['lugar']} | Precio: ${d['precio']}")
    else:
        print("\nNo se encontraron destinos con ese nombre.")
    pausar()

#buscar destino por id
def buscar_destino_por_id(destinos):
    limpiar_pantalla()
    print("=== Buscar Destino por ID ===")
    try:
        id_buscar = int(input("Ingrese el ID del destino: "))
        destino = next((d for d in destinos if d["id"] == id_buscar), None)

        if destino:
            print(f"\nDestino encontrado:")
            print(f"ID: {destino['id']} | Lugar: {destino['lugar']} | Precio: ${destino['precio']}")
        else:
            print("\nNo se encontró un destino con ese ID.")
    except ValueError:
        print("ID inválido.")
    pausar()


# Menú principal
def menu():
    destinos = cargar_destinos()

    while True:
        limpiar_pantalla()
        print("=== Agencia de Viajes ===")
        print("1. Listar destinos")
        print("2. Agregar destino")
        print("3. Eliminar destino")
        print("4. Buscar destino por nombre")
        print("5. Buscar destino por ID")
        print("6. Modificar destino por ID")
        print("7. Listar destinos por precio")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            listar_destinos(destinos)
        elif opcion == '2':
            agregar_destino(destinos)
        elif opcion == '3':
            eliminar_destino(destinos)
        elif opcion == '4':
            buscar_destino(destinos)
        elif opcion == '5':
            buscar_destino_por_id(destinos)
        elif opcion == '6':
            modificar_destino(destinos)
        elif opcion == '7':
            listar_destinos_por_precio(destinos)
        elif opcion == '8':
            print("Gracias por usar el sistema de la Agencia de Viajes.")
            break
        else:
            print("Opción inválida.")
            pausar()

# Ejecutar el programa
if __name__ == "__main__":
    menu()
