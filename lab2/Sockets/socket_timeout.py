import socket 

def test_socket_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Default socket timeout: %s" % s.gettimeout())
    s.settimeout(100)
    print("Current socket timeout: %s" % s.gettimeout())

if __name__ == '__main__':
    test_socket_timeout()

# by default the socket doesn't have timeout so timeout needed to be programmed 
# so that it can gracefully exit if the client doesnt respond back etc 