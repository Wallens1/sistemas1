import os

archivoUsuarios = None
usuarioActual = None


def linea():
    print("------------------------")

def menuInicial():

    global usuarioActual

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

    global archivoUsuarios

    nombreArchivo = 'Usuarios.txt'
    rutaArchivo = os.path.join(os.path.dirname(__file__), nombreArchivo)

    
    if not os.path.isfile(rutaArchivo):
        archivoUsuarios = open(rutaArchivo, "a")
        print("Se ha creado el archivo usuarios")
    else:
        archivoUsuarios = open(rutaArchivo, "a+")
        print("Se cargaron los usuarios con exito")

def cargarPlatos():
    pass

def cargarMesas():
    pass

#Menu inicial
def registrarse():
    
    gmail = input("Ingrese su correo: ")
    
    if(buscarUsuario(gmail) == False):
        if(verificarCorreo(gmail)):
            print("Correo valido")
            contraseña = input("Ingrese una contraseña: ")
            if (verificarContraseña(contraseña)):
                linea()
                print ("Usuario registrado con exito")
                linea()
                guardarUsuario(gmail, contraseña)
                menuInicial()
        else:
            print("Este correo no cuenta con los requisitos minimos\nIntente denuevo")  
            registrarse()
    else:
        print("Este correo ya esta registrado, intentelo de nuevo")
        registrarse()
            

    
def verificarCorreo(gmail):

    mailsValidos = ["gmail", "hotmail", "yahoo", "outlook", "correunivalle"]

    if any(palabra in gmail.lower() for palabra in mailsValidos):
        if "@" in gmail and any(gmail.endswith(extension) for extension in [".com", ".con", ".co"]):
            return True
    return False

def verificarContraseña(contraseña):
    return True

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

    global archivoUsuarios

    if archivoUsuarios:
        if(buscarUsuario(usuario)):
            archivoUsuarios.seek(0)
            for linea in archivoUsuarios:
                usuarioA, contraseñaA = linea.strip().split(',')
                if contraseña == contraseñaA and usuario == usuarioA:
                    return True
            return False
        else:
            return False
    else:
        print("Error: El archivo de usuarios no está abierto.")

def buscarUsuario(usuario):
    
    global archivoUsuarios

    if archivoUsuarios:
        archivoUsuarios.seek(0)
        for linea in archivoUsuarios:
            gmail, contraseña = linea.strip().split(',')
            if usuario == gmail:
                return True
        return False
    else:
        print("Error: El archivo de usuarios no está abierto.")


def menuPrincipal():

    global usuarioActual

    linea()
    print("Hola ",usuarioActual )
    print("-----Menu Principal-----")
    print("1. Gestion Platos")
    print("2. Gestion Mesas")
    print("3. Gestion pedidos")
    print("4. Cerras sesion")
    linea()

    opcion = int(input("¿Que desea hacer?: "))

    while (opcion < 5 and opcion > 0):
        if opcion == 1:
            pass

        if opcion == 2:
            pass

        if opcion == 3:
            pass

        if opcion == 4:
            pass
    return 0

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
    
    global usuarioActual

    usuarioActual = None

    linea()
    print("Cerrando sesion")
    linea()
    menuInicial()

if __name__ == "__main__":

    cargarDatos()

    menuInicial()

    if archivoUsuarios:
        archivoUsuarios.close()