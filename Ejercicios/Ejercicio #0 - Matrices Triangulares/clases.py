class Persona :
    def __init__(self,nombre):
        self nombre = nombre
    
    def imprimir(self):
        print("Hola, me llamo",self.nombre)


persona = Persona("Marisol")
persona.imprimir()

persona2 = Persona("Luis")
persona2.imprimir()

persona3 = Persona("Jose")
persona3.imprimir()