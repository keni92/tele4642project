from mininet.cli import CLI
from mininet.link import Link
from mininet.link import TCLink
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.term import makeTerm

if '__main__' == __name__:
    net = Mininet(controller=RemoteController, autoStaticArp = True, autoSetMacs = True)

    c0 = net.addController('c0')


    s1 = net.addSwitch('s1')
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')
    net.addLink(h1, s1, port2 = 1)
    net.addLink(h2, s1, port2 = 2)
    net.addLink(h3, s1, port2 = 3)
    TCLink(h4, s1, 1, 4, bw = 1)
    TCLink(h4, s1, 2, 5, bw = 1) 

    net.build()
    net.startTerms()
    c0.start()
    s1.start([c0])
    s1.sendCmd('ovs-vsctl set bridge s1 protocols=OpenFlow13')
   
    #c0.cmd('ryu-manager ./bw_monitor_13.py')
    
    CLI(net)

    net.stop()

