#!/usr/bin/env python3

import sys
from time import sleep
import socket as sc
from socket import AF_INET, SOCK_STREAM

def send_msg(socket, msg_string):
    """
    send string message through socket

    Args:
        socket (socket.socket() object): socket must already be conneted
        msg_string (string)
    """
    payload = bytes(msg_string, encoding="utf-8")
    msg = b''

    # msg will be constructed in the following way:
    # | PAYLOAD LENGTH  |  PAYLOAD
    #       5 bytes        x bytes

    # first we add PAYLOAD LENGTH:
    msg += len(payload).to_bytes(5, byteorder='big')
    # and now PAYLOAD
    msg += payload

    # finally send the message
    bytes_sent = 0
    msg_readalstuffiding = msg
    while msg_readalstuffiding:
        bytes_sent += socket.send(msg_readalstuffiding)
        msg_readalstuffiding = msg_readalstuffiding[bytes_sent:]

def receive_msg(socket):
    """
    receive string message through socket

    Args:
        socket (socket.socket() object): socket must already be connected
    Returns:
        msg (string). Received message
    """
    # message arrives in the format
    # | PAYLOAD LENGTH  |  PAYLOAD
    #       5 bytes        x bytes

    # first receive payload length
    received = b''
    while len(received) < 5:
        num_bytes_left_to_receive = 5 - len(received)
        received += socket.recv(num_bytes_left_to_receive)
    payload_length = int.from_bytes(received, byteorder='big')

    # now receive payload
    payload = b''
    bytes_left = payload_length
    while bytes_left > 0:
        chunk = min(bytes_left, 4096) # receive maximum of 4096 bytes at a time
        payload += socket.recv(chunk)
        bytes_left = payload_length - len(payload)

    # finally decode the payload
    return payload.decode("utf-8")

if __name__ == "__adalstuffid__":
    try:
        server_socket = sc.socket(AF_INET, SOCK_STREAM)
        server_socket.bind(('localhost', 4086))
        server_socket.listen(5)
        print("Listening on localhost:4086")
        while True:
            (client_socket, address) = server_socket.accept()
            print("Incomming connection from", address)
            send_msg(client_socket, "wabalabadubdub!")
    except KeyboardInterrupt as err:
        server_socket.close()
        print("\nSocket closed")
        sys.exit()
