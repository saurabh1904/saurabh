Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
Socket_server code:

#Server side
import socket
def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000        # initiate port no above 1024

    server_socket = socket.socket()       # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))       # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()       # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())       # send data to the client

    conn.close()        # close the connection

if __name__ == '__main__':
    server_program()

Socket_Client code:

#Client side 
import socket
def client_program():
    host = socket.gethostname()            # as both code is running on same pc
    port = 5000         # socket server port number

    client_socket = socket.socket()        # instantiate
    client_socket.connect((host, port))       # connect to the server

    message = input(" -> ")        # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())         # send message
        data = client_socket.recv(1024).decode()        # receive response

        print('Received from server: ' + data)      # show in terminal

        message = input(" -> ")      # again take input

    client_socket.close()      # close the connection

if __name__ == '__main__':
    client_program()
