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

# Create user-defined chain
sudo iptables -t filter -N firewall404.rules

# Write a rule that only accepts packets that originate from f1.com.
sudo iptables -A firewall.rules -s f1.com -j ACCEPT #figure out if -A is right

# For all outgoing packets, change their source IP address to your own machine’s IP address
sudo iptables -t nat -A POSTROUTING -o 0/0 -j MASQUERADE #super not done

# Write a rule to protect yourself against indiscriminate and nonstop scanning of ports on your machine
iptables -A FORWARD -p tcp --tcp-flags SYN,ACK,FIN,RST \
                        -m limit --limit 1/s -j ACCEPT


# Write a rule to protect yourself from a SYN-flood Attack by limiting the number of incoming 
# 'new connection' requests to 1 per second once your machine has reached 500 requests.
iptables -A FORWARD -p tcp --syn -m limit --limit 1/s -j ACCEPT #doesn't have 500 request featire

# Write a rule to allow full loopback access on your machine i.e. access using localhost
iptables -A INPUT -i $int_if -j ACCEPT #int_if is ambiguous


# Write a port forwarding rule that routes all traffic arriving on port 8888 to port 25565. Make
# sure you specify the correct table and chain. Subsequently, the target for the rule should be
# DNAT.


# Write a rule that only allows outgoing ssh connections to engineering.purdue.edu. You
# will need two rules, one for the INPUT chain and one for the OUTPUT chain on the FILTER
# table. Make sure to specify the correct options for the --state suboption for both rules.

# Drop any other packets if they are not caught by the above rules.
