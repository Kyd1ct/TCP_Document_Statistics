'''
Name: TCP_Stat_Client.py
Desc: An example TCP Document Statistics Client
Auth: Martin Georgiev
Date: 1/12/19
'''

import socket  # Imports socket library

SERVER_HOST = 'localhost'  # Specifies the server is localhost
SERVER_PORT = 2000  # Specifies the server's port

# Opens the server socket (TCP)
CLIENT_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connects to the server
CLIENT_SOCKET.connect((SERVER_HOST, SERVER_PORT))

# Client loop
while True:
    # Input text file name (must be in the same directory)
    TEXT_FILE = input("What is the name of the text file: \n")

    # Add .txt in case user does not input file extension
    if '.' not in TEXT_FILE:
        TEXT_FILE = f"{TEXT_FILE}.txt"

    # Opens text file and reads it as bytes which removes the need of encoding
    with open(TEXT_FILE, "rb") as f:
        TEXT_FILE = f.read()

    # Sends the data to the server
    CLIENT_SOCKET.sendall(TEXT_FILE)

    # Receives the message from the server
    RECEIVED_MESSAGE, SERVER_ADDRESS = CLIENT_SOCKET.recvfrom(4096)

    # Prints the decoded message
    print(RECEIVED_MESSAGE.decode())

# Closes the server socket
CLIENT_SOCKET.close()