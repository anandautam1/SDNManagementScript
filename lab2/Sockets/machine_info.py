import socket

def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print("Host name: %s" % host_name)
    print("IP address: %s" % ip_address)

if __name__ == '__main__':
    print_machine_info()

# the program use the socket module 
# functions in socket can be shown by the manual https://docs.python.org/3.4/library/socket.html 
# sethostname() set the machine hostname to name 
# send() send data to the socket. the socket must be connected to a remote socket.
