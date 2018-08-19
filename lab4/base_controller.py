from mininet.cli import CLI 
from mininet.net import Mininet 
from mininet.node import OVSController    

if'__main__' == __name__:     
    net = Mininet(controller=OVSController )        
    c0 = net.addController('c0', port=6633)     
    s1 = net.addSwitch('s1')          
    h1 = net.addHost('h1')     
    h2 = net.addHost('h2') 
 
    net.addLink(s1, h1)     
    net.addLink(s1, h2) 
 
    net.build()          
    c0.start()          
    s1.start([c0])          
    net.startTerms()     
    CLI(net)     
    net.stop()