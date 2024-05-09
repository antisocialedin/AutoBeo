#!/usr/bin/env python
# Eder Filho
# 09/05/2024
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - SSH

import os

#start no SSH
os.system("sudo systemctl enable ssh")

#monitorar o SSH
os.system("sudo systemctl status ssh")

#gerar key SSH 
os.system("ssh keygen")

#copiar key para nó 1
os.system("ssh-copy-id -i ~/.ssh/id_rsa.pub no1")

#copiar key para nó 2
os.system("ssh-copy-id -i ~/.ssh/id_rsa.pub no2")