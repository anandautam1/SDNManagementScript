#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 3
# This program is optimized for Python 2.7.
# It may run on any other version with/without modifications.

import argparse
import socket
import struct
import fcntl
import nmap

SAMPLE_PORTS = '21-23'

def get_interface_status(ip_address):
    nm = nmap.PortScanner()         
    nm.scan(ip_address, SAMPLE_PORTS)      
    return nm[ip_address].state()          

    
if  __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Python networking utils')
    parser.add_argument('--ifname', action="store", dest="ifname", required=True)
    given_args = parser.parse_args() 
    ifname = given_args.ifname    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip_address = socket.inet_ntoa(fcntl.ioctl(
        sock.fileno(),0x8915, struct.pack('256s', bytes(ifname[:15], 'utf-8')))[20:24])
    print ("Interface [%s] ip address is: %s and port %s is: %s" %(ifname, ip_address , SAMPLE_PORTS, get_interface_status(ip_address)))       

# ip_address = socket.inet_ntoa(fcntl.ioctl(sock.fileno(),0x8915, struct.pack('256s', ifname[:15]))[20:24])
# ensure that nmap is installed in the linux machine as the python binder wil require nmap as the interfacing from the terminal
# otherwise pip install python-nmap will install properly and execute the required interfacing
