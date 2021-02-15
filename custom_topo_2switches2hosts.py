#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.util import dumpNodeConnections

class MyTopo(Topo):

	def __init__(self):

	# Initialize topology

		Topo.__init__(self)

		# Add hosts and switches
		hostH1 = self.addHost('h1')
		hostH2 = self.addHost('h2')
		hostH3 = self.addHost('h3')
		hostH4 = self.addHost('h4')
		
		# AddSwitch
		switchS1 = self.addSwitch('s1')
		switchS2 = self.addSwitch('s2')

		# Add links
		self.addLink(hostH1, switchS1, bw=10, delay='5ms', max_queue_size=1000, use_htb=True)
		self.addLink(hostH2, switchS1, bw=10, delay='5ms', max_queue_size=1000, use_htb=True)
		self.addLink(switchS1, switchS2, bw=10, delay='5ms', max_queue_size=1000, use_htb=True)
		self.addLink(hostH3, switchS2, bw=10, delay='5ms', max_queue_size=1000, use_htb=True)
		self.addLink(hostH4, switchS2, bw=10, delay='5ms', max_queue_size=1000, use_htb=True)

topos = { 'mytopo': (lambda: MyTopo()) }