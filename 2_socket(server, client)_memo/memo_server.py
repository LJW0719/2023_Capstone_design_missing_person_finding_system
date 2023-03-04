import socket


# Input your server IP address 
HOST = ''

# Port number to wait for client access.
PORT = 9999        



# Create a socket object.
# It uses IPv4 as the address family and TCP as the socket type.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Necessary to solve WinError 10048 error 
# that cannot be connected because the port is in use.
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


# The bind function is used to bind a socket 
# to a specific network interface and port number.
# HOST can be a hostname, ip address, or the empty string "".
# An empty string allows connections from all network interfaces. 
# PORT can use a number between 1-65535. 
server_socket.bind((HOST, PORT))

# Server accept connections from clients.
server_socket.listen()

# accept Wait in the function and 
# return a new socket when a client connects.
client_socket, addr = server_socket.accept()

# Address of the connecting client.
print('Connected by', addr)

copy ='0'

# Infinite loop
while True:
    # Enter the local location of your notepad.
    f = open('hello.txt', 'r')
    s = f.read()
    f.close()
   
    if copy == s:
        continue
    else:
        print('Memo contents  ',s)
         # Send the contents of the notepad to the client.   
        copy = s
        client_socket.sendall(s.encode())


    
# Close the socket.
client_socket.close()
server_socket.close()
