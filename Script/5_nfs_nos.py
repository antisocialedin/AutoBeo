#!/usr/bin/env python
# Eder Filho
# 15/08/2024
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - NFS

import paramiko
from dhcp_get_ip import ip_list  # Importa a lista de IPs do arquivo ip_list.py

# Configurar todos os nós
sudo_password = "1234"  # Substitua pela senha correta

def configure_node(ip, sudo_password):
    try:

        print(f"Conectando SSH ao nó {ip}")
        # Conectar ao nó via SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Autenticação por chave
        private_key_path = '/home/cluster/.ssh/id_rsa'  # Substitua pelo caminho da sua chave privada
        private_key = paramiko.RSAKey.from_private_key_file(private_key_path)
        
        ssh.connect(ip, username='cluster', pkey=private_key)

        # Criar diretório compartilhado
        print(f"Criando diretório compartilhado no nó {ip}")
        ssh.exec_command("mkdir -p /home/cluster/clusterdir")

        # Criar o script remoto para editar /etc/fstab e montar o diretório
        print(f"Rodando script remoto para configurar NFS no nó {ip}")
        remote_script = """
        #!/bin/bash
        echo '192.168.40.1:/home/cluster/clusterdir /home/cluster/clusterdir nfs rw,sync,hard,int 0 0' | sudo tee -a /etc/fstab
        sudo mount -t nfs 192.168.40.1:/home/cluster/clusterdir /home/cluster/clusterdir
        """
        
        # Enviar o script para o nó
        sftp = ssh.open_sftp()
        remote_script_path = "/home/cluster/configure_nfs.sh"
        with sftp.open(remote_script_path, "w") as script_file:
            script_file.write(remote_script)
        sftp.chmod(remote_script_path, 0o755)  # Tornar o script executável
        sftp.close()

        # Executar o script remoto
        stdin, stdout, stderr = ssh.exec_command(f"sudo -S bash {remote_script_path}", get_pty=True)
        stdin.write(sudo_password + '\n')
        stdin.flush()
        print("script stdout:", stdout.read().decode())
        print("script stderr:", stderr.read().decode())

    except Exception as e:
        print(f"Erro ao configurar o nó {ip}: {e}")
    
    finally:
        # Fechar conexões
        if ssh:
            ssh.close()

for ip in ip_list:
    configure_node(ip, sudo_password)
