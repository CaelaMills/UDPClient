# Even though your UDP server is the file client2.py, you must always run the server first to have it
# listening so that when you run your UDP client, you can receive a response from the server that's
# listening on the same socket.

import socket  # Import the socket module to enable network communication

# Define the server address and port
host = "127.0.0.1"  # Localhost IP address
port = 80           # Port number for UDP communication

# Create a UDP socket object
# 'AF_INET' stands for Address Family Internet Protocol Version 4, meaning we're using IPv4 addresses.
# 'SOCK_DGRAM' indicates that we are using UDP, which is a connectionless and unreliable protocol.
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the specified address and port
# This method makes the socket listen for incoming data on this address and port.
server.bind((host, port))  # This method binds your UDP socket to a specific address and port.

print(f"UDP Server is listening on {host}:{port}")  # Print a message indicating the server is active and listening

try:
    # Loop indefinitely to continuously handle incoming data
    while True:
        # Receive data from the client
        # 'server.recvfrom(4096)' listens for incoming UDP packets and returns a tuple containing
        # the data and the address of the sender. The buffer size is 4096 bytes.
        data, addr = server.recvfrom(4096)  # Buffer size of 4096 bytes

        # Decode the received data from bytes to a string for readability
        # 'data.decode('utf-8')' converts the byte data to a UTF-8 encoded string
        print(f"Received data from {addr}: {data.decode('utf-8')}")  # Print the received data and the sender's address

        # Send a response to the client
        # 'server.sendto(response, addr)' sends a byte response to the client's address
        response = b"Data received"  # Response message to send back to the client
        server.sendto(response, addr)  # Send the response to the client
        print(f"Sent response to {addr}")  # Print a message indicating that the response was sent

except socket.error as e:
    # Handle socket errors
    # Print the error message if a socket error occurs
    print(f"Socket error: {e}")

finally:
    # Ensure the socket is closed
    # Close the socket to free up resources when done
    server.close()
    print("Server socket closed")  # Print a message indicating the socket has been closed
