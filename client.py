import socket

target_host = "127.0.0.1" # "127.0.0.1" is your default/standard reserved loopback IP address for every local machine.
target_port = 80 # "80" is port 80 which is your typical port for HTTP but since we are creating a UDP client
# then we can utilize any port number. Hypertext Transfer Protocol or HTTP is a foundational protocol for
# formatting and transmitting data over web servers (think web pages and vms ***Client-Server Models)
# The 'client' (usually a web browser) makes requests to a server (a website or other resource) and
# the server responds with the requested data (message or action).

# Create a udp socket object
# 'AF_INET' stands for Address Family Internet Protocol Version 4, meaning, we want our socket to pull IPv4 addresses.
# 'SOCK_DGRAM' indicates our socket will use UDP which is a connectionless, unreliable protocol.
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Send some data
    client.sendto(b"This is test data. Please ignore.", (target_host, target_port))

    # Just for completeness...
    # Receive some data
    data,addr = client.recvfrom(4096)
    print("Received data:", data)
    print("From address:", addr)

except socket.error as e:
    # Handle socket errors
    print(f"Socket error: {e}")

finally:
    # Ensure the socket is closed
    client.close()
