#!/usr/bin/env python
# Eder Filho
# 19/12/2023
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - ARQUIVO INTERFACES

import os

#interfaces
#os.system("touch /etc/network/interfaces")
arquivo = open("/etc/network/interfaces", "a")
interfaces = list()
interfaces.append("auto enp0s3 \n") #verificar nome da placa
interfaces.append("iface enp0s3 inet static \n") #verificar nome da placa
interfaces.append("address 192.168.1.110 \n") #modificar para cada nó
interfaces.append("netmask 255.255.255.0 \n")
interfaces.append("network 192.168.1.0 \n")
interfaces.append("broadcast 192.168.1.255 \n")
arquivo.writelines(interfaces)

#start placa de rede 
os.system("ifup enp0s3") #verificar nome da placa

#print de configurações de rede
os.system("ifconfig") 