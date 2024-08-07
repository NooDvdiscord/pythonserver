import socket

def start_server(host='0.0.0.0', port=12345):
    print(f"Start server on {host}:{port}...")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server is listening for connections...")
    client_socket, address = server_socket.accept()
    print(f"Connection from {address}")
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received data: {data}")
    client_socket.close()
if __name__ == "__main__":
    start_server()
input()
