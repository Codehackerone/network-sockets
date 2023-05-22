import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# get local machine name
host = socket.gethostname()

# set the port number
port = 9999

# bind the socket to a public host and port
server_socket.bind((host, port))

# print server address
print('Server listening on {}:{}'.format(host, port))

while True:
    # receive data from the client
    data, address = server_socket.recvfrom(1024)
    print('Received data from {}: {}'.format(address, data.decode('utf-8')))

    # reverse the data and send it back to the client
    reversed_data = data[::-1]
    server_socket.sendto(reversed_data, address)
