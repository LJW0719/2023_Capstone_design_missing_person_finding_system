## 1. Socket (server, client)

+ The server receives the message from the client and prints it.

+ IP addresses of both echo_server.py and echo_client.py are your own IP address in your laptop.

### (0) Socket network flow

![image](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FlRcp2%2FbtrrEUFw62k%2F5TBTR9g3jnvOWB3gDL0d31%2Fimg.jpg)

+ The waiting side is called the server, and the server opens the port and waits for the client to connect.

+ The connecting side is called the Client, and networks are linked by connecting to the IP and Port of the server.

+ Communication between the server and the client is exchanged in the form of Send and Receive.

+ After communication is over, it disconnects with close().

### (1) Server

+ echo_server.py is used in your own laptop.

+ The IP and PORT bound address (addr) and the size of the buffer were set.

+ Important method: bind, listen, accept, recv, send

### (2) Client

+ echo_client.py is used in raspberry pie.

+ Important method: connect, send, recv

Reference:
https://itholic.github.io/python-socket/
https://wildeveloperetrain.tistory.com/122
