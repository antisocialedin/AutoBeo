#!/usr/bin/env python
# Eder Filho
# 01/07/2023
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - MAIN

import os


#Verificação de máquina
print("---------------------- Script Cluster ----------------------\n")
print("Digite 1 - Configurar DHCP \n")
print("Digite 2 - Restart DHCP \n")
print("Digite 3 - Para configurar o mestre \n") 
print("Digite 4 - Para configurar os escravos: \n")

maquina = int(input("~: "))

match maquina:
    case 1:
        print("Configurando DHCP...")
        os.system("sudo python3 1_dhcp.py")

    case 2:
        os.system("sudo service isc-dhcp-server restart")

    case 3:
        print("Configurando o mestre...")

    case 4:
        print("Configurando os escravos...")

