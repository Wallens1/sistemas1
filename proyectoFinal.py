import os

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

    global archivoU

    if not os.path.isfile(ruta_archivo):
        archivoU = open(nombre_archivo, "a")
        print(f'Se ha creado el archivo "{nombre_archivo}" en la carpeta del script con éxito.')
    else:
        print("Se cargaron los usuarios con exito")

def cargarPlatos():

    nombre_archivo = 'Platos.txt'
    ruta_archivo = os.path.join(os.path.dirname(__file__), nombre_archivo)

    if not os.path.isfile(ruta_archivo):
        with open(ruta_archivo, 'w') as archivo:
            pass
        print(f'Se ha creado el archivo "{nombre_archivo}" en la carpeta del script con éxito.')
    else:
        print("Se cargaron los platos con exito")

def cargarMesas():

    nombre_archivo = 'Mesas.txt'
    ruta_archivo = os.path.join(os.path.dirname(__file__), nombre_archivo)

    if not os.path.isfile(ruta_archivo):
        with open(ruta_archivo, 'w') as archivo:
            pass
        print(f'Se ha creado el archivo "{nombre_archivo}" en la carpeta del script con éxito.')
    else:
        print("Se cargaron las mesas con exito")


#Menu inicial
def registrarse():
    
    gmail = input("Ingrese su correo: ")
    
    while(True):
        if(verificarCorreo(gmail)):
            print("Correo valido")
            contraseña = input("Ingrese una contraseña: ")
            if (verificarContraseña(contraseña)):
                linea()
                print ("Usuario registrado con exito")
                linea()
                guardarUsuario(gmail, contraseña)
                menuInicial()
                break
        else:
            print("Este correo no cuenta con los requisitos minimos\nIntente denuevo")  
    


def verificarCorreo(gmail):

    mailsValidos = ["gmail", "hotmail", "yahoo", "outlook", "correunivalle"]

    if any(palabra in gmail.lower() for palabra in mailsValidos):
        if "@" in gmail and any(gmail.endswith(extension) for extension in [".com", ".con", ".co"]):
            return True
    return False

def verificarContraseña(contraseña):

    return True

def guardarUsuario(correo, contraseña):

    with open(archivoU, "a") as f:
        f.write(f"{correo},{contraseña}\n")

    

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

    cargarDatos()

    menuInicial()