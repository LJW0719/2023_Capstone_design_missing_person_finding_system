import socket

# set network information
SERVER_IP = ''  # input your IP address
SERVER_PORT = 5050
SIZE = 1024
SERVER_ADDR = (SERVER_IP, SERVER_PORT)

# set client socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(SERVER_ADDR)  # connect to the server
    client_socket.send('hi'.encode())  # send message to the server
    msg = client_socket.recv(SIZE)  # return message from the server
    print("resp from server : {}".format(msg))  # print message from the server