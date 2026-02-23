from data.login import *
import random
import json, re
#--------------------- BUSQUEDAS DE LIBROS ---------------------
def busquedaLibroAutNom(archivo, nombre_autor, opcion):
    if opcion == 2:
        print(f"Buscando libros que contengan: '{nombre_autor}'")
    elif opcion == 1:
        print(f"Buscando libros del autor: '{nombre_autor}'")
    patron = re.compile(re.escape(nombre_autor), re.IGNORECASE)     
    with open(archivo, "r", encoding="UTF-8") as arch: 
        libros_encontrados = []
        for linea in arch:
            id, nombre, autor, stock, categoria = linea.strip().split(";")
            if opcion == 1: #AUTOR
                if patron.search(autor):
                    libros_encontrados.append([id, nombre, autor, stock, categoria])
            if opcion == 2: #NOMBRE
                if patron.search(nombre):
                    libros_encontrados.append([id, nombre, autor, stock, categoria])
    if libros_encontrados:
        print("Libros encontrados:")
        for libro in libros_encontrados:
            print(f"- {libro[1]} de {libro[2]} (ID: {libro[0]}), Stock: {libro[3]}, Categoría: {libro[4]})") 
    else:
        print("No se encontraron libros.")

def busquedaLibroID(archivo, id_libro, opcion):
    if opcion == 0: #Busqueda de préstamo
        print (f"Buscando préstamo con ID: {id_libro}")
        with open(archivo, "r", encoding="UTF-8") as arch:
            for linea in arch:
                id_prestamo, id_book, fecha_prestamo, legajo, fecha_devolucion, estado = linea.strip().split(";")
                if id_prestamo == id_libro and estado == "Activo":
                    print(f"Préstamo encontrado: ID {id_prestamo}, Libro ID: {id_book}, Fecha de préstamo: {fecha_prestamo}, Legajo: {legajo}, Fecha de devolución: {fecha_devolucion}")
                    return id_book, True
        print("No se encontró ningún préstamo activo con ese ID.")
        return False
    if opcion == 1: #Busqueda de libro
        print(f"Buscando libro con ID: {id_libro}")
        with open(archivo, "r", encoding="UTF-8") as arch:
            for linea in arch:
                id, nombre, autor, stock, categoria = linea.strip().split(";")
                if id == id_libro:
                    print(f"Libro encontrado: {nombre} (Autor: {autor}, Stock: {stock}, Categoría: {categoria})")
                    return True
        print("No se encontró ningún libro con ese ID.")
        return False

def chequearLibroRepite(archivo, nombre_libro):
    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            datos = linea.strip().split(";")
            if datos[1].lower() == nombre_libro.lower():
                print("El libro ya existe en el archivo.")
                return True
    return False


#--------------------- VALIDACIONES --------------------------

def validContraseña(contraseñaUsuario):
    tiene_mayuscula = False
    tiene_numero = False
    tiene_especial = False
    especiales = r"[^\w\s]"         # Cualquier carácter que no(^) sea alfanumérico(\w) o espacio(\s) ( Con tilde circunflejo ^ niega el conjunto w: alfa numérico y s: espacio)             
    errores = []

    if len(contraseñaUsuario) < 8:        
        errores.append("Debe tener al menos 8 caracteres.")

    for caracter in contraseñaUsuario:        
        if caracter.isupper():              
            tiene_mayuscula = True
        if caracter.isdigit():              
            tiene_numero = True
    if re.search(especiales, contraseñaUsuario):  
        tiene_especial = True

    if not tiene_mayuscula:                 
        errores.append("Debe contener al menos una letra mayúscula.")
    if not tiene_numero:
        errores.append("Debe contener al menos un número.")
    if not tiene_especial:
        errores.append("Debe contener al menos un carácter especial.")

    if errores:                   
        print("Contraseña inválida:")
        for error in errores:
            print(f"- {error}")
        return False        
    return True                 

def iniciar_sesion(archivo_json):
    import json
    nombre = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")
    try:
        with open(archivo_json, "r", encoding="utf-8") as f:
            socios = json.load(f)  
        for legajo, datos in socios.items():
            if datos["nombre"] == nombre:
                if datos["contrasena"] == contraseña:
                    print("✅ Inicio de sesión exitoso.")
                    return legajo, nombre
                else:
                    while datos["contrasena"] != contraseña:
                        contraseña = input("Contraseña incorrecta. Intente nuevamente: ")
                    print("✅ Inicio de sesión exitoso.")
                    return legajo, nombre
    except FileNotFoundError:
        print("El archivo de usuarios no existe.")
    except Exception as e:
        print("Error al leer el archivo:", e)
    print("❌ Usuario no encontrado.")
    return None, None

#--------------------- EXTRAS --------------------------
def retroceder_menu(opcion):
    print("Desea seguir operando?")
    print("1. Si")
    print("2. No")
    operando = input("Ingrese su opción: ")
    operando = expcepcionLetra(operando, 1, 2)
    if operando == 1 and opcion == 1:
        return True, False
    elif operando == 1 and opcion == 2:
        print("Regresando al menú de socio...")
        return True, True
    elif operando == 1 and opcion == 3:
        print("Regresando al menú de administrador...")
        return True, True
    elif operando == 2:
        print("Cerrando programa...")
        return False, False
    else:
        return False, False

def chequearStock(archivo, idLibro):
    with open(archivo, "r", encoding="UTF-8") as arch:
        for linea in arch:
            id, nombre, autor, stock, categoria = linea.strip().split(";")
            if id == idLibro:
                if int(stock) > 0:
                    print(f"El libro '{nombre} del {autor}' está disponible para préstamo.")
                    return True
                else:
                    print(f"El libro '{nombre} del {autor}' no está disponible en este momento.")
                    return False

def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
def validar_fecha(fecha):
    partes = fecha.split('/')
    if len(partes) != 3:
        return False 
    dia, mes, anio = partes
    if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
        return False
    dia = int(dia)
    mes = int(mes)
    anio = int(anio)
    if mes < 1 or mes > 12:
        return False
    dias_por_mes = [31, 29 if es_bisiesto(anio) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if dia < 1 or dia > dias_por_mes[mes - 1]:
        return False
    return True

def expcepcionLetra(opcion,inicio,fin):
    while True:
        try:
            opcion = int(opcion)
            if opcion < inicio or opcion > fin:
                raise ValueError("Opción fuera de rango.")
            return opcion
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, ingrese un número entre {inicio} y {fin}.")
            opcion = input("Ingrese su opción: ")

#-------------- ARCHIVOS .TXT ---------------
def leerArchivo(archivo, modo, opcion):
    try:
        if opcion == 1:
            arch = open(archivo, modo, encoding="UTF-8")
            linea = arch.readline().strip()
            print("ID".ljust(4) + "Nombre".ljust(35) + "Autor".ljust(30)  + "Stock".ljust(10) + "Categoria".ljust(30))
            print("-" * 125)  
            while linea:
                id, nombre, autor, stock, categoria = linea.split(";")
                print(f'{id:4}{nombre:35}{autor:30}{stock:10}{categoria:30}')
                linea = arch.readline().strip() 
        elif opcion == 2:
            arch = open(archivo, modo, encoding="UTF-8")
            linea = arch.readline().strip()
            print("ID_prest".ljust(10) + "ID_libro".ljust(10) + "Ini_prest".ljust(15)  + "Legajo".ljust(10) + "Fin_prest".ljust(15) + "Estado".ljust(10))
            print("-" * 73)  
            while linea:
                id_prest, id_libro, fecha_prestamo, legajo, fecha_devolucion, estado = linea.split(";")
                print(f'{id_prest:10}{id_libro:10}{fecha_prestamo:15}{legajo:10}{fecha_devolucion:15}{estado:10}')
                linea = arch.readline().strip() 
    except OSError:
            print("No se pudo leer el archivo")
    finally:
            try:
                arch.close()
            except:
                print("No se pudo cerrar el archivo")

def actualizarStock(archivo, idLibro, cantidad):
    try:
        with open(archivo, "r", encoding="UTF-8") as arch:
            nuevas_lineas = []
            actualizado = False
            for linea in arch:
                partes = linea.strip().split(";")
                if len(partes) == 5:
                    id, nombre, autor, stock, categoria = partes
                    if id == idLibro:
                        nuevo_stock = max(0, int(stock) - cantidad)
                        nuevas_lineas.append(f"{id};{nombre};{autor};{nuevo_stock};{categoria}\n")
                        actualizado = True
                    else:
                        nuevas_lineas.append(linea)
                else:
                    nuevas_lineas.append(linea)
        if actualizado:
            with open(archivo, "w", encoding="UTF-8") as arch_w:
                arch_w.writelines(nuevas_lineas)
        else:
            print("No se encontró el libro con ese ID.")
    except FileNotFoundError:
        print("Error: El archivo no existe.")
    except OSError as e:
        print(f"Error al abrir el archivo: {e}")

#----------------------- ARCHIVOS .JSON -----------------------
def cargar_json(nombre_archivo, nuevo_socio):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            socios = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        socios = {}
    if socios:
        nuevo_legajo = str(int(max(socios.keys(), key=int)) + 1)
    else:
        nuevo_legajo = "1"
    socios[nuevo_legajo] = nuevo_socio

    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(socios, f, ensure_ascii=False, indent=4)

def imprimir_socios_json():
    try:
        with open("Archivos/MatrizSocios.json", "r", encoding="utf-8") as f:
            socios = json.load(f)
        print("Legajo".ljust(10), "Nombre".ljust(20), "Correo".ljust(30), "Contraseña".ljust(20), "Estado".ljust(10))
        print("-" * 95)
        for legajo, datos in socios.items():
            print(
                str(legajo).ljust(10),
                datos["nombre"].ljust(20),
                datos["mail"].ljust(30),
                datos["contrasena"].ljust(20),
                datos["estado"].ljust(10)
            )
    except FileNotFoundError:
        print("El archivo no existe.")
    except json.JSONDecodeError:
        print("El archivo está vacío o tiene formato incorrecto.")

def buscarSocioJson(archivo, legajo):
    try:
        with open(archivo, "r", encoding = "utf-8") as arc:
            listadoSocios = json.load(arc)
            if str(legajo) in listadoSocios:
                socio = listadoSocios[str(legajo)]
                print(f"Legajo: {legajo}, Nombre: {socio['nombre']}, Correo: {socio['mail']}, Contraseña: {socio['contrasena']}")
                return True
            else:
                print(f"No se encontró el socio con legajo {legajo}.")
                return False
    except FileNotFoundError:
        print("Archivo no encontrado")
    except json.JSONDecodeError:
        print("El archivo está vacío o tiene formato incorrecto.")
    else:
        print("Error desconocido al intentar abrir el archivo.")
        return False

def modificarEstadoSocio(archivo, legajo):
    try:
        with open(archivo, "r", encoding="utf-8") as arc:
            listadoSocios = json.load(arc)
        if str(legajo) in listadoSocios:
            if listadoSocios[str(legajo)]["estado"] == "activo":
                nuevoEstado = "inactivo"
                listadoSocios[str(legajo)]["estado"] = nuevoEstado
            else:
                nuevoEstado = "activo"
                listadoSocios[str(legajo)]["estado"] = nuevoEstado
            with open(archivo, "w", encoding="utf-8") as arc:
                json.dump(listadoSocios, arc, ensure_ascii=False, indent=4)
            print(f"Estado del socio con legajo {legajo} modificado a '{nuevoEstado}'.")
            return True
        
    except FileNotFoundError:
        print("Archivo no encontrado")
    except json.JSONDecodeError:
        print("El archivo está vacío o tiene formato incorrecto.")
    else:
        print("Error desconocido al intentar abrir el archivo.")
        return False

def modificarEstadoPrestamo(archivo, id_prestamo):
    try:
        with open(archivo, "r", encoding="utf-8") as arc:
            nuevas_lineas = []
            linea = arc.readline()
            encontrado = False
            inactivo = False
            while linea:
                datos = linea.strip().split(";")
                if len(datos) == 6 and str(datos[0]) == str(id_prestamo):
                    if datos[5] == "Activo":
                        nuevo_estado = "Inactivo"
                        datos[5] = nuevo_estado
                        print(f"Estado del préstamo con ID {id_prestamo} modificado a '{nuevo_estado}'.")
                    else:
                        inactivo = True
                    encontrado = True
                nuevas_lineas.append(";".join(datos))
                linea = arc.readline()
        if inactivo:
            print("El préstamo ya está inactivo.")
            return False
        if encontrado:
            with open(archivo, "w", encoding="utf-8") as arc:
                for l in nuevas_lineas:
                    arc.write(l + "\n")
            return True
        else:
            print(f"No se encontró el préstamo con ID {id_prestamo}.")
            return False
    except FileNotFoundError:
        print("Archivo no encontrado")
    except Exception as e:
        print(f"Error al modificar el estado del préstamo: {e}")
        return False


#--------------------- CREAR CUENTA --------------------------
def crearCuenta(archivo):
    nombreUsuario = input("Ingresar Nombre de Usuario: ")
    contraseñaUsuario = input("Ingresar Contraseña: ")

    while not validContraseña(contraseñaUsuario):
        contraseñaUsuario = input("Ingresar contraseña válida: ")

    with open(archivo, "r", encoding="UTF-8") as arch:
        matrizBibliotecaSocios = json.load(arch)        
    ultimoLegajo = max(map(int, matrizBibliotecaSocios.keys()), default=0) + 1  
    mail = nombreUsuario.lower() + "@biblio.edu.ar"  

    matrizBibliotecaSocios[ultimoLegajo] = {           
        "nombre": nombreUsuario,
        "mail": mail,
        "contrasena": contraseñaUsuario,
        "estado": "activo"
        }
    cargar_json(archivo, matrizBibliotecaSocios[ultimoLegajo])
    print("✅ Socio creado con éxito:")
    print(f"Usuario: {nombreUsuario} | Email: {mail} | Legajo: {ultimoLegajo}")


#--------------------- OPCIONES SOCIO--------------------------
#SOCIO > BUSQUEDA
def buscarLibroSocio(archivo):
    bandera_busqueda = True
    bandera = True
    while bandera_busqueda and bandera:
        sub_menuBusqueda()
        sub_opcion = input("Ingrese su opción: ")
        sub_opcion = expcepcionLetra(sub_opcion, 0, 3)

        if sub_opcion == 1:
            nombreAutor = input("Ingrese el nombre del autor a buscar: ")
            busquedaLibroAutNom(archivo, nombreAutor, 1)
            bandera, bandera_busqueda = retroceder_menu(2)
        elif sub_opcion == 2:
            nombreLibro = input("Ingrese el nombre del libro a buscar: ")
            busquedaLibroAutNom(archivo, nombreLibro, 2)
            bandera, bandera_busqueda = retroceder_menu(2)
        elif sub_opcion == 3:
            id_libro = input("Ingrese el ID del libro a buscar: ")
            busquedaLibroID(archivo, id_libro, 1)
            bandera, bandera_busqueda = retroceder_menu(2)
        elif sub_opcion == 0:
            # Volver al menú de socio
            return True, True
    return bandera, bandera_busqueda


#SOCIO > MOSTRAR LIBRO
def mostrarLibrosSocio(archivo):
    while True:
        print("Mostrando la lista de libros:")
        leerArchivo(archivo, "r", 1)
        total_libros = contarLineasRecursivamente(archivo)
        print(f"Total de libros disponibles: {total_libros}")
        with open (archivo, "r", encoding="utf-8") as f:
            print("Total de libros en stock:", contar_stock_recursivo(f, total_libros))
        seguir_operando, bandera_back = retroceder_menu(2)
        break
    return seguir_operando, bandera_back

#SOCIO > PRESTAR LIBRO
def prestarLibroSocio(archivoLibros, archivoPrestamo, legajoUsuario):
    idLibro = input("Ingrese el ID del libro a buscar: ")
    busquedaLibroID(archivoLibros, idLibro, 1)
    if chequearStock(archivoLibros, idLibro):
        with open("Archivos/Prestamos.txt", "r", encoding="utf-8") as archivo:
            contador = 1
            linea = archivo.readline().strip()
            while linea != "":
                contador += 1
                linea = archivo.readline().strip()
        nuevo_id = contador
        fecha_prestamo = input("Ingrese la fecha de préstamo (DD/MM/AAAA): ")
        while not validar_fecha(fecha_prestamo):
            fecha_prestamo = input("Ingrese una fecha válida (DD/MM/AAAA): ")
        fecha_devolucion = input("Ingrese la fecha de devolución (DD/MM/AAAA): ")
        while not validar_fecha(fecha_devolucion):
            fecha_devolucion = input("Ingrese una fecha válida (DD/MM/AAAA): ")
        with open(archivoPrestamo, "a") as file:
            file.write(f"{nuevo_id};{idLibro};{fecha_prestamo};{legajoUsuario};{fecha_devolucion};Activo\n")
        actualizarStock(archivoLibros, idLibro, 1)
        print(f"✅ Préstamo exitoso. ID de préstamo: {nuevo_id}")
    else:
        print("❌ No hay stock disponible para este libro.")
    seguir_operando, bandera_back = retroceder_menu(2)
    return seguir_operando, bandera_back
#---------------------- OPCIONES ADMIN --------------------------
#ADMIN > BUSQUEDA
def adminOpcionesSocio(archivo):
    seguir_operando = True
    bandera_back = True
    while seguir_operando:
        subMenuAdmin_Socio()
        sub_opcion_admin = input("Ingrese su opción: ")
        sub_opcion_admin = expcepcionLetra(sub_opcion_admin, 0, 3)
        if sub_opcion_admin == 1:  # Dar de alta un socio
            nombreUsuario = input("Ingresar Nombre de Usuario a dar de alta: ")
            contraseñaUsuario = input("Ingresar Contraseña: ")
            while not(validContraseña(contraseñaUsuario)):
                contraseñaUsuario = input("Ingresar contraseña válida: ")
            dict_socio = {
                "nombre": nombreUsuario,
                "mail": nombreUsuario.lower() + "@biblio.edu.ar",
                "contrasena": contraseñaUsuario,
                "estado": "activo"
            }
            cargar_json(archivo, dict_socio)
            print("✅ Cuenta creada con éxito:")
            print(f"Usuario: {nombreUsuario} | Email: {nombreUsuario.lower() + '@biblio.edu.ar'}")
            seguir_operando, bandera_back = retroceder_menu(3)
        elif sub_opcion_admin == 2:  # Modificar estado de un socio
            bandera_usuario = True
            while bandera_usuario:
                legajoUsuario = input("Ingrese el número de legajo del socio a modificar el estado: ")
                legajoUsuario = expcepcionLetra(legajoUsuario, 120800, 150000)
                if buscarSocioJson(archivo, legajoUsuario):
                    print(f"¿Está seguro de que desea modificar el estado del socio con legajo {legajoUsuario}?")
                    print("1. Si")
                    print("2. No")
                    confirmacion = input("Ingrese su opción: ")
                    confirmacion = expcepcionLetra(confirmacion, 1, 2)
                    if confirmacion == 1:
                        modificarEstadoSocio(archivo, legajoUsuario)
                        print("✅ Modificado con éxito.")
                    elif confirmacion == 2:
                        print("❌ Modificación cancelada.")
                    bandera_usuario = False
                else:
                    print("❌ Legajo no encontrado. Intente nuevamente.")
            seguir_operando, bandera_back = retroceder_menu(3)
        elif sub_opcion_admin == 3:  # Ver listado de socios
            imprimir_socios_json()
            seguir_operando, bandera_back = retroceder_menu(3)
        elif sub_opcion_admin == 0:  # Volver al menú de administrador
            return True, True
        else:
            seguir_operando = False
    return seguir_operando, bandera_back

#ADMIN > LIBRO
def adminOpcionesLibro(archivo):
    seguir_operando = True
    bandera_back = True
    while seguir_operando:
        subMenuAdmin_Libro()
        sub_opcion_admin = input("Ingrese su opción: ")
        sub_opcion_admin = expcepcionLetra(sub_opcion_admin, 0, 6)
        if sub_opcion_admin == 1:
            bandera_busqueda = True
            while bandera_busqueda:
                sub_menuBusqueda()
                sub_opcion = input("Ingrese su opción: ")
                sub_opcion = expcepcionLetra(sub_opcion, 0, 3)
                if sub_opcion == 1:
                    nombreAutor = input("Ingrese el nombre del autor a buscar: ")
                    busquedaLibroAutNom(archivo, nombreAutor,1)
                    seguir_operando, bandera_back = retroceder_menu(3)
                elif sub_opcion == 2:
                    nombreLibro = input("Ingrese el nombre del libro a buscar: ")
                    busquedaLibroAutNom(archivo, nombreLibro,2)
                    seguir_operando, bandera_back = retroceder_menu(3)
                elif sub_opcion == 3:
                    id_libro = input("Ingrese el ID del libro a buscar: ")
                    busquedaLibroID(archivo, id_libro, 1)
                    seguir_operando, bandera_back = retroceder_menu(3)
                elif sub_opcion == 0:
                    bandera_busqueda  = False
            return seguir_operando, bandera_back
        elif sub_opcion_admin == 2:  # Dar de alta un libro
            nombreLibro = input("Ingrese el nombre del libro: ")
            if not chequearLibroRepite(archivo, nombreLibro):
                auxiliar = []
                nombreAutor = input("Ingrese el autor del libro: ")
                with open(archivo, "r") as archivo_r:
                    contador = 0
                    linea = archivo_r.readline().strip()
                    while linea != "":
                        contador += 1
                        linea = archivo_r.readline().strip()
                nuevo_id = contador + 1
                categoria = input("Ingrese la categoría del libro: ")
                auxiliar.append(["0"+str(nuevo_id), nombreLibro.title(), nombreAutor.title(), random.randint(1, 10), categoria.title()])
                lineas_existentes = []
                with open("Archivos/Libros.txt", "r", encoding="utf-8") as arch:
                    for linea in arch:
                        lineas_existentes.append(linea)
                if lineas_existentes and not lineas_existentes[-1].endswith('\n'):
                    lineas_existentes[-1] += '\n'
                with open("Archivos/Libros.txt", "w", encoding="utf-8") as arch:
                    for l in lineas_existentes:
                        arch.write(l)
                    for fila in auxiliar:
                        linea = ";".join(str(elemento) for elemento in fila)
                        arch.write(linea + "\n")
                print("Libro agregado con éxito.")
                return mostrarLibrosSocio("Archivos/Libros.txt")
            seguir_operando, bandera_back = retroceder_menu(3)
            return seguir_operando, bandera_back
        elif sub_opcion_admin == 3:  # Dar de baja un libro
            idLibro = input("Ingrese el ID del libro a dar de baja: ")
            if busquedaLibroID("Archivos/Libros.txt", idLibro, 1):
                auxiliar = []
                with open("Archivos/Libros.txt", "r", encoding="utf-8") as f:
                    for linea in f:
                        datos = linea.strip().split(";")
                        auxiliar.append(datos)
                libros_filtrados = [libro for libro in auxiliar if str(libro[0]) != str(idLibro) and str(libro[2]) != str(idLibro)]
                with open(archivo, "w", encoding="utf-8") as f:
                    for libro in libros_filtrados:
                        f.write(";".join(map(str, libro)) + "\n")
                print("Libro eliminado con éxito.")
            else:
                print("El libro no se encontró.")
            seguir_operando, bandera_back = retroceder_menu(3)
            return seguir_operando, bandera_back
        elif sub_opcion_admin == 4:  # Modificar un libro
            bandera_modificar = True
            while bandera_modificar:
                sub_menuModificar()
                opcion_modificar = input("Ingrese su opción: ")
                opcion_modificar = expcepcionLetra(opcion_modificar, 0, 3)
                if opcion_modificar == 0:
                    bandera_modificar = False
                    break
                elif opcion_modificar == 1: # Modificar nombre del libro
                    libros_actualizados = []
                    idLibro = input("Ingrese el ID del libro a modificar: ")
                    if busquedaLibroID(archivo, idLibro, 1):
                        nuevo_nombre = input("Ingrese el nuevo nombre del libro: ")
                        with open(archivo, "r", encoding="utf-8") as f:
                            for linea in f:
                                datos = linea.strip().split(";")
                                if datos[0] == str(idLibro):
                                    datos[1] = nuevo_nombre
                                libros_actualizados.append(";".join(datos))
                        with open(archivo, "w", encoding="utf-8") as archivo_w:
                            for libro in libros_actualizados:
                                archivo_w.write(libro + "\n")
                    else:
                        print("El libro no se encontró.")
                    bandera_modificar = False
                elif opcion_modificar == 2: # Modificar autor del libro
                    idLibro = input("Ingrese el ID del libro a modificar el autor: ")
                    if busquedaLibroID(archivo, idLibro, 1):
                        nuevo_autor = input("Ingrese el nuevo autor del libro: ")
                        libros_actualizados = []
                        with open(archivo, "r", encoding="utf-8") as f:
                            for linea in f:
                                datos = linea.strip().split(";")
                                if datos[0] == str(idLibro):
                                    datos[2] = nuevo_autor
                                libros_actualizados.append(";".join(datos))
                        with open(archivo, "w", encoding="utf-8") as archivo_w:
                            for libro in libros_actualizados:
                                archivo_w.write(libro + "\n")
                        print("Autor del libro modificado con éxito.")
                    else:
                        print("El libro no se encontró.")
                    bandera_modificar = False
                elif opcion_modificar == 3: # Modificar stock del libro
                    bandera_modificar_stock = True
                    while bandera_modificar_stock:
                        sub_menuModificarStock()
                        opcion_modificar_stock = input("Ingrese su opción: ")
                        opcion_modificar_stock = expcepcionLetra(opcion_modificar_stock, 0, 2)
                        if opcion_modificar_stock == 0:
                            bandera_modificar_stock = False
                            break
                        elif opcion_modificar_stock == 1: # Aumentar stock del libro
                            idLibro = input("Ingrese el ID del libro a aumentar stock: ")
                            if busquedaLibroID(archivo, idLibro, 1):
                                cantidad_aumentar = input("Ingrese la cantidad a aumentar: ")
                                cantidad_aumentar = expcepcionLetra(cantidad_aumentar, 0, 100000)
                                actualizarStock(archivo, idLibro, -cantidad_aumentar)
                                bandera_modificar_stock, bandera_modificar = False, False
                        elif opcion_modificar_stock == 2: # Disminuir stock del libro
                            idLibro = input("Ingrese el ID del libro a disminuir stock: ")
                            if busquedaLibroID(archivo, idLibro, 1):
                                cantidad_disminuir = input("Ingrese la cantidad a disminuir: ")
                                cantidad_disminuir = expcepcionLetra(cantidad_disminuir, 0, 100000)
                                actualizarStock(archivo, idLibro, cantidad_disminuir)
                                bandera_modificar_stock, bandera_modificar = False, False
            if opcion_modificar != 0:
                seguir_operando, bandera_back = retroceder_menu(3)
                return seguir_operando, bandera_back
        elif sub_opcion_admin == 5:  # Listar libros
            print("Mostrando la lista de libros:")
            leerArchivo(archivo, "r", 1)
            total_libros = contarLineasRecursivamente(archivo)
            print(f"Total de libros: {total_libros}")
            with open (archivo, "r", encoding="utf-8") as f:
                print("Total de libros en stock:", contar_stock_recursivo(f, total_libros))
            seguir_operando, bandera_back = retroceder_menu(3)
            return seguir_operando, bandera_back
        elif sub_opcion_admin == 0:  # Volver al menú de admin
            return True, True
        else:
            seguir_operando = False
    return seguir_operando, bandera_back

#ADMIN > PRESTAMO
def adminOpcionesPrestamo(archivo):
    seguir_operando = True
    bandera_back = True
    while seguir_operando:
        subMenuAdmin_Prestamo()
        sub_opcion_admin = input("Ingrese su opción: ")
        sub_opcion_admin = expcepcionLetra(sub_opcion_admin, 0, 2)  
        if sub_opcion_admin == 1:  # Ver listado de préstamos
            leerArchivo(archivo, "r", 2)
            seguir_operando, bandera_back = retroceder_menu(3)
            return seguir_operando, bandera_back
        elif sub_opcion_admin == 2:  # Devolver libro
            idPrestamo = input("Ingrese el ID del préstamo a devolver: ")
            resultado = busquedaLibroID("Archivos/Prestamos.txt", idPrestamo, 0)
            if resultado:
                idLibro, estado = resultado
                if estado:
                    actualizarStock("Archivos/Libros.txt", idLibro, -1)
                    if modificarEstadoPrestamo("Archivos/Prestamos.txt", idPrestamo):
                        print(f"✅ Préstamo devuelto correctamente.")
            seguir_operando, bandera_back = retroceder_menu(3)
            return seguir_operando, bandera_back
        elif sub_opcion_admin == 0:  # Volver al menú de admin
            return True, True
        else:
            seguir_operando = False
    return seguir_operando, bandera_back


#---------------------- RECURSIVIDAD --------------------------
def contar_stock_recursivo(archivo, lineas_restantes, stock_total=0):
    if lineas_restantes == 0:
        return stock_total
    linea = archivo.readline()
    partes = linea.strip().split(";") 
    if len(partes) == 5:
        try:
            stock = int(partes[3])
            stock_total += stock
        except ValueError:
            pass
    return contar_stock_recursivo(archivo, lineas_restantes - 1, stock_total)


def contarLineasRecursivamente(archivo,arch=["CERO"], contador =0):
    if arch == ["CERO"]:
        arch = open(archivo, "r", encoding="UTF-8")
    linea = arch.readline().strip()
    if linea:
        contador += 1
        return contarLineasRecursivamente(archivo, arch, contador)
    else:
        arch.close()
        return contador
