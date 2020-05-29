class Persona:
    
    def __init__(self, nombre, apellido, edad):
        super().__init__()
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        
    @property
    def nombre(self):
        '''
        Definirlo con property arriba me permite llamarlo sin los parentesis, y no permite modificarlo asi nomas.
        '''
        return self._nombre
    
    @nombre.setter
    def setNombre(self, nombre):
        self._nombre = nombre
        
        
yo = Persona('Joaquin', 'Fontela', 20)
print(yo.nombre)

