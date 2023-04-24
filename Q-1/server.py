import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# set the port number
port = 9999

# bind the socket to a public host and port
server_socket.bind((host, port))

# become a server socket
server_socket.listen(5)

# wait for a connection
print('Server listening on {}:{}'.format(host, port))
client_socket, address = server_socket.accept()

while True:
    # receive data from the client
    data = client_socket.recv(1024).decode('utf-8')
    if not data:
        break
    print('Received data: {}'.format(data))

    # send the data back to the client
    client_socket.send(data.encode('utf-8'))

## close the connection
#client_socket.close()
#server_socket.close()