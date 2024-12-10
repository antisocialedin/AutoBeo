#!/usr/bin/env python
# Eder Filho
# 15/08/2024
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - NFS

import paramiko
from dhcp_get_ip import ip_list  # Importa a lista de IPs do arquivo ip_list.py

def configure_node(ip):
    # Conectar ao nó via SSH
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Autenticação por chave
    private_key_path = '/home/cluster/.ssh/id_rsa'  # Substitua pelo caminho da sua chave privada
    private_key = paramiko.RSAKey.from_private_key_file(private_key_path)
    
    ssh.connect(ip, username='cluster', pkey=private_key)

    # Criar diretório compartilhado
    ssh.exec_command("mkdir -p /home/cluster/clusterdir")

    # Editar o arquivo fstab com privilégios de superusuário
    fstab_entry = "192.168.40.1:/home/cluster/clusterdir /home/cluster/clusterdir nfs rw,sync,hard,int 0 0\n"
    command = f'echo "{fstab_entry}" | sudo tee -a /etc/fstab'
    stdin, stdout, stderr = ssh.exec_command(command)
    stderr_output = stderr.read().decode()
    if stderr_output:
        print(f"Erro ao editar /etc/fstab no nó {ip}: {stderr_output}")
    
    # Montar o diretório com sudo
    mount_command = "sudo mount -t nfs 192.168.40.1:/home/cluster/clusterdir /home/cluster/clusterdir"
    stdin, stdout, stderr = ssh.exec_command(mount_command)
    stderr_output = stderr.read().decode()
    if stderr_output:
        print(f"Erro ao montar diretório no nó {ip}: {stderr_output}")

    # Fechar conexões
    ssh.close()

# Configurar todos os nós
for ip in ip_list:
    configure_node(ip)
