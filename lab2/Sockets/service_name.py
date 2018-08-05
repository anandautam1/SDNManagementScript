import socket 

def find_service_name():
    protocolname = 'tcp'
    for port in [80,25,21,22,110]:
        print ("Port: %s => service name: %s" % (port, socket.getservbyport(port,protocolname)))    
    print ("Port: %s => service name: %s" % (53, socket.getservbyport(53,'udp')))

if __name__ == '__main__':
    find_service_name()

# the output is the service binded by the port and the service behind each port 
# the output is port 80 is http 25 is smtp and 53 is domain (DNS)
# the output port 21 -> ftp ; 22 -> ssh; 110 -> pop3
