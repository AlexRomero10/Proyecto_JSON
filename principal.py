import json
from funciones import *

with open("mundial2018.json") as fichero:
    datos=json.load(fichero)

while True:
    menu=('''OPCIONES:
    1- LISTAR INFORMACIÓN
    2- CONTAR INFORMACIÓN
    3- BUSCAR O FILTRAR INFORMACIÓN
    4- BUSCAR INFORMACIÓN RELACIONADA
    5- ÚLTIMO PARTIDO
    6- SALIR
    ''')

    print(menu)
    opcion=int(input("¿Qué acción desea realizar?: "))
    while opcion!=1 and opcion!=2 and opcion!=3 and opcion!=4 and opcion!=5 and opcion!=6:
        opcion=int(input("Error. Introduzca una opción del 1 al 6: "))

    #EJERCICIO 1
    if opcion==1:
        selecciones_locales= listar_informacion(datos)
        for elem in selecciones_locales:
            print(elem)
        print("\n")
    #EJERCICIO 2
    if opcion == 2:
        num_partidos = contar_informacion(datos)
        print(f"Nº DE PARTIDOS: {num_partidos}\n")


    #EJERCICIO 3
    if opcion==3:
        seleccion = input("Introduce el nombre de la selección en inglés: ")
        while not validar_selecciones(datos, seleccion):
            seleccion = input("No existe esta selección. Vuelve a intentarlo: ")
            print("\nRIVALES:")
        rivales = buscar_informacion(datos, seleccion)
        for rival in rivales:
            print(rival)
        
    #EJERCICIO 4
    if opcion ==4:
        pais = input("Introduce el nombre de un país: ")
        buscar_goles(pais)
        
    #EJERCICIO 5
    if opcion == 5:
        print("ATENCIÓN: Debes introducir el nombre de la selección en inglés.")
        seleccion = input("Selección: ")
        while not validar_selecciones(datos, seleccion):
            seleccion = input("No existe esta selección. Vuelva a intentarlo: ")
        fecha, partido, goles_descanso, goles = ejercicio_libre(datos, seleccion)
        print("FECHA\n", fecha[0], fecha[1])
        print("PARTIDO\n", partido[0], "-", partido[1])
        print("DESCANSO\n", goles_descanso[0], "-", goles_descanso[1])
        print("RESULTADO FINAL\n", goles[0], "-", goles[1], "\n\n")
    
    #Salir
    if opcion==6:
        print("Has seleccionado la opción 6:")
        print("SALIR")
        print("FIN DEL PROGRAMA")
        break