# Trabajo Práctico I - Programación II

import os
from bibloteca import ejemplares_prestados, devolver_ejemplar_libro, menu, validacionOpcion, registrar_nuevo_libro, eliminar_ejemplar_libro, prestar_ejemplar_libro
from libro import nuevo_libro, generar_codigo

print("\nBienvenido!")
respuesta = ""




while respuesta != "salir":
    menu()
    opt = input("Ingrese la opción de menú:\n")
    os.system("cls")  # Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            ejemplares_prestados() 
        elif int(opt) == 2:
            devolver_ejemplar_libro()
        elif int(opt) == 3:
            registrar_nuevo_libro()
        elif int(opt) == 4:
            eliminar_ejemplar_libro()
        elif int(opt) == 5:
            prestar_ejemplar_libro()
        elif int(opt) == 6:
            respuesta = "salir"
        else:
            print("Ingrese una opción válida")
    else:
        print("Ingrese una opción numérica")
    # input("Presione cualquier tecla para continuar....")  # Pausa

print("Hasta luego!.")
