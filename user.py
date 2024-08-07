import socket

def send_massage_to_server(host='127.0.0.1', port=12345, massage="Hello World!"):
    print(f"Connecting to server at {host}:{port}...")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Sending massage: {massage}")
    client_socket.sendall(massage.encode('utf-8'))
    client_socket.close()
    print("Message sent and connection close")

if __name__ == "__main__":
    send_massage_to_server()
input()