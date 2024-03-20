#!/usr/bin/env python
# Eder Filho
# 19/12/2023
#SCRIPT PARA CONFIGURAÇÃO DE REDE - MESTRE

import os

#Verificação da quantidade de nós 
qtd_nos = int(input("Digite a quantidade de nós: "))

""" #Instalação dependências
os.system("apt-get install net-tools")
os.system("apt-get install ifupdown") 
os.system("apt-get install openssh-server")
os.system("apt-get install libopenmpi-dev")
os.system("apt-get install nfs-kernel-server") #apenas mestre
os.system("apt-get install nfs-common")
os.system("apt-get install portmap")
os.system("apt-get install build-essential") """

#Configurar rede 

#interfaces
#os.system("touch /etc/network/interfaces")
arquivo = open("/etc/network/interfaces", "a")
interfaces = list()
interfaces.append("auto enp0s3 \n")
interfaces.append("iface enp0s3 inet static \n")
interfaces.append("address 192.168.1.110 \n")
interfaces.append("netmask 255.255.255.0 \n")
interfaces.append("network 192.168.1.0 \n")
interfaces.append("broadcast 192.168.1.255 \n")
arquivo.writelines(interfaces)

#start placa de rede 
os.system("ifup enp0s3")

#hosts
arquivo = open("/etc/hosts", "a")
hosts = list()
hosts.append("127.0.1.1 mestre \n")
hosts.append("192.168.1.100 mestre\n")
arquivo.writelines(hosts)

i = 0
while i < qtd_nos:
    print(i)
    arquivo = open("/etc/hosts", "a")
    hosts_no = list()
    hosts_no.append("192.168.1.10")
    hosts_no.append(i)
    hosts_no.append("no")
    hosts_no.append(i)
    hosts_no.append("\n")
    arquivo.writelines(hosts_no)
    i = i+1
