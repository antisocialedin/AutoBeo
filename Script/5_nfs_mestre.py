#!/usr/bin/env python
# Eder Filho
# 09/05/2024
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - NFS

import os

#criar diretório compartilhado mestre
os.system("mkdir /home/cluster/clusterdir")

os.system(" > /etc/exports") #limpa o arquivo

#editar exports (apenas Mestre)
arquivo = open("/etc/exports", "a")
exports = list()
exports.append("/home/cluster/clusterdir 192.168.40.0/24(rw,no_subtree_check,async,no_root_squash) \n")
arquivo.writelines(exports)

#iniciar serviço de NFS (apenas Mestre)
print("Iniciando servidor NFS...")
os.system("systemctl enable nfs-kernel-server")

#iniciar serviço de NFS (apenas Mestre)
print("Restart servidor NFS...")
os.system("sudo /etc/init.d/nfs-kernel-server restart")
