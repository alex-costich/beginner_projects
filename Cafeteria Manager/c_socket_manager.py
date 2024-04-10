import socket, json
from cs_config import host, port

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

def send_data(data):
    data_str = json.dumps(data)
    client_socket.send(data_str.encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    return json.loads(response)
