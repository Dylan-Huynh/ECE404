#!/bin/sh

#Homework Number: 9
#Name: Dylan Huynh
#ECN login: huynh38
#Due Date: 3/28/2023

# Flush and delete all previously define rules and chains
sudo iptables -t filter -F
sudo iptables -t filter -X
sudo iptables -t mangle -F
sudo iptables -t mangle -X
sudo iptables -t nat -F
sudo iptables -t nat -X
sudo iptables -t raw -F
sudo iptables -t raw -X

# Write a rule that only accepts packets that originate from f1.com.
sudo iptables -t filter -A INPUT -s f1.com -j ACCEPT

# For all outgoing packets, change their source IP address to your own machine’s IP address
sudo iptables -t nat -A POSTROUTING -j MASQUERADE

# Write a rule to protect yourself against indiscriminate and nonstop scanning of ports on your machine
sudo iptables -t filter -A FORWARD -p tcp --tcp-flags SYN,ACK,FIN,RST NONE -m limit --limit 1/s -j ACCEPT


# Write a rule to protect yourself from a SYN-flood Attack by limiting the number of incoming 
# 'new connection' requests to 1 per second once your machine has reached 500 requests.
sudo iptables -t filter -A FORWARD -p tcp --syn -m limit --limit 1/s --limit-burst 500 -j ACCEPT

# Write a rule to allow full loopback access on your machine i.e. access using localhost
sudo iptables -t filter -A INPUT -i lo -j ACCEPT
sudo iptables -t filter -A OUTPUT -o lo -j ACCEPT


# Write a port forwarding rule that routes all traffic arriving on port 8888 to port 25565. Make
# sure you specify the correct table and chain. Subsequently, the target for the rule should be
# DNAT.
sudo iptables -t nat -A PREROUTING -p tcp --dport 8888 -j REDIRECT --to-ports 25565


# Write a rule that only allows outgoing ssh connections to engineering.purdue.edu. You
# will need two rules, one for the INPUT chain and one for the OUTPUT chain on the FILTER
# table. Make sure to specify the correct options for the --state suboption for both rules.
sudo iptables -t filter -A INPUT -p tcp --dport 22 -s 128.46.104.20 -m state --state ESTABLISHED -j ACCEPT
sudo iptables -t filter -A OUTPUT -p tcp --dport 22 -d 128.46.104.20 -m state --state NEW,ESTABLISHED -j ACCEPT
#128.46.104.20

# Drop any other packets if they are not caught by the above rules.
sudo iptables -t filter -A INPUT -j DROP
sudo iptables -t filter -A OUTPUT -j DROP
sudo iptables -t filter -A FORWARD -j DROP