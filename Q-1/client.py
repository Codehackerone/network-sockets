import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# set the port number
port = 9999

# connect to the server
client_socket.connect((host, port))

while True:
    # send data to the server
    data = input('Enter data to send: ')
    client_socket.send(data.encode('utf-8'))

    # receive the response from the server
    response = client_socket.recv(1024).decode('utf-8')
    print('Received response: {}'.format(response))

## close the connection
# client_socket.close()
