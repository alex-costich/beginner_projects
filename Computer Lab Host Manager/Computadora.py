class Computadora:
    def __init__(self, num, marca, modelo, ram, procesador, so):
        self.num = num
        self.marca = marca
        self.modelo = modelo
        self.ram = ram
        self.procesador = procesador
        self.so = so

    # MÉTODOS GET
    def get_num(self):
        return self.num
        
    def get_marca(self):
        return self.marca
    
    def get_modelo(self):
        return self.modelo
    
    def get_ram(self):
        return self.ram
    
    def get_procesador(self):
        return self.procesador
    
    def get_so(self):
        return self.so
        
        
    # MÉTODOS SET        
    def set_num(self, num):
        self.num = num
        
    def set_marca(self, marca):
        self.marca = marca
    
    def set_modelo(self, modelo):
        self.modelo = modelo
    
    def set_ram(self, ram):
        self.ram = ram
        
    def set_procesador(self, procesador):
        self.procesador = procesador
        
    def set_so(self, so):
        self.so = so