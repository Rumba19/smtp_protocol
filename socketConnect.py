# step1_connect.py
from socket import socket, AF_INET, SOCK_STREAM

# 1) Choose a mail server
# For local testing: MailHog default listener
mailserver = ("localhost", 1025)

# 2) Create a TCP socket and connect
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

# 3) Read the server's 220 banner
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    raise RuntimeError('220 reply not received from server.')

# Keep socket open for next step
