'''

Crear, leer, modificar y eliminar clientes.


'''
import json
def altaCliente():
    clientesJson='Archivos-Json/clientes.json'
    with open(clientesJson,'r',encoding='utf-8') as clientesjson:
        clientes= json.load(clientesjson)
    
    print('ingrese los datos del nuevo cliente')
    nombre= input('ingrese el nombre: ')
    apellido= input('ingrese el apellido: ')
    dni= input('ingrese el dni: ')
    email= input('ingrese el email: ')
 
    nuevoId=(clientes[len(clientes)-1]['id'])+1
    #print(type(clientes))
    nuevoCliente={
        'id':nuevoId,
        'nombre':nombre,
        'apellido':apellido,
        'dni':dni,
        'email':email
    }
    #print(type(clientes))
    clientes.append(nuevoCliente)
    #print(clientes)
    with open(clientesJson,'w',encoding='utf-8') as i:
        json.dump(clientes,i)


altaCliente()