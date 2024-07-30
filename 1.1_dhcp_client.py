#!/usr/bin/env python
# Eder Filho
# 29/07/2023
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - DHCP CLIENT

#import os
import subprocess

# Executa o comando com shell=True para permitir encadeamento de comandos
result = subprocess.run('dhcp-lease-list | tail -n +4 | cut -d " " -f 3', shell=True, capture_output=True, text=True)

# Imprime a saída capturada
print(result.stdout)

