import socket 
from binascii import hexlify

def convert_ip4_address():
    for ip_addr in ['127.0.0.1', '192.168.0.1']:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print("IP address: %s => Integer: %s => Packed: %s, Unpacked: %s" % (ip_addr, packed_ip_addr, hexlify(packed_ip_addr),unpacked_ip_addr))

if __name__ == '__main__':
    convert_ip4_address()

# the output of the script is the ip address converted into different format 
# hexilify allows you to convert the string format into its hex representative for any valid number removes \x
# ntoa convert into numbers representative on the ntoa function number to its string 
