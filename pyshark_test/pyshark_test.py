# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 16:55:48 2021

@author: Samir
"""

import pyshark

def print_live_dns():
    capture = pyshark.LiveCapture(interface="Wi-Fi", bpf_filter="udp port 53", display_filter="dns")
    for packet in capture:
        if "DNS" in packet and not packet.dns.flags_response.int_value:
            print(packet.dns.qry_name)
            
if __name__ == "__main__":
    print_live_dns()