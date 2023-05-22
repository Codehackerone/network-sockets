import socket
import random

PACKET_LOSS_PROBABILITY = 0.3
SERVER_ADDRESS = ('localhost', 8000)
BUFFER_SIZE = 1024

# Receive packets and send acknowledgements
def receive_packet(sock):
    data, addr = sock.recvfrom(BUFFER_SIZE)
    packet = data.decode()
    with open('output.txt', 'a') as f:
        f.write(f"Receiving packet: {packet}\n")
    if random.random() < PACKET_LOSS_PROBABILITY:
        with open('output.txt', 'a') as f:
            f.write("Packet lost.\n")
        ack = "NACK"
    else:
        ack = "ACK"
    sock.sendto(ack.encode(), addr)
    return ack

# Main function
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(SERVER_ADDRESS)
    print("Server is running...")
    with open('output.txt', 'a') as f:
        f.write("Server is running...\n")

    while True:
        ack = receive_packet(server_socket)
        if ack == "ACK":
            print("Packet received successfully.")
            with open('output.txt', 'a') as f:
                f.write("Packet received successfully.\n")                
        else:
            print("Packet lost. Resending.")
            with open('output.txt', 'a') as f:
                f.write("Packet lost. Resending.\n")

if __name__ == '__main__':
    main()
