#!/usr/bin/env python
# Eder Filho
# 19/12/2023
#SCRIPT PARA CONFIGURAÇÃO DE REDE - NÓS

import os

#instalação dependências
os.system("sudo apt-get install net-tools")
os.system("sudo apt-get install ifupdown")
os.system("sudo apt-get install openssh-server")
os.system("sudo apt-get install libopenmpi-dev")
#os.system("sudo apt-get install nfs-kernel-server") #apenas mestre
os.system("sudo apt-get install nfs-common")
os.system("sudo apt-get install portmap")
os.system("sudo apt-get install build-essential")

#configurar rede
arquivo = open("/etc/network/interfaces", "a")


