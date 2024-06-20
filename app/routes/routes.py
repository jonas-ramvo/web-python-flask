import random
from flask import Flask, Blueprint, render_template, request, redirect, url_for

from app import db
from app.data.clientes import Clientes
from app.data.pedidos import Pedidos


rutas_mitienda = Blueprint("routes", __name__)


@rutas_mitienda.route('/')
def index():
    return render_template('index.html')



@rutas_mitienda.route('/clientes')
def clientes():

    clientes = Clientes()
    lista_clientes = clientes.select_all(db)

    return render_template('clientes.html',lista=lista_clientes)



@rutas_mitienda.route('/insertarCliente', methods=['POST'])   
def insertarCliente():

    clientes = Clientes()

    dni = request.form['dni']
    nombre = request.form['nombre']
    apellidos = request.form['apellidos']
    genero = request.form['genero']
    fecha_nacimiento = request.form['fecha_nacimiento']
    tlf_movil = request.form['tlf_movil']
    direccion = request.form['direccion']



    if (dni == "" or nombre == "" or apellidos == ""   or genero == ""  or fecha_nacimiento == "" or tlf_movil == "" or direccion == ""):

        return render_template('error.html',error='Debes de rellenar todos los campos para insertar un cliente.')

    clientes.insert(db,dni,nombre,apellidos,genero,fecha_nacimiento,tlf_movil,direccion)

    return redirect(url_for('routes.clientes'))



@rutas_mitienda.route('/borrarCliente', methods=['POST'])   
def borrarCliente():

    clientes = Clientes()

    id_cliente = request.form['id_cliente']

    clientes.delete(db,id_cliente)
   
    return redirect(url_for('routes.clientes'))



@rutas_mitienda.route('/updateCliente', methods=['POST'])   
def updateCliente():

    clientes = Clientes()

    id_cliente = request.form['id_cliente']
    dni = request.form['dni']
    nombre = request.form['nombre']
    apellidos = request.form['apellidos']
    genero = request.form['genero']
    fecha_nacimiento = request.form['fecha_nacimiento']
    tlf_movil = request.form['tlf_movil']
    direccion = request.form['direccion']



    if (dni == "" or nombre == "" or apellidos == ""   or genero == ""  or fecha_nacimiento == "" or tlf_movil == "" or direccion == ""):

        return render_template('error.html',error='Debes de rellenar todos los campos para actualizar un cliente.')

    clientes.update(db,id_cliente,dni,nombre,apellidos,genero,fecha_nacimiento,tlf_movil,direccion)

    return redirect(url_for('routes.clientes')) 



@rutas_mitienda.route('/pedidos')
def pedidos():

    clientes = Clientes()
    lista_clientes = clientes.select_all(db)

    id_cliente= request.args.get('id_cliente')

    if id_cliente == None:

        pedidos = Pedidos()
        lista_pedidos = pedidos.select_all(db)

        return render_template('pedidos.html',lista=lista_clientes,lista2=lista_pedidos)

    else:

        clientes = Clientes()
        data_cliente = clientes.select_one(db,id_cliente)

        pedidos = Pedidos()
        lista_pedidos = pedidos.select_one(db,id_cliente)

        
        return render_template('pedidos.html',lista=lista_clientes,lista2=lista_pedidos,id_cliente=id_cliente,lista3=data_cliente)



@rutas_mitienda.route('/insertarPedido', methods=['POST'])   
def insertarPedido():

    pedidos = Pedidos()

    fecha = request.form['fecha']
    articulo = request.form['articulo']
    cantidad = request.form['cantidad']
    precio_unidad = request.form['precio_unidad']
    precio_total = request.form['precio_total']
    id_cliente = request.form['id_cliente']

    id_cliente2 = request.args.get('id_cliente')


    if (id_cliente == "" or articulo == "" or fecha == ""   or cantidad == ""  or precio_unidad == "" or precio_total == ""):

        return render_template('error.html',error='Debes de rellenar todos los campos para insertar un pedido.')

    pedidos.insert(db,fecha,articulo,cantidad,precio_unidad,precio_total,id_cliente)

    return redirect(url_for('routes.pedidos',id_cliente=id_cliente2))   



@rutas_mitienda.route('/borrarPedido', methods=['POST'])   
def borrarPedido():

    pedidos = Pedidos()

    id_pedido = request.form['id_pedido']

    id_cliente = request.args.get('id_cliente')

    pedidos.delete(db,id_pedido)
   
    return redirect(url_for('routes.pedidos',id_cliente=id_cliente)) 



@rutas_mitienda.route('/updatePedido', methods=['POST'])   
def updatePedido():

    pedidos = Pedidos()

    id_pedido = request.form['id_pedido']
    fecha = request.form['fecha']
    articulo = request.form['articulo']
    cantidad = request.form['cantidad']
    precio_unidad = request.form['precio_unidad']
    precio_total = request.form['precio_total']
    id_cliente = request.args.get('id_cliente')


    if (id_pedido == "" or articulo == "" or fecha == ""   or cantidad == ""  or precio_unidad == "" or precio_total == ""):

        return render_template('error.html',error='Debes de rellenar todos los campos para actualizar un pedido.')

    pedidos.update(db,id_pedido,fecha,articulo,cantidad,precio_unidad,precio_total)

    return redirect(url_for('routes.pedidos',id_cliente=id_cliente))   
