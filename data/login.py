def inicio():
    #Menu de inicio
    print("╔══════════════════════════════╗")
    print("║    ⚜  BIBLIOTECA UADE ⚜      ║")
    print("╠══════════════════════════════╣")
    print("║ 1. Crear cuenta              ║")
    print("║ 2. Iniciar sesión como socio ║")
    print("║ 3. Iniciar sesión como admin ║")
    print("║ 0. Salir                     ║")
    print("╚══════════════════════════════╝")

#Menu de socio
def menu_socio():
    print(" ╔══════════════════════════════╗")
    print(" ║    ⚜  BIBLIOTECA UADE ⚜      ║")
    print(" ╠══════════════════════════════╣")
    print(" ║ 1. Búsqueda de libro         ║")
    print(" ║ 2. Listar libros             ║")
    print(" ║ 3. Pedir libro               ║")
    print(" ║ 0. Cerrar sesión             ║")
    print(" ╚══════════════════════════════╝")

#Menu de admin
def menuAdmin():
    print("╔══════════════════════════════╗")
    print("║   ⚜  BIBLIOTECA UADE ⚜       ║")
    print("╠══════════════════════════════╣")
    print("║ 1. Socio                     ║")
    print("║ 2. Libro                     ║")
    print("║ 3. Préstamo                  ║")
    print("║ 0. Cerrar Sesión             ║")
    print("╚══════════════════════════════╝")

def subMenuAdmin_Socio():
    print(" ╔══════════════════════════════╗")
    print(" ║    ⚜  BIBLIOTECA UADE ⚜      ║")
    print(" ╠══════════════════════════════╣")
    print(" ║ 1. Dar de alta un socio      ║")
    print(" ║ 2. Modificar estado          ║")
    print(" ║ 3. Ver listado socios        ║")
    print(" ║ 0. Retroceder                ║")
    print(" ╚══════════════════════════════╝")

def subMenuAdmin_Libro():
    print(" ╔══════════════════════════════╗")
    print(" ║    ⚜  BIBLIOTECA UADE ⚜      ║")
    print(" ╠══════════════════════════════╣")
    print(" ║ 1. Búsqueda de libro         ║")
    print(" ║ 2. Dar de alta un libro      ║")
    print(" ║ 3. Dar de baja un libro      ║")
    print(" ║ 4. Modificar libro           ║")
    print(" ║ 5. Listar libros             ║")
    print(" ║ 0. Retroceder                ║")
    print(" ╚══════════════════════════════╝")

def subMenuAdmin_Prestamo():
    print(" ╔══════════════════════════════╗")
    print(" ║    ⚜  BIBLIOTECA UADE ⚜      ║")
    print(" ╠══════════════════════════════╣")
    print(" ║ 1. Ver listado préstamo      ║")
    print(" ║ 2. Devolver libro            ║")
    print(" ║ 0. Retroceder                ║")
    print(" ╚══════════════════════════════╝")

#Menu de sub-menu socio
def sub_menuBusqueda():
    print(" ╔══════════════════════════════╗")
    print(" ║   ⚜  BIBLIOTECA UADE ⚜       ║")
    print(" ╠══════════════════════════════╣")
    print(" ║ 1. Buscar libro por autor    ║")
    print(" ║ 2. Buscar libro por nombre   ║")
    print(" ║ 3. Buscar libro por ID       ║")
    print(" ║ 0. Retroceder                ║")
    print(" ╚══════════════════════════════╝")


def sub_menuModificar():
    print("╔══════════════════════════════╗")
    print("║   ⚜  BIBLIOTECA UADE ⚜       ║")
    print("╠══════════════════════════════╣")
    print("║ 1. Modificar nombre          ║")
    print("║ 2. Modificar autor           ║")
    print("║ 3. Modificar stock           ║")
    print("║ 0. Retroceder                ║")
    print("╚══════════════════════════════╝")

def sub_menuModificarStock():
    print("╔══════════════════════════════╗")
    print("║   ⚜  BIBLIOTECA UADE ⚜       ║")
    print("╠══════════════════════════════╣")
    print("║ 1. Aumentar unidades         ║")
    print("║ 2. Disminuir unidades        ║")
    print("║ 0. Retroceder                ║")
    print("╚══════════════════════════════╝")