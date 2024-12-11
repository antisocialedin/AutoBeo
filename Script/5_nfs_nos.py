#!/usr/bin/env python
# Eder Filho
# 15/08/2024
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - NFS

import paramiko
from dhcp_get_ip import ip_list  # Importa a lista de IPs do arquivo ip_list.py

sudo_password = "1234"  # Senha do sudo

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

    # Editar o arquivo fstab com privilégios de superusuário
    fstab_entry = "192.168.40.1:/home/cluster/clusterdir /home/cluster/clusterdir nfs rw,sync,hard,int 0 0\n"
    command = f'echo "{fstab_entry}" | sudo -S tee -a /etc/fstab'
    
    # Executar o comando e enviar a senha via stdin.write()
    stdin, stdout, stderr = ssh.exec_command("sudo -S whoami", get_pty=True)
    stdin.write(sudo_password + '\n')
    stdin.flush()

    # Captura a saída do comando
    stdout_data = stdout.read().decode()
    stderr_data = stderr.read().decode()
    if stderr_data:
        print(f"Erro ao editar /etc/fstab no nó {ip}: {stderr_data}")
    else:
        print(f"Arquivo /etc/fstab editado com sucesso no nó {ip}")

    # Montar o diretório com sudo
    mount_command = "sudo -S mount -t nfs 192.16840.1:/home/cluster/clusterdir /home/cluster/clusterdir"
    stdin, stdout, stderr = ssh.exec_command(mount_command)
    
    # Passa a senha para o sudo
    stdin, stdout, stderr = ssh.exec_command("sudo -S whoami", get_pty=True)
    stdin.write(sudo_password + '\n')
    stdin.flush()

    # Captura a saída do comando de montagem
    stdout_data = stdout.read().decode()
    stderr_data = stderr.read().decode()
    if stderr_data:
        print(f"Erro ao montar diretório no nó {ip}: {stderr_data}")
    else:
        print(f"Diretório montado com sucesso no nó {ip}")

    # Fechar conexões
    ssh.close()

# Configurar todos os nós
for ip in ip_list:
    configure_node(ip, sudo_password)
