import time

# Define the window size for the sender and receiver
WINDOW_SIZE = 4


# Define the sender and receiver processes
class Sender:
    def __init__(self, receiver):
        self.receiver = receiver
        self.base = 0
        self.next_sequence_number = 0
        self.packets = []

    def send(self, data):
        while True:
            if self.next_sequence_number < self.base + WINDOW_SIZE:
                # Send the packet to the receiver
                packet = f'{self.next_sequence_number}:{data}'
                print(f'Sender: Sending packet {packet}...')
                self.receiver.receive(packet)
                self.packets.append(packet)

                if self.base == self.next_sequence_number:
                    # Start the timer if the base packet is being sent
                    self.start_timer()

                self.next_sequence_number += 1
                time.sleep(1)
            else:
                print(f'Sender: Window is full. Waiting for acknowledgments...')
                self.wait_for_ack()

    def wait_for_ack(self):
        # Wait for acknowledgments for the sent packets
        while True:
            ack = self.receiver.get_ack()

            if ack >= self.base:
                # Update the base and remove acknowledged packets
                self.base = ack + 1
                self.packets = self.packets[self.base:]
                break

    def start_timer(self):
        # Start the timer for the base packet
        print('Sender: Starting timer...')
        time.sleep(3)
        self.timer_expired()

    def timer_expired(self):
        # Handle the case when the timer expires
        if self.base < self.next_sequence_number:
            print('Sender: Timer expired. Resending packets...')
            for packet in self.packets:
                print(f'Sender: Resending packet {packet}...')
                self.receiver.receive(packet)
                time.sleep(1)
            self.start_timer()


class Receiver:
    def __init__(self):
        self.expected_sequence_number = 0
        self.last_ack = -1

    def receive(self, packet):
        # Simulate the packet being transmitted to the receiver
        print(f'Receiver: Received packet {packet}.')

        # Extract the sequence number from the packet
        sequence_number, data = packet.split(':')
        sequence_number = int(sequence_number)

        if sequence_number == self.expected_sequence_number:
            # Accept the packet and send an ACK
            print(f'Receiver: Accepting packet {packet}.')
            self.expected_sequence_number += 1
            self.send_ack(sequence_number)
        else:
            # Discard the packet and send the last ACK
            print(f'Receiver: Discarding packet {packet}.')
            self.send_ack(self.last_ack)

    def send_ack(self, sequence_number):
        # Simulate the ACK being transmitted back to the sender
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
        # for c in word:
        sender.send(word)
