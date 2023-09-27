from Control_Labs import Control_Labs

# MENÚ

p = 1
computadora = Control_Labs()

while(p):

    print("\n1 - Agregar computadora")
    print("\n2 - Buscar computadora")
    print("\n3 - Eliminar computadora")
    print("\n4 - Actualizar sistema operativo")
    print("\n5 - Agrandar la ram")
    print("\n6 - Salir")

    opcion = int(input("Ingresa la opcion a utilizar. "))
    if(opcion == 1):
        ##contacto.agregar_contacto()
        computadora.agregar_compu(name_lab = input("Nombre lab: "),num = int(input("Número de lab: ")),marca = input("Marca: "),modelo = input("Modelo: "),ram = int(input("Ram: ")),procesador = input("Procesador: "),so = input("Sistema operativo: "))
    elif(opcion == 2):
        computadora.buscar_compu(name_lab = input("Ingrese el nombre del laboratorio: "), num = int(input("Ingrese el número del equipo")))
    elif(opcion == 3):
        computadora.eliminar_compu(name_lab = input("Ingrese el nombre de laboratorio "),num = int(input("Ingrese el numero del equipo: ")))
    elif(opcion == 6):
        p = -1