# EJERCICIO: Recetario Interactivo con Archivos
# Requerimientos:
# 1. Toda la información debe guardarse en el archivo "nuevas_recetas.txt"
# 2. El usuario puede:
#    - Ver todas las recetas.
#    - Agregar una nueva receta (se guarda en el archivo).
#    - Buscar recetas por posición.
#    - Salir del programa.
# 3. Se deben utilizar:
#    - Manejo de archivos con open(), read(), write(), y close().
#    - Bucles para el menú interactivo.
#    - Condicionales para controlar las opciones del menú.
#    - Manejo de excepciones (FileNotFoundError, IOError).
# 4. Todas las recetas están almacenadas como una receta por línea.



try:
    flag = True
    recetario = open("nuevas_recetas.txt", "r+") 
    if not recetario:
        raise FileNotFoundError

    while flag:
        print("1. Ver Recetas\n2. Agregar Receta\n3. Buscar Receta por posicion\n4. Salir")
        opcion = input("Ingrese su opcion: ")
        if opcion == "1":
            recetario.seek(0)
            contenido = recetario.read()
            print(contenido)
        elif opcion == "2":
            nueva_receta = input("Ingrese el nombre de la nueva receta: ")
            recetario.write(f"{nueva_receta}\n")
        elif opcion == "3":
            numero = int(input("Ingrese el numero de la receta que busca: "))
            recetas = recetario.readlines()
            print(recetas[numero])
        elif opcion == "4":  
            flag = False
        else:
            print("Numero no Valido.")
except FileNotFoundError: 
    print("El archivo no se encuentra")
except IOError:
    print("No se pudo leer/modificar el archivo")
finally:
    recetario.close()
