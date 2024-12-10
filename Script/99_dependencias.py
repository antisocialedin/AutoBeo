#!/usr/bin/env python
# Eder Filho
# 19/12/2023
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - DEPENDENCIAS

import os

#Instalação dependências
os.system("apt-get install net-tools")
os.system("apt-get install ifupdown") 
os.system("apt-get install openssh-server")
os.system("apt-get install libopenmpi-dev")
os.system("apt-get install isc-dhcp-server") #apenas mestre
os.system("apt-get install nfs-kernel-server") #apenas mestre
os.system("apt-get install nfs-common")
os.system("apt-get install portmap")
os.system("apt-get install build-essential")
os.system("apt-get install python3-pip")
os.system("pip install paramiko")