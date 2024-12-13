#!/usr/bin/env python
# Eder Filho
# 09/05/2024
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - SSH

import os
from dhcp_get_ip import ip_list  # Importa a lista de IPs do arquivo ip_list.py

# Função para executar um comando com verificação de saída
def run_command(command):
    result = os.system(command)
    if result != 0:
        print(f"Erro ao executar o comando: {command}")
    return result

# Iniciar o servidor SSH
print("Iniciando servidor SSH...")
run_command("sudo systemctl enable ssh")

# Monitorar o servidor SSH
print("Monitorando servidor SSH...")
run_command("sudo systemctl status ssh")

# Diretório e caminho da chave SSH
ssh_key_dir = "/home/cluster/.ssh"
ssh_key_path = os.path.join(ssh_key_dir, "id_rsa")

# Gerar a chave SSH
if not os.path.exists(ssh_key_path):
    print(f"Gerando chave SSH em {ssh_key_path}...")
    run_command(f"sudo -u cluster ssh-keygen -f {ssh_key_path} -N ''")
else:
    print(f"Chave SSH já existe em {ssh_key_path}.")

# Copiar a chave para os IPs
print("Copiando chave para os IPs...")
for ip in ip_list:
    print(f"Tentando copiar chave para {ip}...")
    # Adicionar opção para solicitar senha se a chave pública falhar
    command = (
        f"sshpass -p '1234' ssh-copy-id -o PreferredAuthentications=password "
        f"-i {ssh_key_path}.pub cluster@{ip}"
    )
    result = run_command(command)
    if result != 0:
        print(f"Erro ao copiar chave para {ip}. Verifique as configurações de SSH.")

print("Processo de configuração de chave SSH concluído.")
