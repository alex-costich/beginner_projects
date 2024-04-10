from flask import Flask, render_template, request
from c_socket_manager import client_socket, send_data
import json

app = Flask(__name__) # Crea una nueva app web utilizando Flask

# -- RUTAS DE LA APLICACIÓN WEB -- #

@app.route("/")
def index(): # Página predeterminada
    return render_template("login2.html", permiso = True)

@app.route("/signIn", methods = ['GET', 'POST'])
def signIn(): # Iniciar sesión
    return render_template("signIn.html")

@app.route("/hacer_pedido", methods = ['GET'])
def hacer_pedido(): # Ordenar algo
    idmenu = request.args.get('menu_id','')
    registro = [idmenu, 4]
    print(registro) # Test
    data = json.dumps(registro)
    print("HOLAAAAA")
    client_socket.send(data.encode('utf-8'))
    menu = client_socket.recv(1024).decode('utf-8')
    print("ADIOSSSS")
    menu = json.loads(menu)
    print(menu) # Test
    
    return render_template("clientPage2.html", menus = menu)

@app.route("/registro", methods = ['GET'])
def registro(): # Registro de usuario nuevo
    # Obtener los parámetros de la solicitud GET
    verificarRango = request.args.get('verificado', '')
    print(f"\n\n{verificarRango}\n\n")
    admin = 1 if verificarRango == 'on' else 0
    username = request.args.get('nombre_usuario', '')  # Proporciona un valor predeterminado vacío si no se encuentra 'nombre_usuario'
    password = request.args.get('contrasena', '')  # Proporciona un valor predeterminado vacío si no se encuentra 'contrasena'
    nombre1 = request.args.get('nombre1', '')
    nombre2 = request.args.get('nombre2', '')
    apellidop = request.args.get('apellidop', '')
    apellidom = request.args.get('apellidom', '')
    telefono = request.args.get('telefono', '')
    correo = request.args.get('correo', '')
    usuario_nuevo = [[admin, 1, password, username, nombre1, nombre2, apellidop, apellidom, telefono, correo], 0]
    print(usuario_nuevo)  # Test
    data = json.dumps(usuario_nuevo)
    client_socket.send(data.encode('utf-8'))
    index()
    
    # flash('Registro exitoso', 'success')

    return render_template("login2.html", permiso = True)
        
@app.route("/procesar_login", methods = ["POST"])
def procesar_login(): # Procesamiento de los datos de inicio de sesión
    usuario = request.form["usuario"]
    contrasena = request.form["contrasena"]
    while True:
        message = [[usuario,contrasena],1]
        data = json.dumps(message)
        client_socket.send(data.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        response = json.loads(response)
        permiso = response[0]
        if permiso:
            menu = response[1]
            admin = response[2]
        else:
            admin = False
        # print(f"Respuesta del servidor: {response}") # Test
        if permiso == True and admin == True:
            return render_template("adminPage.html") # Despliega página de administrador
        elif permiso == True and admin == False:
            return render_template("clientPage2.html", menus = menu) # Despliega página de cliente
        else:
            return render_template ("login2.html") # Devuelve a la página de inicio de sesión y reinicia los campos rellenados

@app.route("/insert_menu", methods = ["POST"])
def insert_menu(): # Insertar producto
    print("1\n\n1\n1\n\n1")
    nombre_menu = request.form["nombre_menu"] # Nombre del producto
    descripcion = request.form["descripcion"] # Descripción
    precio = request.form["precio"] # Precio
    idturno = request.form["idturno"] # Turno para servicio
    URL_imagen = request.form["URL"] # Turno para servicio
    registro = [[nombre_menu, descripcion, precio, idturno,URL_imagen], 2]
    print(f"El registro es {registro}.") # Test

    data = json.dumps(registro)
    client_socket.send(data.encode('utf-8'))

    return render_template ("adminPage.html")

@app.route("/delete_menu", methods = ['GET'])
def delete_menu(): # Eliminar producto de la base de datos
    print("HOLAAA") # Test
    idmenu = request.args.get('menu_id', '')
    print(idmenu)
    registro = [idmenu, 5]
    data = json.dumps(registro) # Serializa los datos del menú
    client_socket.send(data.encode('utf-8')) # Envía los datos al servidor
    response = client_socket.recv(1024).decode('utf-8')
    response = json.loads(response)
    return render_template("tablasAdmin.html", menu_items = response)

@app.route("/tablasAdmin", methods = ['POST'])
def tablasAdmin(): # Carga la ventana de administrador con toda la info
    opc = [0, 3]
    data = json.dumps(opc) # Serializa los datos del menú
    client_socket.send(data.encode('utf-8')) # Envía los datos al servidor
    response = client_socket.recv(1024).decode('utf-8')
    response = json.loads(response)

    return render_template("tablasAdmin.html", menu_items = response)

@app.route("/pedidos")
def lista_pedidos(): # Lista de pedidos activos (admin)
    opc = [0, 6]
    data = json.dumps(opc) # Serializa los datos del menú
    client_socket.send(data.encode('utf-8')) # Envía los datos al servidor
    response = client_socket.recv(1024).decode('utf-8')
    response = json.loads(response)
    return render_template("pedidos.html", pedidos = response)

@app.route("/clientPage")
def clientPage(): # Página para pedidos del cliente
    opc = [0, 3]
    data = json.dumps(opc) # Serializa los datos del menú
    client_socket.send(data.encode('utf-8')) # Envía los datos al servidor
    response = client_socket.recv(1024).decode('utf-8')
    response = json.loads(response)
    return render_template("clientPage2.html", menus = response)

@app.route("/update_price", methods = ['GET'])
def update_price(): # Actualizar precio de producto
    new_price = request.args.get("new_price",'')
    idmenu = request.args.get('menu_id', '')
    opc = [[idmenu,new_price],7]
    print(opc)
    data = json.dumps(opc) # Serializa los datos del menú
    client_socket.send(data.encode('utf-8')) # Envía los datos al servidor
    response = client_socket.recv(1024).decode('utf-8')
    response = json.loads(response)
    tablasAdmin()
    return render_template("tablasAdmin.html", menu_items = response)

@app.route("/update_desc", methods = ['GET'])
def update_desc(): # Actualizar descripción de producto
    new_desc = request.args.get("new_desc",'')
    idmenu = request.args.get('menu_id', '')
    opc = [[idmenu,new_desc],9]
    print(opc)
    data = json.dumps(opc) # Serializa los datos del menú
    client_socket.send(data.encode('utf-8')) # Envía los datos al servidor
    response = client_socket.recv(1024).decode('utf-8')
    response = json.loads(response)
    tablasAdmin()
    return render_template("tablasAdmin.html", menu_items = response)

@app.route("/update_name", methods = ['GET'])
def update_name(): # Actualizar nombre de producto
    new_name = request.args.get("new_name",'')
    idmenu = request.args.get('menu_id', '')
    opc = [[idmenu,new_name],10]
    print(opc)
    data = json.dumps(opc) # Serializa los datos del menú
    client_socket.send(data.encode('utf-8')) # Envía los datos al servidor
    response = client_socket.recv(1024).decode('utf-8')
    response = json.loads(response)
    tablasAdmin()
    return render_template("tablasAdmin.html", menu_items = response)

@app.route("/delete_order", methods = ['GET'])
def delete_order(): # Eliminar pedido de la lista de pedidos (admin)
    print("HOLAAA") # Test
    idpedido = request.args.get('pedido', '')
    print(idpedido)
    registro = [idpedido, 8]
    data = json.dumps(registro) # Serializa los datos del menú
    client_socket.send(data.encode('utf-8')) # Envía los datos al servidor
    response = client_socket.recv(1024).decode('utf-8')
    response = json.loads(response)
    return render_template("pedidos.html", pedidos = response)

@app.route("/pedidosCliente")
def pedidosCliente(): # Lista de pedidos realizados por el cliente
    opc = [0, 11]
    data = json.dumps(opc) # Serializa los datos del pedido
    client_socket.send(data.encode('utf-8')) # Envía los datos al servidor
    response = client_socket.recv(1024).decode('utf-8')
    response = json.loads(response)

    return render_template("pedidosCliente.html", pedidos = response)

@app.route("/update_URL", methods = ['GET'])
def update_URL(): # Actualizar URL de imágen para producto
    new_desc = request.args.get("new_desc",'')
    idmenu = request.args.get('menu_id', '')
    opc = [[idmenu,new_desc],12]
    print(opc)
    data = json.dumps(opc) # Serializa los datos del pedido
    client_socket.send(data.encode('utf-8')) # Envía los datos al servidor
    response = client_socket.recv(1024).decode('utf-8')
    response = json.loads(response)
    tablasAdmin()
    return render_template("tablasAdmin.html", menu_items = response)

@app.route("/admin")
def admin(): # Página de administrador
    return render_template("adminPage.html")