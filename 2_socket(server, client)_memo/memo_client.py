import socket


# Input the server's address. You can use hostname or ip address.
HOST = '127.0.0.1'  
# Port number assigned by the server.
PORT = 9999       


# Create a socket object.
# It uses IPv4 as the address family and TCP as the socket type.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Connect to the server using the specified HOST and PORT.
client_socket.connect((HOST, PORT))

# Send a message.


# Receive a message.

copy ='0'

while True:

    data = client_socket.recv(1024)

    if copy == data:
        continue
    else:
        print('Note content received from server', repr(data.decode()))
        
        copy = data
        # Input the local location of your notepad.
        f = open('helloClient.txt', 'w')
        f.write(data.decode())
        f.close()
    

# Close the socket.
client_socket.close()