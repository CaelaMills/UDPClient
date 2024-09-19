# Even though your UDP server is the file client2.py, you must always run the server first to have it
# listening so that when you run your UDP client, you can receive a response from the server that's
# listening to on the same socket.

# In this project, I wanted to advance the server, so that we can prevent injection attacks.
# We will do that by using 1) Sanitize Input, 2) Length Checks and 3) Whitelisting.

import socket  # Import the socket module to enable network communication
import re      # Import regex for sanitization. This library is used for working for "regular expressions" aka alpha,
# numerica and basic punctuation.

# Define the server address and port
host = "127.0.0.1"  # Localhost IP address
port = 80           # Port number for UDP communication
max_length = 1024 # The max length of data should be 1024 bytes. This is for length checks.
valid_commands = ["   COMMAND_A   "]  # Whitelisted the command(s) with whitespace
# Acceptable commands are put into a data format, a list. This is for whitelisting that allows pre-approved
# entities--like IP addresses or commands--to interact with a system, like a server.

# Create a UDP socket object
# 'AF_INET' stands for Address Family Internet Protocol Version 4, meaning we're using IPv4 addresses.
# 'SOCK_DGRAM' indicates that we are using UDP, which is a connectionless and unreliable protocol.
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the specified address and port
# This method makes the socket listen for incoming data on this address and port.
server.bind((host, port))  # This method binds your UDP socket to a specific address and port.

print(f"UDP Server is listening on {host}:{port}")  # Print a message indicating the server is active and listening

def sanitize_input(input_data):
    # Sanitize the input by removing unwanted characters that are not in the specified pattern.
    sanitized = re.sub(r'[^a-zA-Z0-9_ .,?!]', '', input_data)
    return sanitized

try:
    # Loop indefinitely to continuously handle incoming data
    while True:
        # Receive data from the client
        # 'server.recvfrom(4096)' listens for incoming UDP packets and returns a tuple containing
        # the data and the address of the sender. The buffer size is 4096 bytes.
        data, addr = server.recvfrom(4096)  # Buffer size of 4096 bytes

        if len(data) > max_length: # Length checks on incoming data by the number of bytes (or charatcers) there are in
            #that data.
            print("Received data exceeds maximum length")
            continue

        # Sanitize and normalize the incoming command
        cmd = sanitize_input(data.decode('utf-8'))

        # Check is command is valid
        if cmd not in valid_commands:
            print(f"Invalid command received from {addr}: {cmd}")
            continue

        # Process the valid command
        if cmd.strip() == "COMMAND_A":  # Check without whitespace
            response = b"This is test data. Please ignore."
            print(f"Sending response to {addr}: {response.decode('utf-8')}") # Print the received data and the sender's address

        # Decode the received data from bytes to a string for readability
        # 'data.decode('utf-8')' converts the byte data to a UTF-8 encoded string
        #print(f"Received data from {addr}: {data.decode('utf-8')}")  # Print the received data and the sender's address

        # Send a response to the client
        # 'server.sendto(response, addr)' sends a byte response to the client's address
        #response = b"Data received"  # Response message to send back to the client
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


