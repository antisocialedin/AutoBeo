#!/usr/bin/env python
# Eder Filho
# 01/07/2023
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - MAIN

import os

while True:

    #Verificação de máquina
    print("---------------------- Script Cluster ----------------------\n")
    print("Digite 1 - Configurar servidor DHCP \n")
    print("Digite 2 - Start servidor DHCP \n")
    print("Digite 3 - Status servidor DHCP \n")
    print("Digite 4 - Restart servidor DHCP \n")
    print("Digite 5 - Configurar o servidor SSH \n") 
    print("Digite 6 - Configurar NFS (Network File System) \n") 
    print("Digite 7 - Configurar os escravos \n")
    print("Digite 99 - SAIR \n")

    maquina = int(input("~: "))

    match maquina:
        case 1:
            print("Configurando servidor DHCP...")
            os.system("sudo python3 1_dhcp.py")

        case 2:
            print("Start servidor DHCP...")
            os.system("sudo service isc-dhcp-server start")
        
        case 3:
            print("Status servidor DHCP...")
            os.system("sudo service isc-dhcp-server status")

        case 4:
            print("Restart servidor DHCP...")
            os.system("sudo service isc-dhcp-server restart")

        case 5:
            print("Configurando servidor ssh...")
            os.system("sudo python3 4_ssh.py")

        case 6:
            print("Configurando NFS mestre...")
            os.system("sudo python3 5_nfs_mestre.py")

            print("Configurando NFS nos...")
            os.system("sudo python3 5_nfs_nos.py")
            
        case 7:
            print("Configurando os escravos...")

        case 99:
            print("Saindo...")
            break

        case _:
            print("Opção inválida. Tente novamente.")

