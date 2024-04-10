import socket
from cs_config import host, port

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creación del socket
server_socket.bind((host, port)) # Vínculo del socket a puerto e ip
server_socket.listen(5) # Aceptar conexiones entrantes (máximo 5 clientes en espera)
print(f"Servidor escuchando en {host}:{port}") # Verificación de apertura
