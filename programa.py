from lxml import etree
from funciones import *
datos = etree.parse('proyecto.xml')

print(menu())
opcion=int(input("Elige una opción: "))

while opcion!=6:
    
    if opcion==1:
        for info in ListarInformacion(datos):
            print(info)
        opcion=int(input("Elige una opción: "))
    
    elif opcion==2:
        print(f"Se tiene registro de {ContarInformacion(datos)} programas afectados.")
        opcion=int(input("Elige una opción: "))
    
    elif opcion==3:
        nombre=input("Introduce el nombre del programa que se desea buscar: ")
        print("Las versiones del programa que son vulnerables son las siguientes: ")
        for info in BuscarInformacion(nombre,datos):
            print(info, " ",end="")
        opcion=int(input("\nElige una opción: "))
    
    elif opcion==4:
        version=input("Introduce el nombre de la versión que se desea buscar: ")
        print("La descripción de la vulnerabilidad es: ")
        for info in BuscarInformacionRelacionada(version,datos):
            print(info," ",end="")
        opcion=int(input("\nElige una opción: "))