#!/usr/bin/env python
# Eder Filho
# 09/05/2024
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - SSH

import os
from dhcp_client import ip_list  # Importa a lista de IPs do arquivo ip_list.py

#start no SSH
os.system("sudo systemctl enable ssh")

#monitorar o SSH
os.system("sudo systemctl status ssh")

#gerar key SSH 
os.system("ssh keygen")

# Copia a chave para cada IP na lista
for ip in ip_list:
    os.system(f"ssh-copy-id -i ~/.ssh/id_rsa.pub {ip}")