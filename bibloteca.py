import libro as l


# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios(libros[numero]) a la lista
# a medida de q se vayan adquiriendo
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

validacion = bool

def menu():
    print("-----------------------------------")
    print("1 - Gestionar Préstamo")
    print("2 - Gestionar Devolución")
    print("3 - Registrar nuevo libro")
    print("4 - Eliminar ejemplar")
    print("5 - Mostrar ejemplares prestados")
    print("6 - Salir")
    print("-----------------------------------")

op = input

def validacionOpcion():  # funcion agregada para validacion de opcion de confirmacion
    op = input()
    if op == "S" or op == "N":
        validacion = True
    else:
        validacion = False
        print("Ingrese una opción correcta")
        validacionOpcion()


    return validacion and op


def ejemplares_prestados():
    encontrado = False
    print("Ingrese código del libro a tomar prestado:")
    codigoIngresado = input()
    for libro in libros:
        if codigoIngresado == libro.get("cod"):
            encontrado = True
        if not encontrado:
            print("-----------------------------------") 
            print("ERROR: No se encontró el ejemplar.")
            print("-----------------------------------")
        if encontrado:
            print("-----------------------------------")  # si el codigo ingresado por el cliente coincide con el codigo de un libro real, entonces se muestran los datos
            print("Título:", libro["autor"])
            print("Autor:", libro["titulo"])
            if libro["cant_ej_ad"] == 0:
                print("No quedan ejemplares para prestar.")
                print("-----------------------------------") 
                print("\nIngrese la opción de menú:")
            if libro["cant_ej_ad"] > 0:
                print("Cantidad de ejemplares disponibles:", libro["cant_ej_ad"])
                print("-----------------------------------")
                print("Desea confirmar el préstamo? S/N")
                validacionOpcion()
                if validacion:
                    nuevaCantidadDisponibles = libro["cant_ej_ad"] - 1 # actualizo ejemplares prestados de dicho libro
                    libro["cant_ej_ad"] = nuevaCantidadDisponibles
                    break
                else:
                    break


def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    # completar
    return None


def eliminar_ejemplar_libro():
    # completar
    return None


def prestar_ejemplar_libro():
    # completar
    return None


def devolver_ejemplar_libro():
    encontrado = False
    print("Ingrese código del libro:")
    codigoIngresado = input()
    for libro in libros:
        if codigoIngresado == libro.get('cod'):
            encontrado = True
        else: 
            not encontrado
        if encontrado and libro['cant_ej_pr'] > 0:
            print("Desea confirmar la devolución? S/N")
            validacionOpcion()
            if validacion and op == "S":
                nuevaCantidadPrestados = libro["cant_ej_pr"] - 1  # se devuelve un libro y disminuye la cant de libros q estan prestados
                libro["cant_ej_pr"] = nuevaCantidadPrestados
                break
            else:
                break
        if encontrado and libro['cant_ej_pr'] == 0:
            print("-----------------------------------") 
            print("ERROR: El libro no posee ejemplares prestados.")
            print("-----------------------------------")
        if not encontrado:
            print("-----------------------------------") 
            print("ERROR: No se encontró el ejemplar.")
            print("-----------------------------------")
        


def nuevo_libro():
    # completar
    return None
