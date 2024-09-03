#!/usr/bin/env python
# Eder Filho
# 15/08/2024
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - NFS

import os
from dhcp_get_ip import ip_list  # Importa a lista de IPs do arquivo ip_list.py

for ip in ip_list:
    #criar diretório compartilhado nos
    os.system(f"ssh {ip} 'mkdir /home/cluster/clusterdir'")

    #editar fstab (apenas Nós)
    os.system(" > /etc/fstab") #limpa o arquivo

    arquivo = open(" /etc/fstab", "a")
    fstab = list()
    fstab.append("192.168.40.1:/home/cluster/clusterdir /home/cluster/clusterdir nfs rw,sync,hard,int 0 0 \n")
    arquivo.writelines(fstab)

    os.system("sudo mount -t nfs 192.168.40.1:/home/cluster/clusterdir /home/cluster/clusterdir")