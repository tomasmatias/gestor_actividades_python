registros = [] # Creacion de listas

# Funcion de registro de datos

def agregar_registro():
    nombre = input("Ingrese el nombre: ")
    edad = input("Ingrese la edad: ")
    email = input("Ingrese el correo electrónico: ")
    registro = {
        "nombre": nombre,
        "edad": edad,
        "email": email
    }
    registros.append(registro)
    print("Registro agregado con éxito.")

# Funcion para imprimir registros en pantalla

def ver_registros():
    # si la condición es true, entonces se muestran los datos.
    if registros:
        print("Registros:")
        for i, registro in enumerate(registros, 1):
            print(f"Registro {i}:")
            print(f"Nombre: {registro['nombre']}")
            print(f"Edad: {registro['edad']}")
            print(f"Correo electrónico: {registro['email']}")
            print()
            # de lo contrario, se imprime un mensaje de que no existen registros.
    else:
        print("No hay registros.")

# Impresion de menu en pantalla.

def menu():
    print("=== Sistema de Registro ===")
    print("1. Agregar registro")
    print("2. Ver registros")
    print("3. Salir")

# Buclé while para mostrar las opciones del programa.

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_registro()
    elif opcion == "2":
        ver_registros()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
