import socket
import time

PACKET_SIZE = 1 # Size of each packet in characters
TIMEOUT = 1 # Timeout duration in seconds
SERVER_ADDRESS = ('localhost', 8000) # Server address and port to send packets to
BUFFER_SIZE = 1024 # Size of buffer for receiving data from server


def generate_packets(data):
    """Function to generate packets from input data.

    Args:
        data (str): Input data string.

    Returns:
        list: List of packets created from the input data.
    """
    packets = []
    sequence_number = 0
    for char in data:
        packet = {
            'sequence_number': sequence_number,
            'data': char
        }
        packets.append(packet)
        sequence_number = 1 - sequence_number # Flip the sequence number between 0 and 1 for each packet
    return packets


def send_packet(sock, packet):
    """Function to send a packet and receive an ACK from the server.

    Args:
        sock (socket.socket): UDP socket object used for sending/receiving data.
        packet (dict): Packet to be sent.

    Returns:
        str: ACK received from the server.
    """
    data = "Sequence: " + str(packet['sequence_number']) + "; Data: " + packet['data'] # Create data string to be sent
    sock.sendto(data.encode(), SERVER_ADDRESS) # Send data to server
    print(f"Sending packet: {packet}") # Print sent packet details
    ack, addr = sock.recvfrom(BUFFER_SIZE) # Receive ACK from server
    ack = ack.decode() # Convert ACK byte string to regular string
    print(f"Received ACK: {ack}") # Print received ACK
    return ack


def send_data(data):
    """Function to send data packets.

    Args:
        data (str): Input data string to be sent.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create UDP socket object for client
    packets = generate_packets(data) # Generate packets from input data

    for packet in packets: # Loop over all packets
        ack = None
        while ack is None or ack == "NACK": # Resend if no ACK received or NACK received
            ack = send_packet(client_socket, packet) # Send the packet and receive an ACK
            if ack == "NACK":
                print("Packet lost. Resending.")
                # Simulate timeout by waiting for a certain period
                time.sleep(TIMEOUT)

    client_socket.close() # Close the socket when done


def main():
    with open('input.txt', 'r') as file:
        data = file.read() # Read input data from file
    send_data(data) # Send the input data


if __name__ == '__main__':
    main()
