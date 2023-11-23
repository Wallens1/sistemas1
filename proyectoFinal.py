import os

def menuInicial():

    cargarDatos()

    print("\n-----Menu Principal-----")
    print("1. Registrarse")
    print("2. Iniciar sesion")
    print("3. Salir")
    print("------------------------")

    opcion = int(input("¿Que desea hacer?: "))

    while (opcion !=3):
        if opcion == 1:
            registrarse()

        if opcion == 2:
            iniciarSesion()

        if opcion == 3:
            break

    return 0

def cargarDatos():

    #Abrir usuarios
    cargarUsuarios()
    #Abrir Platos
    cargarPlatos()
    #Abrir Mesas
    cargarMesas()

def cargarUsuarios():

    nombre_archivo = 'Usuarios.txt'
    ruta_archivo = os.path.join(os.path.dirname(__file__), nombre_archivo)

    if not os.path.isfile(ruta_archivo):

        with open(ruta_archivo, 'w') as archivo:
        print(f'Se ha creado el archivo "{nombre_archivo}" en la carpeta del script con éxito.')
    else:
        print("Se cargaron los usuarios con exito")

def cargarPlatos():

    nombre_archivo = 'Platos.txt'
    ruta_archivo = os.path.join(os.path.dirname(__file__), nombre_archivo)

    if not os.path.isfile(ruta_archivo):

        with open(ruta_archivo, 'w') as archivo:
        print(f'Se ha creado el archivo "{nombre_archivo}" en la carpeta del script con éxito.')
    else:
        print("Se cargaron los platos con exito")

def cargarMesas():

    nombre_archivo = 'Mesas.txt'
    ruta_archivo = os.path.join(os.path.dirname(__file__), nombre_archivo)

    if not os.path.isfile(ruta_archivo):

        with open(ruta_archivo, 'w') as archivo:
        print(f'Se ha creado el archivo "{nombre_archivo}" en la carpeta del script con éxito.')
    else:
        print("Se cargaron las mesas con exito")


#Menu inicial
def registrarse():
    pass

def iniciarSesion():
    nombre = input("Ingrese su nombre de usuario: ")
    buscarUsuario(nombre)
    

def buscarUsuario(nombre):
    pass


def menuPrincipal():
    pass


#Platos
def gestionPlatos():
    pass

def agregarPlato():
    pass
def eliminarPlato():
    pass
def actualizarPlato():
    pass


#Mesas
def gestionMesas():
    pass

def agregarReserva():
    pass
def eliminarReserva():
    pass
def modificarReserva():
    pass

#Pedidos
def gestionPedidos():
    pass

def realizarPedido():
    pass
def elimninarPedido():
    pass
def modificarPedido():
    pass

#Cerrar sesion
def cerrarSesion():
    pass

if __name__ == "__main__":

    menuInicial()