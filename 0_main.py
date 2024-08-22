#!/usr/bin/env python
# Eder Filho
# 01/07/2023
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - MAIN

import os

while True:

    #Verificação de máquina
    print("---------------------- Script Cluster ----------------------\n")
    print("Digite 0 - Instalação e Configuração Completa \n")
    print("Digite 1 - Configurar servidor DHCP \n")
    print("Digite 2 - Start servidor DHCP \n")
    print("Digite 3 - Status servidor DHCP \n")
    print("Digite 4 - Restart servidor DHCP \n")
    print("Digite 5 - Configurar o servidor SSH \n") 
    print("Digite 6 - Configurar NFS (Network File System) \n") 
    print("Digite 7 - Gerar .mpi_hostfile \n")
    print("Digite 99 - SAIR \n")

    opt = int(input("~: "))

    match opt:

        case 0:
            print("Configurando servidor DHCP...")
            os.system("python3 1_dhcp.py")

            print("Configurando servidor ssh...")
            os.system("python3 4_ssh.py")

            print("Configurando NFS mestre...")
            os.system("python3 5_nfs_mestre.py")

            print("Configurando NFS nos...")
            os.system("python3 5_nfs_nos.py")

            print("Gerando .mpi_hostfile...")
            os.system("python3 6_mpi_hostfile.py")

        case 1:
            print("Configurando servidor DHCP...")
            os.system("python3 1_dhcp.py")

        case 2:
            print("Start servidor DHCP...")
            os.system("service isc-dhcp-server start")
        
        case 3:
            print("Status servidor DHCP...")
            os.system("service isc-dhcp-server status")

        case 4:
            print("Restart servidor DHCP...")
            os.system("service isc-dhcp-server restart")

        case 5:
            print("Configurando servidor ssh...")
            os.system("python3 4_ssh.py")

        case 6:
            print("Configurando NFS mestre...")
            os.system("python3 5_nfs_mestre.py")

            print("Configurando NFS nos...")
            os.system("python3 5_nfs_nos.py")

        case 7:
            print("Gerando .mpi_hostfile...")
            os.system("python3 6_mpi_hostfile.py")

        case 99:
            print("Saindo...")
            break

        case _:
            print("Opção inválida. Tente novamente.")

