import socket
import threading

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# set the port number
port = 9998

# bind the socket to a public host and port
server_socket.bind((host, port))

# set the server to listen for incoming connections
server_socket.listen()

# list to store all the connected clients
clients = []

def handle_client(client_socket, client_address):
    """Function to handle each individual client connection"""
    print('Connected client:', client_address)

    # add the client to the list of clients
    clients.append(client_socket)

    # send a welcome message to the client
    client_socket.send('Welcome to the chat server!'.encode('utf-8'))

    while True:
        try:
            # receive data from the client
            data = client_socket.recv(1024).decode('utf-8')

            if not data:
                # if no data is received, remove the client from the list of clients
                clients.remove(client_socket)
                client_socket.close()
                print('Disconnected client:', client_address)
                break

            # send the received data to all the other connected clients
            for client in clients:
                if client != client_socket:
                    client.send(data.encode('utf-8'))

        except Exception as e:
            print('Error:', e)
            # if an exception occurs, remove the client from the list of clients
            clients.remove(client_socket)
            client_socket.close()
            print('Disconnected client:', client_address)
            break


while True:
    # accept a connection from a client
    client_socket, client_address = server_socket.accept()

    # create a new thread to handle the client connection
    thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    thread.start()
