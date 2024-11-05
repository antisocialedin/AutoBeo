#!/usr/bin/env python
# Eder Filho
# 09/05/2024
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - MPI

import os

os.system(" > /home/cluster/.mpi_hostfile") #limpa o arquivo

#editar hostfile (apenas Mestre)
arquivo = open("/home/cluster/.mpi_hostfile", "a")
hostfile = list()
hostfile.append("localhost slots= {Digite a quantidade de núcleos do mestre} \n")
hostfile.append("{IP da Máquina 1} slots = {Digite a quantidade de núcleos} \n")
hostfile.append("{IP da Máquina 2} slots= {Digite a quantidade de núcleos} \n")
hostfile.append("{IP da Máquina n} slots= {Digite a quantidade de núcleos} \n")
arquivo.writelines(hostfile)