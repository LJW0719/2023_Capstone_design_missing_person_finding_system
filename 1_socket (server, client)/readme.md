## 1. Socket (server, client)

+ The server receives the message from the client and prints it.

+ IP addresses of both echo_server.py and echo_client.py are your own IP address in your laptop.

### (1) Server

+ echo_server.py is used in your own laptop.

+ The IP and PORT bound address (addr) and the size of the buffer were set.

+ Important method: bind, listen, accept, recv, send

### (2) Client

+ echo_client.py is used in raspberry pie.

+ Important method: connect, send, recv

