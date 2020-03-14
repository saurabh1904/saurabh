Socket_server code:

#Server side
import socket
def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000       

    server_socket = socket.socket()      
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))       

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()       
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())      

    conn.close()        

if __name__ == '__main__':
    server_program()

Socket_Client code:

#Client side 
import socket
def client_program():
    host = socket.gethostname()           
    port = 5000         

    client_socket = socket.socket()       
    client_socket.connect((host, port))      

    message = input(" -> ")      

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())        
        data = client_socket.recv(1024).decode()        

        print('Received from server: ' + data)     

        message = input(" -> ")     

    client_socket.close()     

if __name__ == '__main__':
    client_program()
