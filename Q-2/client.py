import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# get local machine name
host = socket.gethostname()

# set the port number
port = 9999

while True:
    # send data to the server
    data = input('Enter data to send: ')
    client_socket.sendto(data.encode('utf-8'), (host, port))

    # receive the response from the server
    response, server_address = client_socket.recvfrom(1024)
    print('Received response from {}: {}'.format(server_address, response.decode('utf-8')))

# close the connection
client_socket.close()
