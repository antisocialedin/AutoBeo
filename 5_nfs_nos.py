#!/usr/bin/env python
# Eder Filho
# 15/08/2024
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - NFS

import paramiko
from dhcp_get_ip import ip_list  # Importa a lista de IPs do arquivo ip_list.py

for ip in ip_list:
    # Configurações SSH
    hostname = ip
    username = 'cluster'
    password = '1234'

    # Cria o cliente SSH
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        print(f"Conectando ao nó {ip}...")
        client.connect(hostname, username=username, password=password)

        # Comando 1: Criar o diretório
        comando1 = "mkdir -p ~/clusterdir"
        stdin, stdout, stderr = client.exec_command(comando1)
        print(f"Saída do nó {ip} - mkdir:", stdout.read().decode(), stderr.read().decode())

        # Comando 2: Atualizar o /etc/fstab
        comando2 = f"echo '192.168.40.1:/home/cluster/clusterdir /home/cluster/clusterdir nfs rw,async,hard,int 0 0' | sudo -S tee /tmp/fstab.temp"
        stdin, stdout, stderr = client.exec_command(comando2, get_pty=True)
        stdin.write(f"{password}\n")
        stdin.flush()
        print(f"Saída do nó {ip} - fstab update:", stdout.read().decode(), stderr.read().decode())

        # Comando 3: Mover o arquivo fstab temporário para o /etc/fstab
        comando3 = "sudo mv /tmp/fstab.temp /etc/fstab"
        stdin, stdout, stderr = client.exec_command(comando3, get_pty=True)
        stdin.write(f"{password}\n")
        stdin.flush()
        print(f"Saída do nó {ip} - move fstab:", stdout.read().decode(), stderr.read().decode())

        # Comando 4: Montar o diretório NFS
        comando4 = "sudo mount -t nfs 192.168.40.1:/home/cluster/clusterdir /home/cluster/clusterdir"
        stdin, stdout, stderr = client.exec_command(comando4, get_pty=True)
        stdin.write(f"{password}\n")
        stdin.flush()
        print(f"Saída do nó {ip} - mount:", stdout.read().decode(), stderr.read().decode())

    except paramiko.SSHException as e:
        print(f"Erro ao conectar ao nó {ip}: {str(e)}")

    finally:
        client.close()
