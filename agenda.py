import json
import os

archivoJson = 'usuarios.json'

def agregarUsuario():
    nombre = input("ingresa el NOMBRE del usuario:  ")
    id = input("ingresa el ID del usuario:  ")
    email = input("ingresa el EMAIL del usuario:  ")
    phone = input("ingresa el PHONE del usuario:  ")

    nuevoUsuario = {
            "nombre": nombre,
            "id": id,
            "email": email,
            "phone": phone
        }

    try:
        with open(archivoJson, "r+", encoding="utf-8") as archivo:
            try:
                usuarios = json.load(archivo)
            except json.JSONDecodeError:
                usuarios = {'contactos':[]}
            
                usuarios.append(nuevoUsuario)
            archivo.seek(0)
            json.dump(usuarios, archivo, indent=4, ensure_ascii=False)
            print("Usuario agregado correctamente")

    except FileNotFoundError:
    
        with open(archivoJson, "w", encoding="utf-8") as archivo:
                    json.dump([nuevoUsuario], archivo, indent=4, ensure_ascii=False)
                    print("Archivo creado y usuario agregado correctamente.")

def mostrarJson():
     with open(archivoJson, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                
                print("Archivo creado y usuario agregado correctamente.")



menu = """
-------------------
1. Crear contactos
2. Mostrar
3. Actualizar
4. Eliminar
-------------------
"""

opcion = input("Ingresa la opción que deseas realizar: ")
while True:
    if opcion == '1':
        agregarUsuario()
    
