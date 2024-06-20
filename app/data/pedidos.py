from app.data.modelo.pedido import Pedido

class Pedidos:

    def select_one(self,db,id_cliente) -> list[Pedido]:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM pedidos WHERE id_cliente=%s',[id_cliente])
        pedidos_en_db = cursor.fetchall()
        pedidos : list[Pedido]= list()
        for pedido_en_db in pedidos_en_db:
            pedidos.append(Pedido(pedido_en_db[0],pedido_en_db[1], pedido_en_db[2], pedido_en_db[3], pedido_en_db[4], pedido_en_db[5], pedido_en_db[6]))

        cursor.close()
        return pedidos
    

    def select_all(self,db) -> list[Pedido]:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM pedidos')
        pedidos_en_db = cursor.fetchall()
        pedidos : list[Pedido]= list()
        for pedido_en_db in pedidos_en_db:
            pedidos.append(Pedido(pedido_en_db[0], pedido_en_db[1], pedido_en_db[2], pedido_en_db[3], pedido_en_db[4], pedido_en_db[5], pedido_en_db[6]))

        cursor.close()
        return pedidos
    

    def insert(self,db,fecha,articulo,cantidad,precio_unidad,precio_total,id_cliente):
        cursor = db.cursor()
        sql = ("INSERT INTO pedidos (fecha,articulo,cantidad,precio_unidad,precio_total,id_cliente) values (%s,%s,%s,%s,%s,%s) ")
        data = (fecha,articulo,cantidad,precio_unidad,precio_total,id_cliente)
        cursor.execute(sql, data)
        db.commit()
    

    def delete(self,db,id_pedido):
        cursor = db.cursor()
        sql = ("delete from pedidos where id_pedido = %s ")
        data = [id_pedido]
        cursor.execute(sql, data)
        db.commit()


    def update(self,db,id_pedido,fecha,articulo,cantidad,precio_unidad,precio_total):
        cursor = db.cursor()
        sql = ("update pedidos set fecha = %s, articulo = %s , cantidad = %s , precio_unidad = %s , precio_total= %s where id_pedido = %s ")
        data = [fecha,articulo,cantidad,precio_unidad,precio_total,id_pedido]
        cursor.execute(sql, data)
        db.commit() 