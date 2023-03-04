## 1. Socket (server, client)

+ The server receives the message from the client and prints it.

+ IP addresses of both echo_server.py and echo_client.py are your own IP address in your laptop.

### (0) Socket network flow

![image](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FlRcp2%2FbtrrEUFw62k%2F5TBTR9g3jnvOWB3gDL0d31%2Fimg.jpg)

+ 

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
