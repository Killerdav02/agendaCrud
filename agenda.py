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
            
            usuarios["contactos"].append(nuevoUsuario)
            archivo.seek(0)
            json.dump(usuarios, archivo, indent=4, ensure_ascii=False)
            archivo.truncate()
            print("Usuario agregado correctamente")

    except FileNotFoundError:
    
        with open(archivoJson, "w", encoding="utf-8") as archivo:
                    json.dump({"contactos": [nuevoUsuario]}, archivo, indent=4, ensure_ascii=False)
                    print("Archivo creado y usuario agregado correctamente.")

def mostrarJson():
    if not os.path.exists(archivoJson):
        print("El archivo no existe. No hay contactos para mostrar.")
        return

    with open(archivoJson, "r", encoding="utf-8") as archivo:
        try:
            datos = json.load(archivo)
        except json.JSONDecodeError:
            print("El archivo está vacío o dañado.")
            return

        contactos = datos.get("contactos", [])
        if not contactos:
            print("No hay contactos guardados.")
            return

        print("\n--- Lista de Contactos ---")
        for i, contacto in enumerate(contactos, 1):
            print(f"{i}. Nombre: {contacto['nombre']}")
            print(f"   ID: {contacto['id']}")
            print(f"   Email: {contacto['email']}")
            print(f"   Teléfono: {contacto['phone']}")
            print("-" * 30)

def actualizarUsuario():
    if not os.path.exists(archivoJson):
        print("El archivo no existe. No hay contactos para actualizar.")
        return

    with open(archivoJson, "r+", encoding="utf-8") as archivo:
        try:
            datos = json.load(archivo)
        except json.JSONDecodeError:
            print("El archivo está dañado o vacío.")
            return

        contactos = datos.get("contactos", [])
        if not contactos:
            print("No hay contactos guardados.")
            return

        id_busqueda = input("Ingresa el ID del usuario que deseas actualizar: ")
        encontrado = False

        for contacto in contactos:
            if contacto["id"] == id_busqueda:
                print(f"Contacto encontrado: {contacto['nombre']}")
                nuevo_nombre = input("Nuevo nombre (deja vacío para no cambiar): ")
                nuevo_email = input("Nuevo email (deja vacío para no cambiar): ")
                nuevo_phone = input("Nuevo teléfono (deja vacío para no cambiar): ")

                if nuevo_nombre:
                    contacto["nombre"] = nuevo_nombre
                if nuevo_email:
                    contacto["email"] = nuevo_email
                if nuevo_phone:
                    contacto["phone"] = nuevo_phone

                encontrado = True
                break

        if encontrado:
            archivo.seek(0)
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
            archivo.truncate()
            print("Contacto actualizado correctamente.")
        else:
            print("No se encontró un contacto con ese ID.")

def eliminarUsuario():
    if not os.path.exists(archivoJson):
        print("El archivo no existe. No hay contactos para eliminar.")
        return

    with open(archivoJson, "r+", encoding="utf-8") as archivo:
        try:
            datos = json.load(archivo)
        except json.JSONDecodeError:
            print("El archivo está dañado o vacío.")
            return

        contactos = datos.get("contactos", [])
        if not contactos:
            print("No hay contactos guardados.")
            return

        id_busqueda = input("Ingresa el ID del usuario que deseas eliminar: ")
        nuevo_contactos = [c for c in contactos if c["id"] != id_busqueda]

        if len(nuevo_contactos) == len(contactos):
            print("No se encontró un contacto con ese ID.")
            return

        datos["contactos"] = nuevo_contactos
        archivo.seek(0)
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
        archivo.truncate()
        print("Contacto eliminado correctamente.")


def limpiarConsola():
    os.system('cls' if os.name == 'nt' else 'cls')

menu = """
-------------------
1. Crear contactos
2. Mostrar
3. Actualizar
4. Eliminar
-------------------
"""


while True:
    
    print(menu)
    opcion = input("Ingresa la opción que deseas realizar: ")

    if opcion == '1':
        limpiarConsola()
        agregarUsuario()
    elif opcion == '2':
        limpiarConsola()
        mostrarJson()
    elif opcion == '3':
        limpiarConsola()
        actualizarUsuario()
    elif opcion == '4':
        limpiarConsola()
        eliminarUsuario()
    elif opcion == '5':
        limpiarConsola()
        print("Saliendo del programa...")
        break
    else:
        limpiarConsola()
        print("Opción no válida. Intenta nuevamente.")
    
