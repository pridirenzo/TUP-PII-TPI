# Trabajo Práctico I - Programación II

import os
from bibloteca import ejemplares_prestados, devolver_ejemplar_libro, menu, validacionOpcion

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
            # completar
            print()
        elif int(opt) == 4:
            # completar
            print()
        elif int(opt) == 5:
            # completar
            print()
        elif int(opt) == 6:
            respuesta = "salir"
        else:
            print("Ingrese una opción válida")
    else:
        print("Ingrese una opción numérica")
    # input("Presione cualquier tecla para continuar....")  # Pausa

print("Hasta luego!.")
