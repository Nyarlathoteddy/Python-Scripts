import socket
import random

HOST = '127.0.0.1'
PORT = 8080

def GetTrivia():
    trivia_list = {
        'DNS': 'domain name system',
        'DHCP': 'dynamic host configuration protocol',
        'JBOD': 'just a bunch of disks',
        'SSH': 'secure shell',
        'SCP': 'secure copy',
        'BASH': 'born again shell',
        'SMTP': 'simple mail transfer protocol',
        'POP3': 'post office protocol',
        'PEBCAC': 'problem exists between computer and chair',
        'SATA': 'serial advanced technology attachment',
        'SSD': 'solid state drive',
        'OSPF': 'open shortest path first',
        'RIP': 'routing information protocol',
        'BGP': 'border gateway protocol',
        'PSU': 'power supply unit',
        'GPU': 'graphics processing unit',
        'CPU': 'central processing unit',
        'EIGRP': 'enhanced interior gateway routing protocol',
        'RAID': 'redundant array of independent disks',
        'IPS': 'intrusion prevention system',
        'IDS': 'intrusion detection system',
        'CIDR': 'classless inter-domain routing',
        'RAM': 'random access memory',
        'NAT': 'network address translation',
        'POST': 'power on self test',
        'BIOS': 'basic input output system',
        'ARP': 'address resolution protocol',
        'SNMP': 'simple network management protocol',
        'TCP': 'transmission control protocol',
        'UDP': 'user datagram protocol',
        'USB': 'universal serial bus',
        'VLAN': 'virtual local area network',
        'LAN': 'local area network',
        'WAN': 'wide area network',
        'VLSM': 'variable length subnet mask'
    }
    picked_item = random.choice(list(trivia_list.items())) # Get random key-value pair in trivia_list.
    return picked_item

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST,PORT))
    server.listen(1)
    conn, addr = server.accept()
    print(f"Connected by {addr}")
    total_counter = 0
    correct_counter = 0
    while True:
        trivia = GetTrivia()
        trivia_string = trivia[0] + ": Enter the acronym's meaning or quit to stop.\n"
        conn.send(trivia_string.encode("utf-8"))
        data = conn.recv(1024)
        data = data.decode("utf-8")
                
        if(data.lower() == trivia[1]):
            string = "Correct!\n"
            conn.send(string.encode("utf-8"))
            correct_counter += 1
            total_counter +=1
        else:
            string = "Wrong!\n"
            conn.send(string.encode("utf-8"))
            total_counter+=1
        score = f"\n{correct_counter} out of {total_counter} correct.\n\n"
        conn.send(score.encode("utf-8"))
