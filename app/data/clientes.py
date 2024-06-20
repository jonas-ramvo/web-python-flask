from app.data.modelo.cliente import Cliente

class Clientes:

    def select_all(self,db) -> list[Cliente]:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM clientes')
        clientes_en_db = cursor.fetchall()
        clientes : list[Cliente]= list()
        for cliente_en_db in clientes_en_db:
            clientes.append(Cliente(cliente_en_db[0], cliente_en_db[1], cliente_en_db[2], cliente_en_db[3], cliente_en_db[4],
                                    cliente_en_db[5],cliente_en_db[6],cliente_en_db[7]))

        cursor.close()
        return clientes
    

    def select_one(self,db,id_cliente) -> list[Cliente]:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM clientes WHERE id_cliente=%s',[id_cliente])
        clientes_en_db = cursor.fetchall()
        clientes : list[Cliente]= list()
        for cliente_en_db in clientes_en_db:
            clientes.append(Cliente(cliente_en_db[0], cliente_en_db[1], cliente_en_db[2], cliente_en_db[3], cliente_en_db[4],
                                    cliente_en_db[5],cliente_en_db[6],cliente_en_db[7]))

        cursor.close()
        return clientes
    

    def insert(self,db,dni,nombre,apellidos,genero,fecha_nacimiento,tlf_movil,direccion):
        cursor = db.cursor()
        sql = ("INSERT INTO clientes (dni,nombre,apellidos,genero,fecha_nacimiento,tlf_movil,direccion) values (%s,%s,%s,%s,%s,%s,%s) ")
        data = [dni,nombre,apellidos,genero,fecha_nacimiento,tlf_movil,direccion]
        cursor.execute(sql, data)
        db.commit() 


    def delete(self,db,id):
        cursor = db.cursor()
        sql = ("delete from clientes where id_cliente = %s ")
        data = [id]
        cursor.execute(sql, data)
        db.commit()


    def update(self,db,id_cliente,dni,nombre,apellidos,genero,fecha_nacimiento,tlf_movil,direccion):
        cursor = db.cursor()
        sql = ("update clientes set dni = %s, nombre = %s , apellidos = %s, genero = %s , fecha_nacimiento = %s , tlf_movil = %s , direccion = %s where id_cliente = %s ")
        data = [dni,nombre,apellidos,genero,fecha_nacimiento,tlf_movil,direccion,id_cliente]
        cursor.execute(sql, data)
        db.commit() 