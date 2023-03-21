from TcpAttack import * #Your TcpAttack class should be named as TcpAttack

# Will contain actual IP addresses in real script
spoofIP='172.1.16.128' ; targetIP='172.217.1.110'
rangeStart = 1 ; rangeEnd = <int> ; port = 90
Tcp = TcpAttack(spoofIP,targetIP)
Tcp.scanTarget(rangeStart, rangeEnd)
if Tcp.attackTarget(port,10):
    print('port was open to attack')