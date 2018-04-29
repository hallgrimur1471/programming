#!/usr/bin/env python3

from time import sleep
import socket as sc
from socket import AF_INET, SOCK_STREAM

from svarmi.sockets import send_msg, receive_msg

SERVER_IP = "192.168.228.30"
SERVER_PORT = 49604

client_socket = sc.socket(AF_INET, SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))
#send_msg(client_socket, "0123456789")
sleep(10)
client_socket.close()
