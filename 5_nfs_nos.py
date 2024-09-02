#!/usr/bin/env python
# Eder Filho
# 15/08/2024
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - NFS

import os
import paramiko # type: ignore
from dhcp_get_ip import ip_list  # Importa a lista de IPs do arquivo ip_list.py

#criar e copiar conteudo do diretório compartilhado (apenas Nós)
""" for ip in ip_list:

    os.system(f"ssh cluster@{ip}")
    os.system("mkdir ~/clusterdir")
    os.system("sudo mount -t nfs 192.168.40.1:/home/cluster/clusterdir /home/cluster/clusterdir")

    #editar fstab (apenas Nós)
    os.system(" > /etc/fstab") #limpa o arquivo

    arquivo = open(" /etc/fstab", "a")
    fstab = list()
    fstab.append("192.168.40.1:/home/cluster/clusterdir /home/cluster/clusterdir nfs rw,sync,hard,int 0 0 \n")
    arquivo.writelines(fstab)

    os.system("exit") """

for ip in ip_list:
    # Configurações SSH
    hostname = ip  # IP do nó1, por exemplo
    username = 'cluster'
    password = '1234'

    # Cria o cliente SSH
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Conecta ao host
        client.connect(hostname, username=username, password=password)

        # Define o conjunto de comandos
        comandos = """
        mkdir ~/clusterdir &&
        sudo mount -t nfs 192.168.40.1:/home/cluster/clusterdir /home/cluster/clusterdir &&
        sudo sh -c 'echo "" > /etc/fstab' &&
        echo "192.168.40.1:/home/cluster/clusterdir /home/cluster/clusterdir nfs rw,sync,hard,int 0 0" | sudo tee -a /etc/fstab
        """

        # Executa os comandos no nó remoto
        stdin, stdout, stderr = client.exec_command(comandos)

        # Lê a saída e os erros do comando
        output = stdout.read().decode()
        erros = stderr.read().decode()

        # Exibe a saída e os erros
        print("Saída:", output)
        print("Erros:", erros)

    finally:
        # Fecha a conexão
        client.close()
