from mininet.node import CPULimitedHost
from mininet.topo import Topo 
from mininet.net import Mininet 
from mininet.log import setLogLevel, info 
from mininet.node import RemoteController 
from mininet.cli import CLI 
from mininet.link import TCLink 
class GenericTree(Topo):  
    """Simple topology example."""  
def __init__( self, depth=1, fanout=2 ):
        # Numbering: h1..N, s1..M   
            Topo.__init__(self)   
            self.hostNum = 1   
            self.switchNum = 1   
            # Build topology   
            self.addTree(depth, fanout)  
def addTree( self, depth, fanout ):   
    """Add a subtree starting with node n.   
    returns: last node added"""   
    isSwitch = depth > 0   
    if isSwitch:
        node = self.addSwitch( 's%s' % self.switchNum )
        self.switchNum += 1    
        for _ in range( fanout ):
                    child = self.addTree( depth - 1, fanout )     
                    self.addLink( node, child )   
                    
    else:    
        node = self.addHost( 'h%s' % self.hostNum )    
        self.hostNum += 1   
        return node 
        
def run():  
    c = RemoteController('c', '0.0.0.0', 6633)  
    # Change the args of GenericTree() to your desired values. You could even get them from command line.  
    net = Mininet(topo=GenericTree(depth=3, fanout=2), host=CPULimitedHost, controller=None)  
    net.addController(c)  
    net.start()  
    # installStaticFlows( net )  
    CLI(net)  
    net.stop()  
    # if the script is run directly (sudo custom/optical.py): 
if __name__ == '__main__':
    setLogLevel('info')  
    run() 
 
 