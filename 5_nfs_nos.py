#!/usr/bin/env python
# Eder Filho
# 15/08/2024
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - NFS

import paramiko
from dhcp_get_ip import ip_list  # Importa a lista de IPs do arquivo ip_list.py

for ip in ip_list:
    # Configurações SSH
    hostname = ip  # IP do nó, por exemplo
    username = 'cluster'
    password = '1234'

    # Cria o cliente SSH
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Conecta ao host
        client.connect(hostname, username=username, password=password)

        # Comandos a serem executados remotamente
        comandos = """
        # Atualiza o arquivo /etc/fstab com as configurações NFS
        echo "192.168.40.1:/home/cluster/clusterdir /home/cluster/clusterdir nfs rw,async,hard,int 0 0" &&
        # Monta o diretório NFS
        sudo mount -t nfs 192.168.40.1:/home/cluster/clusterdir /home/cluster/clusterdir
        """

        # Executa os comandos no nó remoto
        stdin, stdout, stderr = client.exec_command(comandos, get_pty=True)
        stdin.write(f"{password}\n")
        stdin.flush()

        # Lê a saída e os erros do comando
        output = stdout.read().decode()
        erros = stderr.read().decode()

        # Exibe a saída e os erros
        print(f"Saída do nó {ip}:", output)
        print(f"Erros no nó {ip}:", erros)

    finally:
        # Fecha a conexão
        client.close()


"""         # Cria o diretório se não existir
        mkdir ~/clusterdir &&
        # Atualiza o arquivo /etc/fstab com as configurações NFS
        echo "192.168.40.1:/home/cluster/clusterdir /home/cluster/clusterdir nfs rw,async,hard,int 0 0" &&
        # Monta o diretório NFS
        sudo mount -t nfs 192.168.40.1:/home/cluster/clusterdir /home/cluster/clusterdir
        """