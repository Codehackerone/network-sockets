import random

# Constants
WINDOW_SIZE = 4
PACKET_LOSS_PROBABILITY = 0.2

# Simulate Selective Repeat ARQ protocol
def simulate_selective_repeat_arq(data):
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
        
        # Receive acknowledgements for sent packets, handle losses,
        # and selectively resend lost packets
        if sent_packets:
            acked_indices = []
            for index, (ack_num, _) in enumerate(sent_packets):
                if random.random() >= PACKET_LOSS_PROBABILITY:
                    print(f"Received ACK for packet {ack_num}")
                    acked_indices.append(index)
                else:
                    print(f"Packet {ack_num} lost, resending packet {ack_num}...")
                    seq_num = ack_num  # Reset sequence number to acknowledgment number
            
            # Iterate over all acked indices and remove corresponding packets from sent_packets
            for index in sorted(acked_indices, reverse=True):
                acked_packets.append(sent_packets.pop(index))
                
    # Print message indicating that all packets were successfully sent and acknowledged    
    print("\nAll packets sent and acknowledged successfully!")
# Test the simulation with a string of data
with open('input.txt', 'r') as file:
    data = file.read() # Read input data from file
    
if __name__ == "__main__":    
    simulate_selective_repeat_arq(data)
