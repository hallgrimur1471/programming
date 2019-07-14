#!/usr/bin/env python3

import sys
import socket as sc
from socket import AF_INET, SOCK_STREAM

from socket_server import send_msg, receive_msg

try:
    client_socket = sc.socket(AF_INET, SOCK_STREAM)
    client_socket.connect(('localhost', 4086))
    msg = receive_msg(client_socket)
    print("Received message:", msg)
    client_socket.close()
except KeyboardInterrupt as err:
    client_socket.close()
    print("\nSocket closed")
    sys.exit()
