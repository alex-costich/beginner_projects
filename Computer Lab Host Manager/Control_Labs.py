from Computadora import Computadora

class Control_Labs:
    def __init__(self):
        self.laboratorios = []

    def agregar_compu(self, name_lab, num, marca, modelo, ram, procesador, so):
        #print("\n 1. A")
        #name_lab = str(input("Seleccione laboratorio."))
        self.name_lab = name_lab
        self.num = num
        self.marca = marca
        self.modelo = modelo
        self.ram = ram
        self.procesador = procesador
        self.so = so
        obj = Computadora(num, marca, modelo, ram, procesador, so)
        self.Intel1.append(obj)

    def buscar_compu(self, name_lab):
        tam_lista = len(self.name_lab)

        if tam_lista == 0:
            return print('\n Laboratorio Vacio')
        
        for i in range(tam_lista):
            if name_lab == self.name_lab[i].get_num():
                print("Laboratorio encontrado.")
                print(self.name_lab[i].get_num())
                #for para buscar el numero de equipo
            else:
                return print('No encontré la computadora.')
            
    def eliminar_compu(self, name_lab):
        tam_lista = len(self.name_lab)
        print('Tamaño de la lista: ',tam_lista)

        if tam_lista == 0:
            return '\n Laboratorio vacío.'
        
        for i in range(tam_lista):
            if name_lab == self.name_lab[i].get_nombre():
                print()
                print(self.name_lab[i].get_num())
                print(self.name_lab[i].get_marca())
                print(self.name_lab[i].get_modelo())
                print(self.name_lab[i].get_ram())
                print(self.name_lab[i].get_procesador())
                print(self.name_lab[i].get_so())
                del self.name_lab[i]
                return print('\n Computadora eliminada.')
            else:
                return print ('Este equipo no existe.')
            
Intel = Control_Labs()
        