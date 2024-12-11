#!/usr/bin/env python
# Eder Filho
# 15/08/2024
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - NFS

import paramiko
import time
from dhcp_get_ip import ip_list  # Importa a lista de IPs do arquivo ip_list.py

def configure_node(ip, sudo_password):
    # Conectar ao nó via SSH
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Autenticação por chave
    private_key_path = '/home/cluster/.ssh/id_rsa'  # Substitua pelo caminho da sua chave privada
    private_key = paramiko.RSAKey.from_private_key_file(private_key_path)
    
    ssh.connect(ip, username='cluster', pkey=private_key)

    # Criar diretório compartilhado
    ssh.exec_command("mkdir -p /home/cluster/clusterdir")

    # Editar /etc/fstab
    fstab_command = (
        "echo '192.168.40.1:/home/cluster/clusterdir /home/cluster/clusterdir nfs rw,sync,hard,int 0 0' "
        "| sudo -S tee -a /etc/fstab"
    )
    stdin, stdout, stderr = ssh.exec_command(fstab_command, get_pty=True)
    time.sleep(2)  # Adicionar delay antes de fornecer a senha
    stdin.write(sudo_password + '\n')
    stdin.flush()
    print("fstab stdout:", stdout.read().decode())
    print("fstab stderr:", stderr.read().decode())

    # Montar o diretório
    mount_command = "sudo -S mount -t nfs 192.168.40.1:/home/cluster/clusterdir /home/cluster/clusterdir"
    stdin, stdout, stderr = ssh.exec_command(mount_command, get_pty=True)
    time.sleep(2)  # Adicionar delay antes de fornecer a senha
    stdin.write(sudo_password + '\n')
    stdin.flush()
    print("mount stdout:", stdout.read().decode())
    print("mount stderr:", stderr.read().decode())

    # Fechar conexões
    ssh.close()

# Configurar todos os nós
sudo_password = "1234"  # Substitua pela senha correta
for ip in ip_list:
    configure_node(ip, sudo_password)
