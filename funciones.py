def menu():
    menu=("Menu\n1.Listar la información\n2.Contar la información\n3.Buscar o filtrar información\n4.Buscar información relacionada\n5.Ejercicio Libre\n6.Salir")
    return(menu)

def ListarInformacion(datos):
    lista_nombres=[]
    nombres=datos.xpath("/vuxml/vuln/affects/package/name/text()")
    for programas in nombres:
        lista_nombres.append(nombres)
    return lista_nombres

def ContarInformacion(datos):
    nombres=datos.xpath("/vuxml/vuln/affects/package/name/text()")
    programasafectados=len(nombres)
    return programasafectados

def BuscarInformacion(nombre,datos):
    version=datos.xpath(f"/vuxml/vuln/affects/package[name/text()='{nombre}']/range/lt/text()")
    return version

def BuscarInformacionRelacionada(version,datos):
    vulnerabilidades=datos.xpath(f"/vuxml/vuln/affects/package/range[lt/text()='{version}']/../../../topic/text()")
    return vulnerabilidades

def EjercicioLibreDescripcion(nombre,datos):
    vulnerabilidades=datos.xpath(f"/vuxml/vuln/affects/package[name/text()='{nombre}']/../../topic/text()")
    return vulnerabilidades

def EjercicioLibreFecha(nombre,datos):
    fecha=datos.xpath(f"/vuxml/vuln/affects/package[name/text()='{nombre}']/../../dates/discovery/text()")
    return fecha