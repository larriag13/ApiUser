from modelo.usuario import Usuario
from controlador.usuario_controller import agregar_usuario,buscar_user

def leer_numero(mensaje):
    while True:
        try:
            op=int(input(mensaje))
            return op
        except:
            print("Debe ingresar un número.")

def menu():
    print("App Usuarios")
    print("1.- Agregar")
    print("2.- Editar")
    print("3.- Eliminar")
    print("4.- Mostrar uno")
    print("5.- Mostrar todos")
    print("0.- Salir")
    op=leer_numero("Ingrese una opción: ")
    return op

def add_user():
    nombre=input("Ingrese nombre: ")
    edad=leer_numero("Ingrese edad: ")
    passwd=input("Ingrese contraseña: ")
    perfil=input("Ingrese perfil de usuario: ")
    usuario=Usuario(nombre,edad,passwd,perfil)
    agregar_usuario(usuario)

def mostrar_usuario():
    nombre=input("Ingrese nombre del usuario a buscar: ")
    usuario=buscar_user(nombre)
    print(usuario)


def main_usuario():
    while True:
        op=menu()
        if op==1:#agregar
            add_user()
        elif op==4:
            mostrar_usuario()
        elif op==0:
            print("Gracias por preferirnos")
            break
