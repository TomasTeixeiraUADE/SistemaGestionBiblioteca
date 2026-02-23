from data.login import *
from data.funcionalidades import *

bandera = True
bandera_back = True
while bandera:
    # Mostrar el menú de inicio
    inicio()
    opcion = input("Ingrese su opción: ")
    opcion = expcepcionLetra(opcion, 0, 3)
    if opcion == 1:  # Crear cuenta
        bandera_back = True
        while bandera_back and bandera:
            crearCuenta("Archivos/MatrizSocios.json")
            bandera, bandera_back = retroceder_menu(1)
            if bandera and bandera_back:
                print("Regresando al menú de inicio...")
                break
    elif opcion == 2:  # Socios
        legajoUsuario, nombre = iniciar_sesion("Archivos/MatrizSocios.json")
        if nombre:
            bandera_back = True
            while bandera_back and bandera:
                menu_socio()
                variable = input("Ingrese su opción: ")
                variable = expcepcionLetra(variable, 0, 3)
                if variable == 1:  # Submenú de búsqueda de libros
                    bandera, bandera_back = buscarLibroSocio("Archivos/Libros.txt")
                elif variable == 2:  # Mostrar libros
                    bandera, bandera_back = mostrarLibrosSocio("Archivos/Libros.txt")
                elif variable == 3:  # Pedir libro
                    bandera, bandera_back = prestarLibroSocio("Archivos/Libros.txt", "Archivos/Prestamos.txt", legajoUsuario)
                elif variable == 0:  # Cerrar sesión
                    print("Cerrando sesión...")
                    break  # Sale del bucle de socio y vuelve al menú principal
    elif opcion == 3:  # Administrador
        legajoUsuario, nombre = iniciar_sesion("Archivos/MatrizAdmin.json")
        if nombre:
            bandera_back = True
            while bandera_back and bandera:
                menuAdmin()
                opcion_admin = input("Ingrese su opción: ")
                opcion_admin = expcepcionLetra(opcion_admin, 0, 3)
                if opcion_admin == 1:  # Submenú de administración de socios
                    bandera, bandera_back = adminOpcionesSocio("Archivos/MatrizSocios.json")
                elif opcion_admin == 2:  # Submenú de administración de libros
                    bandera, bandera_back = adminOpcionesLibro("Archivos/Libros.txt")
                elif opcion_admin == 3:  # Submenú de administración de préstamos
                    bandera, bandera_back = adminOpcionesPrestamo("Archivos/Prestamos.txt")
                elif opcion_admin == 0:
                    print("Cerrando sesión de administrador...")
                    break  # Sale del bucle de admin y vuelve al menú principal
    elif opcion == 0:  # Salir del programa
        print("Saliendo del programa...")
        bandera = False
    else:
        print("Opción inválida. Intente nuevamente.")