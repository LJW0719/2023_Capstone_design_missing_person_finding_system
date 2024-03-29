## Overview

From now on, I will explain the code that transmits the data of the notepad in real time using socket communication.

[Server - PC, Client - Raspberry Pi]

1. Socket communication connection success
2. Write the contents in the notepad on the server (PC)
3. Check the content in Notepad on the client (Raspberry Pi) (This content is the content written on the server is transmitted.)

## 1. socket(server, client)_memo

+ The server sends messages to the client.
+ The client receives messages and checks in their memopad.

### (1) memo_server
+ First, enter the cmd and input 'ipconfig' command to check your own IP address. (Based on Window)
+ In line 42 in "memo_server.py", Interpretation of "while" statements.
+ Set a variable called copy before the while statement.
+ Notepad will open and read "hello.txt".
+ If it is assigned to a variable called s and it is the same as the previously set copy, it continues and the lower line is not executed.
+ If the value assigned to the variable s is not the same as the preset copy (if a new one is written in the notepad), the contents are printed, the copy input value of s is entered, and sent to the client.
+ The reason why s is put here is that when it is repeated again, it must be the same as the condition of the if to print and send only once.

### (2) memo_client
+ First check the IP address of the server and enter it.
+ Execute "memo_client.py" in terminal. (Based on Linux)
+ Execute "while" loop as same as server.

## 2. Results
+ Attach a Raspberry Pi(Client) to the drone to test if it can communicate with a PC(Server) on the ground.
+ ![server_send](https://user-images.githubusercontent.com/117963984/222891202-5f278d58-973b-4c19-b979-fa11c63cc06d.jpg)
Figure01 - Server sends messages to the client(drone) periodically.
The memopad contents:
  +start : drone take off
  +3740 5m : 37m 40s (did not refer hour, just minutes and seconds.) and altitude 5 meters.
  +and so on..
  +3840 lannding : 38m 40s drone has landed.

+ ![client_receive](https://user-images.githubusercontent.com/117963984/222891174-5b4c068d-2adf-416b-bd44-2ee7c34a55f7.jpg)
Figure02 - Client(drone) receives messages to the server and it was recorded.


## Helpful Links
* https://seopseop911.tistory.com/26
