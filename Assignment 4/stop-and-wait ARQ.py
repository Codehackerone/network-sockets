import time

# Define the window size for each method
WINDOW_SIZE = 1


# Define the sender and receiver processes
class Sender:
    def __init__(self, receiver):
        self.receiver = receiver
        self.sequence_number = 0

    def send(self, data):
        while True:
            # Send the packet to the receiver
            packet = f'{self.sequence_number}:{data}'
            print(f'Sender: Sending packet {packet}...')
            self.receiver.receive(packet)

            # Wait for the ACK from the receiver
            ack = self.receiver.get_ack()
            if ack == self.sequence_number:
                print(f'Sender: Received ACK {ack}.')
                self.sequence_number += 1
                break
            else:
                print(f'Sender: Received NAK {ack}. Resending packet...')
                time.sleep(1)


class Receiver:
    def __init__(self):
        self.expected_sequence_number = 0

    def receive(self, packet):
        # Simulate the packet being transmitted to the receiver
        print(f'Receiver: Received packet {packet}.')

        # Extract the sequence number from the packet
        sequence_number, data = packet.split(':')
        sequence_number = int(sequence_number)

        # If the packet is the expected packet, send an ACK
        if sequence_number == self.expected_sequence_number:
            print(f'Receiver: Sending ACK {sequence_number}.')
            self.expected_sequence_number += 1
            self.send_ack(sequence_number)
        else:
            print(f'Receiver: Sending NAK {self.expected_sequence_number}.')
            self.send_ack(self.expected_sequence_number)

    def send_ack(self, sequence_number):
        # Simulate the ACK being transmitted back to the sender
        time.sleep(1)
        print(f'Receiver: Sending ACK {sequence_number}...')
        self.last_ack = sequence_number

    def get_ack(self):
        return self.last_ack


# Define the sender and receiver processes
receiver = Receiver()
sender = Sender(receiver)

# Simulate the transmission of data
with open('input.txt', 'r') as f:
    data = f.read()
    words = data.split()
    for word in words:
        for c in word:
            sender.send(c)
