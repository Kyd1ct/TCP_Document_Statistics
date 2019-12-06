'''
Name: TCP_Stat_Server.py
Desc: An example TCP Document Statistics Server
Auth: Martin Georgiev
Date: 1/12/19
'''

import socket  # Imports socket library

SERVER_HOST = 'localhost'  # Specifies the server is localhost
SERVER_PORT = 2000  # Specifies the server's port

# Opens the server socket (TCP)
SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binds server to the specified port and localhost
SERVER_SOCKET.bind((SERVER_HOST, SERVER_PORT))

# Set the server to listen for incoming messages
SERVER_SOCKET.listen()

# Set the server to accept the incoming messages
INCOMING_CONNECTION, CLIENT_ADDRESS = SERVER_SOCKET.accept()

# Server loop
while True:
    print('Server is up and running!')  # Message indicating the server is on

    # Receive incoming messages from the client address
    INCOMING_MESSAGE = INCOMING_CONNECTION.recv(4096)
    # Decode incoming message
    MESSAGE = INCOMING_MESSAGE.decode()
    # Get the length of the split decoded message (number of words)
    WORDS = len(MESSAGE.split())

    # Put all of the data inside a variable char and get the lenght of the message (number of characters)
    CHAR = ("Number of characters: " + str(len(MESSAGE)) + "\n" + "Number of words: " + str(WORDS))

    # Send the encoded message back to the client
    INCOMING_CONNECTION.sendall(CHAR.encode())

# Close the server socket
SERVER_SOCKET.close()