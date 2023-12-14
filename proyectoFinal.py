import os
import pandas as pd
from tabulate import tabulate
import tkinter as tk
import datetime
import hashlib

dataFrameUsers = pd.DataFrame
dataFramePlatos = pd.DataFrame
dataFrameMesas = pd.DataFrame

matrizUsuarios = []
matrizPlatos = []
matrizMesas = []

usuarioActual = None


def linea():
    print("------------------------")

def menuInicial():

    print("\n-----Menu Principal-----")
    print("1. Registrarse")
    print("2. Iniciar sesion")
    print("3. Salir")
    print("------------------------")

    opcion = int(input("¿Que desea hacer?: "))

    while (opcion < 4 and opcion > 0):
        if opcion == 1:
            registrarse()
            break

        if opcion == 2:
            iniciarSesion()
            break
        
        if opcion == 3:
            return 0
        
        else: break
    return 0

def cargarDatos():

    #Abrir usuarios
    cargarUsuarios()
    #Abrir Platos
    cargarPlatos()
    #Abrir Mesas
    cargarMesas()
    #cargarContraseñas
    OpenPassword()

def cargarUsuarios():

    global archivoUsuarios
    global matrizUsuarios
    global dataFrameUsers

    nombreArchivo = 'Usuarios.txt'
    rutaArchivo = os.path.join(os.path.dirname(__file__), nombreArchivo)

    
    if not os.path.isfile(rutaArchivo):
        archivoUsuarios = open(rutaArchivo, "a")
        print("Se ha creado el archivo usuarios")
    else:
        archivoUsuarios = open(rutaArchivo, "r")
        print("Se cargaron los usuarios con exito")

    for linea in archivoUsuarios:
        usuarioA, contraseñaA = linea.strip().split(',')
        userPass = [usuarioA, contraseñaA]
        matrizUsuarios.append(userPass)
    dataFrameUsers = pd.DataFrame(matrizUsuarios, columns = ["Users", "Passwords"])
    print(dataFrameUsers)   
        
def cargarPlatos():

    global archivoPlatos
    global matrizPlatos
    global dataFramePlatos

    nombreArchivo = 'Platos.txt'
    rutaArchivo = os.path.join(os.path.dirname(__file__), nombreArchivo)

    
    if not os.path.isfile(rutaArchivo):

        archivoPlatos = open(rutaArchivo, "a")
        print("Se ha creado el archivo Platos")
    else:
        archivoPlatos = open(rutaArchivo, "r")
        print("Se cargaron los Platos con exito")

    for linea in archivoPlatos:
        id, nombrePlato, precioPlato, descripcionPlato, disponibilidad = linea.strip().split(',')
        plato = [id, nombrePlato, precioPlato, descripcionPlato, disponibilidad] 
        matrizPlatos.append(plato)

    dataFramePlatos = pd.DataFrame(matrizPlatos, columns = ["ID","Nombre", "Precio", "Descripcion", "Disponibilidad"])
    print(dataFramePlatos)  

def guardarPlatos(id, nombre, precio, descripcion, disponibilidad):

    global archivoPlatos
    global matrizPlatos
    global dataFramePlatos

    with open(archivoPlatos.name, "a") as f:
        f.write(f"{id},{nombre},{precio},{descripcion},{disponibilidad}\n")
        f.flush()

    nuevoPlato = [id, nombre, precio, descripcion, disponibilidad]

    dataFramePlatos.loc[len(dataFramePlatos)] = nuevoPlato

def cargarMesas():

    global archivoMesas
    global matrizMesas
    global dataFrameMesas

    nombreArchivo = 'Mesas.txt'
    rutaArchivo = os.path.join(os.path.dirname(__file__), nombreArchivo)

    
    if not os.path.isfile(rutaArchivo):
        archivoMesas = open(rutaArchivo, "a")
        print("Se ha creado el archivo Mesas")
    else:
        archivoMesas = open(rutaArchivo, "r")
        print("Se cargaron las Mesas con exito")

    for linea in archivoMesas:
        id, fecha, noPersonas = linea.strip().split(',')
        mesa = [id, fecha, noPersonas] 
        matrizMesas.append(mesa)
    dataFrameMesas = pd.DataFrame(matrizMesas, columns = ["ID", "Fecha y hora", "NumeroPersonas"])
    print(dataFrameMesas)  

def guardarMesas(id, fecha, noPersonas):
    global archivoMesas
    global matrizMesas
    global dataFrameMesas

    with open(archivoMesas.name, "a") as f:
        f.write(f"{id},{fecha},{noPersonas}\n")
        f.flush()

    nuevaMesa = [id, fecha, noPersonas]
    matrizMesas.append(nuevaMesa)
    dataFrameMesas.loc[len(dataFrameMesas)] = nuevaMesa

def idTables():

    id =dataFrameMesas.iloc[-1]["ID"]
    id = int(id)
    id += 1

    return id

def idPlates():

    id =dataFramePlatos.iloc[-1]["ID"]
    id = int(id)
    id += 1

    return id

def registrarse():

    contraseñacifrada = hashlib.sha256()
    gmail = input("Ingrese su correo: ")

    if (buscarUsuario(gmail) == False):
        while True:
            if (verificarCorreo(gmail)):
                print("Correo valido")
                contraseña = input("Ingrese una contraseña: ")
                confirmPassword = input("Confirme su contraseña:")
                if contraseña == confirmPassword:
                    if (verificarContraseña(contraseña)):
                        contraseñacifrada = hashlib.sha256(
                            contraseña.encode()).hexdigest()
                        linea()
                        print("Usuario registrado con exito")
                        linea()
                        guardarUsuario(gmail, contraseña)
                        guardarPassword(contraseñacifrada)
                        menuInicial()
                        break
                    else:
                        print(
                            "Este correo no cuenta con los requisitos minimos\nIntente denuevo")
                        registrarse()
                else:
                    print("las contraseñas no coinciden")
    else:
        print("Este correo ya esta registrado, intentelo de nuevo")
        registrarse()


def OpenPassword():

    global archivoContras

    nombreArchivo = 'password.txt'
    rutaArchivo = os.path.join(os.path.dirname(__file__), nombreArchivo)

    if not os.path.isfile(rutaArchivo):
        archivoContras = open(rutaArchivo, "a")
        print("Se ha creado el archivo Password")
    else:
        archivoContras = open(rutaArchivo, "r")
        print("Se cargaron las contraseña cifradas con exito")


def guardarPassword(contraseña):

    with open(archivoContras.name, "a") as f:
        f.write(f"{contraseña}\n")
        f.flush()
              
def verificarCorreo(gmail):

    mailsValidos = ["gmail", "hotmail", "yahoo", "outlook", "correunivalle"]

    if any(palabra in gmail.lower() for palabra in mailsValidos):
        if "@" in gmail and any(gmail.endswith(extension) for extension in [".com", ".con", ".co"]):
            return True
    return False

def verificarContraseña(contraseña):
    
    minus = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    mayus = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    chars = ['@', '*', '$', '!', '?', '\\', '&', '/']
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    if len(contraseña) > 10:
        if any(letter in contraseña for letter in minus):
            if any(letter in contraseña for letter in mayus):
                if any(char in contraseña for char in chars):
                    if any(num in contraseña for num in nums):
                        return True
    return False



def guardarUsuario(correo, contraseña):

    global archivoUsuarios

    with open(archivoUsuarios.name, "a+") as f:
        f.write(f"{correo},{contraseña}\n")
        f.flush()
 

def iniciarSesion():

    global usuarioActual

    nombre = input("Ingrese su nombre de usuario: ")
    if(buscarUsuario(nombre)):
        contraseña = input("Ingrese su clave: ")
        if(confirmarContraseña(nombre, contraseña)):
            print("Sesion iniciada correctamente.")
            usuarioActual = nombre
            menuPrincipal()
        else:
            print("Contraseña incorrecta, intente de nuevo")
            iniciarSesion()
    else:
        print("Nombre de usuario incorrecto, intente de nuevo")
        iniciarSesion()

    
def confirmarContraseña(usuario, contraseña):

    global dataFrameUsers

    fila = dataFrameUsers.loc[dataFrameUsers["Users"] == usuario]
    print(fila)

    contraseñaUsuario = fila["Passwords"].values[0]
    if contraseña == contraseñaUsuario:
        return True
    else:
        return False

def buscarUsuario(usuario):
    
    global dataFrameUsers

    existe = usuario in dataFrameUsers["Users"].values

    if (existe):
        return True
    else:
        return False


def menuPrincipal():

    global usuarioActual

    linea()
    print("Hola ",usuarioActual )
    print("-----Menu Principal-----")
    print("1. Gestion Platos")
    print("2. Gestion Mesas")
    print("3. Gestion pedidos")
    print("4. Cerrar sesion")
    linea()

    opcion = int(input("¿Que desea hacer?: "))

    while (opcion < 5 and opcion > 0):
        if opcion == 1:
            gestionPlatos()
            break

        if opcion == 2:
            gestionMesas()
            break

        if opcion == 3:
            gestionPedidos()

        if opcion == 4:
            cerrarSesion()
            menuInicial()
    return 0

#Platos
def gestionPlatos():
    print("\n-----Gestion de platos-----")
    print("1. Agregar")
    print("2. Eliminar")
    print("3. Actualizar")
    print("4. Menu principal")
    print("------------------------")

    opcion = int(input("¿Que desea hacer?: "))

    while (opcion < 5 and opcion > 0):
        if opcion == 1:
            agregarPlato()
            break

        if opcion == 2:
            eliminarPlato()
            break
        
        if opcion == 3:
            actualizarPlato()
            break

        if opcion == 4:
            menuPrincipal()
            break
    return 0

def agregarPlato():
    
    print("\n-----Agregar Plato-----")
    nombre = input("Nombre del plato: ")
    precio = input("Precio del plato: ")
    descripcion = input("Descripción del plato: ")
    disponibilidad = input("Disponibilidad del plato (Sí/No): ").upper()
    id = idPlates()

    guardarPlatos(id, nombre, precio, descripcion, disponibilidad)
    gestionPlatos()

def eliminarPlato():

    print(dataFramePlatos)
    linea()
    id = input("Ingrese la ID a eliminar: ")
    linea()

    if id in dataFramePlatos["ID"].values:
        index = dataFramePlatos[dataFramePlatos["ID"] == id].index
        dataFramePlatos.drop(index, inplace=True)
        matrizPlatos.pop(index[0])
        print("Plato eliminado")
        dataFramePlatos.to_csv('Platos.txt', index=False)

    else:
        print(f"No se encontro la id: {id}")

    print(dataFramePlatos)
    print(matrizPlatos)

def actualizarPlato():

    print("\n-----Actualizar Plato-----")
    id = input("Ingrese la ID: ")

    if id in dataFramePlatos["ID"].values:
        print("Ingrese los nuevos platos")
        nombre = input("Nuevo nombre del plato: ")
        precio = input("Nuevo precio del plato: ")
        descripcion = input("Nueva descripción del plato: ")
        disponibilidad = input("Nueva disponibilidad del plato (Sí/No): ").upper()

        dataFramePlatos.loc[dataFramePlatos["ID"] == id, ["Nombre", "Precio", "Descripcion", "Disponibilidad"]] = [nombre, precio, descripcion, disponibilidad]
        dataFramePlatos.to_csv('Platos.txt', index=False)

        print("Plato actualizado")

    else:
        print(f"No se encontró la ID: {id}")


#Mesas
def gestionMesas():
    print("\n-----Gestion de Mesas-----")
    print("1. Agregar")
    print("2. Eliminar")
    print("3. Actualizar")
    print("4. Menu principal")
    print("------------------------")

    opcion = int(input("¿Que desea hacer?: "))

    while (opcion < 5 and opcion > 0):
        if opcion == 1:
            agregarReserva()
            break

        if opcion == 2:
            eliminarReserva()
            break
        
        if opcion == 3:
            modificarReserva()
            break

        if opcion == 4:
            menuPrincipal()
            break
    return 0

def agregarReserva():
    print("\n-----Agregar Reserva-----")
    

    while(True):
        try:
            dia = int(input("Dia: "))
            if dia > 31 or dia < 1:
                raise Exception
            break
        except Exception:
            print("El dia debe estar entre 1 y 31")
    while(True): 
        try:
            mes = int(input("Mes: "))
            if mes > 12 or mes < 0:
                raise Exception
            break
        except Exception:
            print("El mes debe estar entre 1 y 12")
    while(True):
        try:
            hora = int(input("Hora: "))
            if hora > 24 or hora < 0:
                raise Exception
            break
        except Exception:
            print("La hora debe estar entre 0 y 24")
        try:
            if dia > 30:
                if mes == 4 or mes == 6 or mes == 9 or mes == 11:
                    raise Exception
        except ValueError:
            print("Dato invalido")
        except Exception:
            print("Este mes tiene no tiene tantos dias")

        id = idTables()

    fecha = datetime.datetime(2023, dia, mes, hora, 0 , 0)
    nPersonas = int(input("Numero personas: "))

    guardarMesas(id, fecha, nPersonas)

def eliminarReserva():
    
    print(dataFrameMesas)
    linea()
    id = input("Ingrese la ID a eliminar: ")
    linea()

    if id in dataFrameMesas["ID"].values:
        index = dataFrameMesas[dataFrameMesas["ID"] == id].index
        dataFrameMesas.drop(index, inplace=True)
        matrizMesas.pop(index[0])
        dataFrameMesas.to_csv('Mesas.txt', index=False)
        print("Plato eliminado")
    else:
        print(f"No se encontro la id: {id}")

    print(dataFramePlatos)
    print(matrizPlatos)

def modificarReserva():
    print("\n-----Modificar Reserva-----")
    id_mesa = input("Ingrese la ID: ")

    if id_mesa in dataFrameMesas["ID"].values:
        reserva = dataFrameMesas[dataFrameMesas["ID"] == id_mesa]

        print("Información actual:")
        print(reserva)

        # Proporciona opciones para modificar la reserva
        print("\nSeleccione el dato que desea modificar:")
        print("1. Fecha y hora")
        print("2. Número de personas")
        print("3. Cancelar")
        
        opcion = input("Opción: ")

        if opcion == "1":
            while(True):
                try:
                    dia = int(input("Dia: "))
                    if dia > 31 or dia < 1:
                        raise Exception
                    break
                except Exception:
                    print("El dia debe estar entre 1 y 31")
            while(True): 
                try:
                    mes = int(input("Mes: "))
                    if mes > 12 or mes < 0:
                        raise Exception
                    break
                except Exception:
                    print("El mes debe estar entre 1 y 12")
            while(True):
                try:
                    hora = int(input("Hora: "))
                    if hora > 24 or hora < 0:
                        raise Exception
                    break
                except Exception:
                    print("La hora debe estar entre 0 y 24")
                try:
                    if dia > 30:
                        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
                            raise Exception
                except ValueError:
                    print("Dato invalido")
                except Exception:
                    print("Este mes tiene no tiene tantos dias")

            fecha = datetime.datetime(2023, dia, mes, hora, 0 , 0)

            dataFrameMesas.loc[dataFrameMesas["ID"] == id_mesa, "Fecha y hora"] = fecha
            print("Fecha y hora modificadas")

        elif opcion == "2":
            nuevo_numero_personas = input("Ingrese numero de personas: ")
            dataFrameMesas.loc[dataFrameMesas["ID"] == id_mesa, "NumeroPersonas"] = nuevo_numero_personas
            print("Numero de personas modificado")

        elif opcion == "3":
            print("Cancelado")
            gestionMesas()
        else:
            print("Opción no válida.")
        dataFrameMesas.to_csv('Mesas.txt', index=False)

    else:
        print(f"No se encontró la ID: {id_mesa}")

#Pedidos
def gestionPedidos():
    print("\n-----Gestion de platos-----")
    print("1. Realizar")
    print("2. Eliminar")
    print("3. Actualizar")
    print("4. Menu principal")
    print("------------------------")

    opcion = int(input("¿Que desea hacer?: "))

    while (opcion < 5 and opcion > 0):
        if opcion == 1:
            realizarPedido()
            break

        if opcion == 2:
            elimninarPedido()
            break
        
        if opcion == 3:
            modificarPedido()
            break

        if opcion == 4:
            menuPrincipal()
            break
    return 0

def realizarPedido():
    pass
def elimninarPedido():
    pass
def modificarPedido():
    pass

#Cerrar sesion
def cerrarSesion():
    
    global usuarioActual

    usuarioActual = None
    
    linea()
    print("Cerrando sesion")
    linea()
    menuInicial()

def saveData():

    script_dir = os.path.dirname(__file__)

    users_path = os.path.join(script_dir, 'Usuarios.txt')
    dataFrameUsers.to_csv(users_path, index=False)

    platos_path = os.path.join(script_dir, 'Platos.txt')
    dataFramePlatos.to_csv(platos_path, index=False)

    mesas_path = os.path.join(script_dir, 'Mesas.txt')
    dataFrameMesas.to_csv(mesas_path, index=False)

if __name__ == "__main__":

    cargarDatos()
    eliminarPlato()
    menuInicial()
    saveData()