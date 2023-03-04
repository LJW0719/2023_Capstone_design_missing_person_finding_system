import socket

# set network information
IP = ''  # input your IP address
PORT = 5050
SIZE = 1024
ADDR = (IP, PORT)

# set server socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(ADDR)  # binding address
    server_socket.listen()  # preparation for client's request

    # entry infinite loop
    while True:
        client_socket, client_addr = server_socket.accept()  # wait to receive, return client information (socket, address)
        msg = client_socket.recv(SIZE)  # return message from the client
        print("[{}] message : {}".format(client_addr,msg))  # print message from the client

        client_socket.sendall("welcome!".encode())  # reply to the client

        client_socket.close()  # client socket termination