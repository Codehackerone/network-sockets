import socket
import threading

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# set the port number
port = 9998

# connect to the server
client_socket.connect((host, port))

def receive_messages():
    """Function to continuously receive messages from the server"""
    while True:
        try:
            # receive data from the server
            data = client_socket.recv(1024).decode('utf-8')
            print(data)
        except Exception as e:
            print('Error:', e)
            break

# create a new thread to continuously receive messages from the server
thread = threading.Thread(target=receive_messages)
thread.start()

while True:
    # get input from the user
    message = input()

    # send the input to the server
    client_socket.send(message.encode('utf-8'))
