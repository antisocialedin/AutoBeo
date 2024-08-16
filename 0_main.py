#!/usr/bin/env python
# Eder Filho
# 01/07/2023
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - MAIN

import os


#Verificação de máquina
print("---------------------- Script Cluster ----------------------\n")
print("Digite 1 - Configurar servidor DHCP \n")
print("Digite 2 - Restart servidor DHCP \n")
print("Digite 3 - Configurar o servidor SSH \n") 
print("Digite 4 - Configurar o mestre \n") 
print("Digite 5 - Configurar os escravos \n")
print("Digite 99 - SAIR \n")

maquina = int(input("~: "))

while True:
    match maquina:
        case 1:
            print("Configurando servidor DHCP...")
            os.system("sudo python3 1_dhcp.py")

        case 2:
            print("Restart servidor DHCP...")
            os.system("sudo service isc-dhcp-server restart")

        case 3:
            print("Configurando servidor ssh...")
            os.system("sudo python3 4_ssh.py")

        case 4:
            print("Configurando o mestre...")

        case 5:
            print("Configurando os escravos...")

        case 99:
                print("Saindo...")
                break

        case _:
            print("Opção inválida. Tente novamente.")

