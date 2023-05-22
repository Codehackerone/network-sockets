import random

# Constants
WINDOW_SIZE = 4
PACKET_LOSS_PROBABILITY = 0.2

# Simulate Go-Back-N ARQ protocol
def simulate_go_back_n_arq(data):
    # Initialize sequence number, packets to be sent and acked
    seq_num = 0
    packets = [data[i:i+WINDOW_SIZE] for i in range(0, len(data), WINDOW_SIZE)]
    sent_packets = []
    acked_packets = []

    # Loop until all packets are sent and acknowledged
    while sent_packets or packets:
        # Send packets if there are any remaining packets and 
        # the window size is not exceeded
        if packets and len(sent_packets) < WINDOW_SIZE:
            packet = packets.pop(0)
            sent_packets.append((seq_num, packet))
            print(f"Sending packet {seq_num}: {packet}")
            seq_num += 1
            
        # Receive acknowledgements for sent packets with a 
        # probability of loss, and handle lost acknowledgements
        if random.random() >= PACKET_LOSS_PROBABILITY and sent_packets:
            ack_num, _ = sent_packets[0]
            if random.random() >= PACKET_LOSS_PROBABILITY:
                print(f"Received ACK for packet {ack_num}")
                acked_packets.append(sent_packets.pop(0))
            else:
                print(f"Packet {ack_num} lost, resending packets...")
                # Resend packets starting from the lost one
                seq_num = ack_num
                sent_packets.clear()
    
    # Print message indicating that all packets were successfully sent and acknowledged
    print("\nAll packets sent and acknowledged successfully!")

# Test the simulation with a string of data
data = "hello world!" * 10

if __name__ == "__main__":
    # Call function to simulate Go-Back-N ARQ protocol
    simulate_go_back_n_arq(data)
