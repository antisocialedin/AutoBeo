#!/usr/bin/env python
# Eder Filho
# 01/07/2023
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - DEPENDENCIAS

import os

#Verificação de máquina
print("---------------------- Script Cluster ----------------------\n")
print("Digite 1 - Para configurar o mestre \n") 
print("Digite 2 - Para configurar os escravos: \n")

maquina = 2

match maquina:
    case 1:
        print("Configurando o mestre")
    case 2:
        print("Configurando os escravos")

