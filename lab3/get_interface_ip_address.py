#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 3
# This program is optimized for Python 2.7.
# It may run on any other version with/without modifications.

import argparse
import sys
import socket
import fcntl
import struct
import array


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Python networking utils')
    parser.add_argument('--ifname', action="store", dest="ifname", required=True)
    given_args = parser.parse_args() 
    ifname = given_args.ifname    
    print ("Interface [%s] --> IP: %s" %(ifname, get_ip_address(ifname)))       
    
# this script use --ifname as an argument and accordingly use the list of interfaces to get the ip address
# binded to that particular inteface so that if wifi0 is passed as an argument then it will show the ipaddress of the interface
# variable that neede dto be provided eis the interface name the parser module graceully breakdown input argument
# and passed it down to the program as a variable