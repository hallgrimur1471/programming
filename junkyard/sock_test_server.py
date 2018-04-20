#!/usr/bin/env python3

import socket as sc
from socket import AF_INET, SOCK_STREAM

from svarmi.sockets import send_msg, receive_msg

SERVER_IP = "192.168.228.30"
SERVER_PORT = 49604

server_socket = sc.socket(AF_INET, SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen()
print("waiting for connections")
(client_socket, address) = server_socket.accept()
print("client_socket timeout: ", client_socket.gettimeout())
print("incomming connection from", address)
client_socket.settimeout(2)
print("start NAT")
try:
    client_socket.recv(4096)
except sc.timeout as e:
    print("Whoops!")
    print(e)
print("NAT BLOCKED")
print("start NAT2")
client_socket.recv(4096)
print("NAT BLOCKED")
receive_msg(client_socket)
print("did NAT block ...")
server_socket.close()
client_socket.close()
