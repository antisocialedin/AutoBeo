#!/usr/bin/env python
# Eder Filho
# 22/07/2023
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - DHCP

import os

#Configuração do DHCP

#criando rede
os.system("sudo ifconfig enp0s9 192.168.40.1 netmask 255.255.255.0") #verificar nome da placa

os.system(" > /etc/default/isc-dhcp-server") #limpa o arquivo

arquivo = open("/etc/default/isc-dhcp-server", "a")
dhcp = list()
dhcp.append('INTERFACESv4="enp0s9') #verificar nome da placa
arquivo.writelines(dhcp)

os.system(" > /etc/dhcp/dhcpd.conf") #limpa o arquivo

arquivo = open("/etc/dhcp/dhcpd.conf", "a")
dhcp2 = list()
dhcp2.append('option domain-name "laboratorio.rede";\n')
dhcp2.append('option domain-name-servers teste1.laboratorio.rede;\n')
dhcp2.append('default-lease-time 60;\n')
dhcp2.append('max-lease-time 86400;\n')
dhcp2.append('authoritative;\n\n')

dhcp2.append('subnet 192.168.40.0 netmask 255.255.255.0 {\n')
dhcp2.append('option routers 192.168.40.1;\n')
dhcp2.append('option subnet-mask 255.255.255.0;\n')
dhcp2.append('option domain-search "laboratorio.rede";\n')
dhcp2.append('option domain-name-servers 192.168.40.3, 8.8.8.8;\n')
dhcp2.append('range 192.168.40.20 192.168.40.100;\n')
dhcp2.append('}')
arquivo.writelines(dhcp2)


#start do serviço  
os.system("service isc-dhcp-server start")

#status do serviço
os.system("service isc-dhcp-server status")
