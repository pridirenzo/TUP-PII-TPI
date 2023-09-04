import libro as l


# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios(libros[numero]) a la lista
# a medida de q se vayan adquiriendo
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

validacion = bool, False
op = str

def menu():
    print("-----------------------------------")
    print("1 - Gestionar Préstamo")
    print("2 - Gestionar Devolución")
    print("3 - Registrar nuevo libro")
    print("4 - Eliminar ejemplar")
    print("5 - Mostrar ejemplares prestados")
    print("6 - Salir")
    print("-----------------------------------")



def ejemplares_prestados():
    encontrado = False  # inicializo bandera en falso
    print("Ingrese código del libro a tomar prestado:")
    codigoIngresado = input()
    
    for libro in libros:
        if codigoIngresado == libro.get("cod"):
            encontrado = True
            print("-----------------------------------")
            print("Título:", libro["titulo"])
            print("Autor:", libro["autor"])
            
            if libro["cant_ej_ad"] > 0:
                print("Cantidad de ejemplares disponibles:", libro["cant_ej_ad"])
                print("-----------------------------------")
                print("Desea confirmar el préstamo? S/N")
                op = input()
                if op == "S":
                    nuevaCantidadDisponibles = libro["cant_ej_ad"] - 1
                    libro["cant_ej_ad"] = nuevaCantidadDisponibles
                    nuevaCantidadPrestados = libro["cant_ej_pr"] + 1 
                    libro["cant_ej_pr"] = nuevaCantidadPrestados
                    print("Su préstamo se ha realizado con éxito!")
                if op == "N":
                    print("Préstamo rechazado exitosamente")
                if op != "N" and op != "S":
                    print("ERROR. Opción inexistente") # aqui el usuario debe volver a ingresar la opcion 1, con la correspondiente respuesta
                
            if libro["cant_ej_ad"] == 0:
                print("No quedan ejemplares para prestar.")
                print("-----------------------------------")
                break 
           
    if encontrado != True:
        print("-----------------------------------") 
        print("ERROR: No se encontró el ejemplar.")
        print("-----------------------------------")

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    libros.append(nuevo_libro)


def eliminar_ejemplar_libro():
    eliminacion = input("Ingrese el código del ejemplar que desea eliminar.\n")
    posicion = 0
    bandera = False

    for busqueda in libros:
        if eliminacion == busqueda["cod"]:
            del libros[posicion]
            bandera = True
            break
        posicion += 1
    
    if bandera == False:
        print("¡Error! No se localizó ningun ejemplar con el código ingresado, reinténtelo.\n")
    else:
        print("El ejemplar fue eliminado con éxito.")
    


def prestar_ejemplar_libro():
    numero_ejemplar = 1
    for prestados in libros:
        print("Título del ejemplar n°", numero_ejemplar, ":", prestados["titulo"])
        if prestados["cant_ej_pr"] > 0:
            print("Cantidad de ejemplares prestados:", prestados["cant_ej_pr"])
            print()
        else: 
            print("No hubo ningun préstamo de este ejemplar.\n")
        numero_ejemplar += 1

def devolver_ejemplar_libro():
    print("Ingrese código del libro a devolver:")
    codigoIngresado = input()
    for libro in libros:
        if codigoIngresado == libro.get('cod'):
            encontrado = True
            if encontrado and libro['cant_ej_pr'] > 0:
                print("Desea confirmar la devolución? S/N")
                op = input()
                if op == "S":
                    nuevaCantidadPrestados = libro["cant_ej_pr"] - 1  # se devuelve un libro y disminuye la cant de libros q estan prestados
                    libro["cant_ej_pr"] = nuevaCantidadPrestados
                    nuevaCantidadDisponibles = libro["cant_ej_ad"] + 1 # como se devolvio un libro, ahora hay nuevo libro disponible
                    libro["cant_ej_ad"] = nuevaCantidadDisponibles
                    print("Devolución realizada correctamente")
                if op == "N":
                    print("Devolución rechazada exitosamente")
            if encontrado and libro['cant_ej_pr'] == 0:
                print("-----------------------------------") 
                print("ERROR: El libro no posee ejemplares prestados.")
                print("-----------------------------------")
    



