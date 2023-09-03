from cod_generator import generar
# Crear un diccionario para cada libro
# ir creando diccionarios a medida de q ingresen nuevos libros
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}
# nota: interpretamos "cant_ej_ad" como cantidad de ejemplares a disposicion / disponibles
# y "cant_ej_pr" como cantidad de ejemplares prestados.
# en funcion de eso realizamos el resto del codigo. 
def nuevo_libro():
    
    titulo_libro = input("Ingrese el título del libro que desea registrar:\n")
    autor_libro = input("Ingrese el nombre de su autor/a:\n")
    adquiridos = int(input("Ingrese la cantidad de ejemplares adquiridos:\n"))
    while adquiridos < 1:
        adquiridos = int(input("Ingrese un número válido.\n"))
        if adquiridos > 0:
            break
    codigo = generar_codigo()

    titulo_libro = titulo_libro.title()
    autor_libro = autor_libro.title()

    registro = {
                "cod": codigo,
                "cant_ej_ad": adquiridos,
                "cant_ej_pr": 0,
                "titulo": titulo_libro,
                "autor": autor_libro,
                }

    print("\nResumen del registro:\n° Título:",titulo_libro)
    print("° Autor:", autor_libro)
    print("° Cantidad de ejemplares disponibles:", adquiridos)
    print("° Código de libro:", codigo)
    return registro
    

def generar_codigo():
    codigo_de_libro = generar()
    return codigo_de_libro