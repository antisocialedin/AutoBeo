#!/usr/bin/env python
# Eder Filho
# 09/05/2024
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - ARQUIVO HOSTS

import os

#Verificação da quantidade de nós 
qtd_nos = int(input("Digite a quantidade de nós: "))

#hosts
arquivo = open("/etc/hosts", "a")
hosts = list()
hosts.append("127.0.1.1 mestre \n")
hosts.append("192.168.1.100 mestre\n")
arquivo.writelines(hosts)

i = 0
while i < qtd_nos:
    print(i)
    arquivo = open("/etc/hosts", "a")
    hosts_no = list()
    hosts_no.append("192.168.1.10")
    hosts_no.append(i)
    hosts_no.append("no")
    hosts_no.append(i)
    hosts_no.append("\n")
    arquivo.writelines(hosts_no)
    i = i+1