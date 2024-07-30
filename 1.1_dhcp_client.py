#!/usr/bin/env python
# Eder Filho
# 29/07/2023
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - DHCP CLIENT

#import os
import subprocess

result = subprocess.run(['dhcp-lease-list | tail -n +4 | cut -d " " -f 3'], capture_output=True, text=True)
print(result.stdout)


