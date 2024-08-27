#!/usr/bin/env python
# Eder Filho
# 15/08/2024
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - NFS

import os
from dhcp_get_ip import ip_list  # Importa a lista de IPs do arquivo ip_list.py

#criar e copiar conteudo do diretório compartilhado (apenas Nós)
for ip in ip_list:

    os.system(f"ssh cluster@{ip}")
    os.system("mkdir ~/clusterdir")
    os.system("sudo mount -t nfs 192.168.40.1:/home/cluster/clusterdir /home/cluster/clusterdir")

    #editar fstab (apenas Nós)
    os.system("sudo > /etc/fstab") #limpa o arquivo

    arquivo = open("sudo /etc/fstab", "a")
    fstab = list()
    fstab.append("192.168.40.1:/home/cluster/clusterdir /home/cluster/clusterdir nfs rw,sync,hard,int 0 0 \n")
    arquivo.writelines(fstab)

    os.system("exit")