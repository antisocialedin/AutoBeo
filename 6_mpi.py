#!/usr/bin/env python
# Eder Filho
# 09/05/2024
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - MPI

import os

#editar hostfile (apenas Mestre)
arquivo = open(".mpi_hostfile", "a")
hostfile = list()
hostfile.append("localhost slots=2 \n")
hostfile.append("no1 slots=2 \n")
hostfile.append("no2 slots=2 \n")
arquivo.writelines(hostfile)