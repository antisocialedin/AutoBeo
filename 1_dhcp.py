#!/usr/bin/env python
# Eder Filho
# 22/07/2023
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - DHCP

import os

#Configuração do DHCP

#criando rede
os.system("sudo ifconfig enp0s3 192.168.40.1 netmask 255.255.255.0 ​")

arquivo = open("/etc/default/isc-dhcp-server​", "a")
dhcp = list()
dhcp.append('INTERFACESv4="enp0s3" \n') #verificar nome da placa
arquivo.writelines(dhcp)

arquivo = open("/etc/dhcp/dhcpd", "a")
dhcp2 = list()
dhcp2.append('option domain-name "laboratorio.rede"; \n')
dhcp2.append('option domain-name-servers teste1.laboratorio.rede;​ \n')
dhcp2.append('default-lease-time 3000; \n')
dhcp2.append('max-lease-time 7200;​ \n')
dhcp2.append('authoritative; \n\n')

dhcp2.append('subnet 192.168.40.0 netmask 255.255.255.0 {​\n')
dhcp2.append('option routers   192.168.40.1;​\n')
dhcp2.append('option subnet-mask 255.255.255.0;​\n')
dhcp2.append('option domain-search "laboratorio.rede";​\n')
dhcp2.append('option domain-name-servers 192.168.40.3, 8.8.8.8;​\n')
dhcp2.append('range 192.168.40.20 192.168.40.100;​\n')
arquivo.writelines(dhcp2)

#start do serviço  
os.system("sudo service isc-dhcp-server start​")

#status do serviço
os.system("sudo service isc-dhcp-server status​")

#restart do serviço
os.system("sudo service isc-dhcp-server restart​")