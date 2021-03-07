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