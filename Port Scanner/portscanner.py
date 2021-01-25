# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:21:41 2021

This script is purely for own testing purposes. Use it for your own testing.
Doing port scanning on other people's websites without their permission is illegall.

@author: Samir
"""

import socket
import threading
from queue import Queue

target = '192.168.1.1' # Port scanning my router, use ipconfig to know your address and then use gateway address
queue = Queue()
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False 
    
#print(portscan(98))
        
# for port in range(1, 1024):
#     result = portscan(port)
#     if result:
#         print("Port {} is open!".format(port))
#     else:
#         print("Port {} is closed!".format(port))

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)
    
def worker():
    while not queue.empty():
        port = queue.get()
        if(portscan(port)):
            print("Port {} is open!".format(port))
            open_ports.append(port)

port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []

for t in range(500):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)
    
for thread in thread_list:
    thread.start()
    
for thread in thread_list:
    thread.join()
    
print("Open ports are: ", open_ports)