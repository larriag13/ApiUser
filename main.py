from vista.vista_usuario import main_usuario,add_user
from controlador.autentificacion_controller import hay_usuarios,autenticar
from vista.vista_indicadores import main_indicadores

usuario=None
def menu():
    print("Menú general")
    print("1.- Usuarios")
    print("2.- Indicadores")
    print("0.- Salir")
    op=int(input("Seleccione una opción: "))
    return op


while True:
    if hay_usuarios():
        print("Inicio sesión")
        nombre=input("Ingrese nombre: ")
        passwd=input("Ingrese contraseña: ")
        usuario=autenticar(nombre,passwd)
        if usuario is not None:
            print(f"Bienvenido {usuario.get_nombre()}")
            op=menu()
            if op==1:
                main_usuario()
            elif op==2:
                main_indicadores()
            break
        else:
            print("Usuario o contraseña incorrecta.")
    else:
        print("No hay usuarios registrados")
        add_user()