import json

biblioteca_usuarios = {
    120805: {"nombre": "Juana", "mail": "mail1@biblio.edu.ar", "contrasena": "contrasena1", "estado": "activo"},
    120806: {"nombre": "Pedro", "mail": "mail2@biblio.edu.ar", "contrasena": "contrasena2", "estado": "activo"},
    120807: {"nombre": "Tomas", "mail": "mail3@biblio.edu.ar", "contrasena": "contrasena3", "estado": "activo"},
    120808: {"nombre": "Lucas", "mail": "mail4@biblio.edu.ar", "contrasena": "contrasena4", "estado": "activo"},
    120809: {"nombre": "Santi", "mail": "mail5@biblio.edu.ar", "contrasena": "contrasena5", "estado": "activo"},
}
# FORMATO DICCIONARIO -> {ID: {"nombre": Nombre, "correo": Correo, "contrasena": Contraseña}}


try:
    archivo=open("MatrizSocios.json", "w")
    json.dump(biblioteca_usuarios, archivo)

except:
    print("No se pudo abrir el archivo")
finally:
    archivo.close() 
