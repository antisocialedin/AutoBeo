#!/usr/bin/env python
# Eder Filho
# 09/05/2024
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - SSH

import os
from dhcp_get_ip import ip_list  # Importa a lista de IPs do arquivo ip_list.py

#start no SSH
print("Iniciando servidor ssh...")
os.system("systemctl enable ssh")

#monitorar o SSH
print("Monitorando servidor ssh...")
os.system("systemctl status ssh")

#criar pasta .ssh
os.system("mkdir /home/cluster/.ssh")

# Defina o caminho da pasta onde você deseja gerar a chave
ssh_key_dir = "/home/cluster/.ssh"

#gerar key SSH 
print(f"Gerando chave ssh em {ssh_key_dir}...")
os.system(f"ssh-keygen -f {ssh_key_dir}")

#caminho da pasta .ssh
print("Caminhando para a pasta .ssh...")
os.chdir("/home/cluster/.ssh")

# Copia a chave para cada IP na lista
print("Copiando chave para os IPs...")
for ip in ip_list:
    os.system(f"ssh-copy-id -i /home/cluster/.ssh/id_rsa.pub cluster@{ip}")
