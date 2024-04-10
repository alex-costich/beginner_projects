import threading, json, sqlite3
from s_socket_manager import server_socket

def handle_client(client_socket):
    conn = sqlite3.connect("orderGenius.db") # Create a connection to the SQLite database outside the loop
    curs = conn.cursor() # Create a cursor object to interact with the database

    while True:
        data = client_socket.recv(1024).decode('utf-8') # Recibir datos del cliente

        if not data:
            break
        
        print(f"Recibido: {data}.") # Test
        
        data = json.loads(data)
        opc = data[1]
        
        if opc == 0: # Registro de usuario nuevo
            usuario_nuevo = data[0]
            print(f"{usuario_nuevo} ESTE ES EL USUARIO DE ")
            
            for item in usuario_nuevo:
                print(f"Object: {item}, Type: {type(item)}")

            print(f"{usuario_nuevo}\n\n\n ") # Test
            curs.execute(f"INSERT INTO Tusuarios (tipo, verificado, contrasena, nombre_usuario, nombre1, nombre2, apellidop, apellidom, telefono, correo) VALUES({int(usuario_nuevo[0])}, {int(usuario_nuevo[1])} ,'{usuario_nuevo[2]}','{usuario_nuevo[3]}','{usuario_nuevo[4]}','{usuario_nuevo[5]}', '{usuario_nuevo[6]}','{usuario_nuevo[7]}','{usuario_nuevo[8]}','{usuario_nuevo[9]}');")
            conn.commit()
            print(f"NuevoRegistro {usuario_nuevo}") # Test
            
        if opc == 1: # Inicio de sesión para usuario existente
            user = data[0][0]
            contra = data[0][1]

            curs.execute("SELECT nombre_usuario from Tusuarios")
            totalUsuarios = curs.fetchall()
            
            if user in [row[0] for row in totalUsuarios]: # Revisa si el usuario existe en la BDD
                curs.execute(f"select * FROM Tusuarios WHERE nombre_usuario = '{user}';") # Consulta de todos los datos del usuario especificado ({user})
                InfoUsuario = curs.fetchall()
                curs.execute("select * FROM Tmenus") # Prepara lista de productos para mostrarlos
                menus = curs.fetchall()

                if contra == InfoUsuario[0][3] and InfoUsuario[0][1] == 1: # Revisa si el usuario es admin
                    print("Contraseña correcta, es admin.")
                    message = [True, menus, True]
                    data = json.dumps(message)
                    client_socket.send(data.encode('utf-8'))

                elif contra == InfoUsuario[0][3] and InfoUsuario[0][1] == 0: # Si no es admin, revisa si el usuario es cliente
                    print("Contraseña correcta, es cliente.")
                    message = [True, menus, False]
                    data = json.dumps(message)
                    client_socket.send(data.encode('utf-8'))

                else: # Si no, el usuario no existe
                    message = [False]
                    data = json.dumps(message)
                    client_socket.send(data.encode('utf-8'))

        elif opc == 2: # Inserción de nuevo menú
            producto_nuevo = data[0]
            print(producto_nuevo)
            curs.execute(f"INSERT INTO Tmenus (nombre_menu, descripcion, precio, idturno, URL_imagen) VALUES('{producto_nuevo[0]}','{producto_nuevo[1]}',{producto_nuevo[2]},{producto_nuevo[3]},'{producto_nuevo[4]}');")
            conn.commit()
            print("Nuevo menú registrado.") # Test

        elif opc == 3: # Información de los menús
            curs.execute("SELECT * FROM Tmenus")
            menus = curs.fetchall()
            message = menus
            print("Hola") # Test
            data = json.dumps(message)
            client_socket.send(data.encode('utf-8'))
        
        elif opc == 4: # Pedidos
            print(data[0])
            pedido = int(data[0])

            curs.execute(f"select * FROM Tusuarios WHERE nombre_usuario = '{user}';") # Consulta de todos los datos del usuario especificado ({user})
            InfoUsuario = curs.fetchall()
            Id = InfoUsuario[0][0]
            
            print(Id) # Test

            curs.execute(f"INSERT INTO Tpedidos (idusuario, idmenu, cantidad, fecha) VALUES({Id}, {pedido}, 1, date('now'));")
            conn.commit()
            curs.execute("SELECT * FROM Tmenus")
            menus = curs.fetchall()

            print("Hola") # Test
            data = json.dumps(menus)
            client_socket.send(data.encode('utf-8'))
        
        elif opc == 5: # Eliminar menú
            print(data[0])
            print(type(data[0]))
            eliminarId = int(data[0])
            curs.execute(f"DELETE FROM Tmenus WHERE idmenu = {eliminarId};")
            conn.commit()
            curs.execute("SELECT * FROM Tmenus")
            menus = curs.fetchall()
            message = menus
            print("Hola") # Test
            data = json.dumps(message)
            client_socket.send(data.encode('utf-8'))

        elif opc == 6: # Información de los menús
            curs.execute("SELECT Tpedidos.idpedido, Tusuarios.nombre_usuario, Tmenus.nombre_menu, Tpedidos.cantidad, Tpedidos.fecha FROM Tpedidos JOIN Tusuarios ON Tpedidos.idusuario = Tusuarios.idusuario JOIN Tmenus ON Tpedidos.idmenu = Tmenus.idmenu;")
            pedidos = curs.fetchall()
            data = json.dumps(pedidos)
            client_socket.send(data.encode('utf-8'))
        
        elif opc == 7: # Actualizar precios
            print(data[0][0])
            idmenu = int(data[0][0])
            nuevoValor = int(data[0][1])
            curs.execute(f"UPDATE Tmenus SET precio = {nuevoValor} WHERE idmenu = {idmenu};")        
            conn.commit()
            curs.execute("SELECT * FROM Tmenus")
            menus = curs.fetchall()
            print("Hola precio") # Test
            data = json.dumps(menus)
            client_socket.send(data.encode('utf-8'))

        elif opc == 8: # Eliminar pedido
            print(data[0])
            print(type(data[0]))
            eliminarId = int(data[0])
            curs.execute(f"DELETE FROM Tpedidos WHERE idpedido = {eliminarId}")
            conn.commit()
            curs.execute("SELECT Tpedidos.idpedido, Tusuarios.nombre_usuario, Tmenus.nombre_menu, Tpedidos.cantidad, Tpedidos.fecha FROM Tpedidos JOIN Tusuarios ON Tpedidos.idusuario = Tusuarios.idusuario JOIN Tmenus ON Tpedidos.idmenu = Tmenus.idmenu;")
            pedidos = curs.fetchall()
            message = pedidos
            print("Hola") # Test
            data = json.dumps(message)
            client_socket.send(data.encode('utf-8'))

        elif opc == 9: # Actualizar descripción
            print(data[0][0])
            idmenu = int(data[0][0])
            nuevaDesc = data[0][1]
            curs.execute(f"UPDATE Tmenus SET descripcion = '{nuevaDesc}' WHERE idmenu = {idmenu};")        
            conn.commit()
            curs.execute("SELECT * FROM Tmenus")
            menus = curs.fetchall()
            print("Hola descripcion") # Test
            data = json.dumps(menus)
            client_socket.send(data.encode('utf-8'))

        elif opc == 10: # Actualizar nombres
            print(data[0][0])
            idmenu = int(data[0][0])
            nuevoNombre = data[0][1]
            curs.execute(f"UPDATE Tmenus SET nombre_menu = '{nuevoNombre}' WHERE idmenu = {idmenu};")        
            conn.commit()
            curs.execute("SELECT * FROM Tmenus")
            menus = curs.fetchall()
            print("Hola descripcion") # Test
            data = json.dumps(menus)
            client_socket.send(data.encode('utf-8'))

        elif opc == 11: # Información de los menús
            
            curs.execute(f"select * FROM Tusuarios WHERE nombre_usuario = '{user}';") # Consulta de todos los datos del usuario especificado ({user})
            InfoUsuario = curs.fetchall()
            Id = int(InfoUsuario[0][0])

            curs.execute(f"SELECT Tpedidos.idpedido, Tusuarios.nombre_usuario, Tmenus.nombre_menu, Tpedidos.cantidad, Tpedidos.fecha FROM Tpedidos JOIN Tusuarios ON Tpedidos.idusuario = Tusuarios.idusuario JOIN Tmenus ON Tpedidos.idmenu = Tmenus.idmenu WHERE Tusuarios.idusuario = {Id};")
            pedidos = curs.fetchall()
            data = json.dumps(pedidos)
            client_socket.send(data.encode('utf-8'))

        elif opc == 12: # Actualizar URL
            print(data[0][0])
            idmenu = int(data[0][0])
            nuevoURL = data[0][1]
            print(nuevoURL)
            curs.execute(f"UPDATE Tmenus SET URL_imagen = '{nuevoURL}' WHERE idmenu = {idmenu};")        
            conn.commit()
            curs.execute("SELECT * FROM Tmenus")
            menus = curs.fetchall()
            print("Hola descripcion") # Test
            data = json.dumps(menus)
            client_socket.send(data.encode('utf-8'))

    conn.commit() # Guarda cambios en la BDD
    conn.close() # Cierra conexión a la BDD
    client_socket.close() # Cierra conexión al cliente

client_connections = [] # Lista para almacenar las conexiones de los clientes

while True: # Acepta conexiones de los clientes
    client_socket, client_address = server_socket.accept()
    print(f"Conexión aceptada desde {client_address[0]}:{client_address[1]}") # Test
    client_connections.append(client_socket) # Agrega el socket del cliente a la lista de conexiones
    client_thread = threading.Thread(target = handle_client, args = (client_socket, )) # Establecer un hilo para manejar la comunicación con ese cliente
    client_thread.start() # Despliega el hilo