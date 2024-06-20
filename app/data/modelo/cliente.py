class Cliente:
    def __init__(self,id_cliente:int,dni:str,nombre:str,apellidos:str,genero:str,fecha_nacimiento:str,tlf_movil:int,direccion:str):
        self.id_cliente = id_cliente
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.genero = genero
        self.fecha_nacimiento = fecha_nacimiento
        self.tlf_movil = tlf_movil
        self.direccion = direccion
        