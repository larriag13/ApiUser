from modelo.bd import conectar
from modelo.usuario import Usuario
import bcrypt
def agregar_usuario(usuario):
    conn=conectar()
    if conn is not None:
        try:
            cursor=conn.cursor()
            pwd_hash=bcrypt.hashpw(usuario.get_passwd().encode('utf-8'),bcrypt.gensalt())
            cursor.execute("INSERT INTO usuario(nombre,edad,passwd,perfil) VALUES(%s,%s,%s,%s)",
                           (usuario.get_nombre(),usuario.get_edad(),pwd_hash,usuario.get_perfil()))
            conn.commit()
            print("Usuario agregado")
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

def buscar_user(nombre):
    conn=conectar()
    if conn is not None:
        try:
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM usuario WHERE nombre=%s",(nombre,))
            usuario=cursor.fetchone()
            usuario_o=Usuario(usuario[1],usuario[2],usuario[3],usuario[4])
            usuario_o.set_id(usuario[0])
            return usuario_o
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

def mostrar_usuarios():
    conn=conectar()
    if conn is not None:
        try:
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM usuario")
            usuarios=cursor.fetchall()
            return usuarios
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()