import socket 

def get_remote_machine_info():
    #remote_host = 'www.python.org'
    #https://www.rmit.edu.au/
    remote_host = 'www.rmit.edu.au'
    try:
        # print("Remote Host name: %s" % remote_host)
        # print("IP address: %s" % socket.gethostbyname(remote_host))

        print("Remote Host name: %s" % remote_host)
        print("IP address: %s" % socket.gethostbyname(remote_host))

    except socket.error as err_msg:
        print("Error accesing %s: error number and detail %s" %(remote_host, err_msg))

if __name__ == '__main__':
    get_remote_machine_info()

# it retrieves the hostname for the website and perform a call to get the IP address 
# to modify to get the RMIT we have to change the remote host target site to www.rmit.edu.au
# then it will all change the way that the socket called the rmit site instead of the python.org site 