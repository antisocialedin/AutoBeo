#!/usr/bin/env python
# Eder Filho
# 09/05/2024
# SCRIPT PARA CONFIGURAÇÃO DE CLUSTER - NFS

import os

#criar diretório compartilhado mestre
os.system("mkdir clusterdir")

#editar exports (apenas Mestre)
arquivo = open("/etc/exports", "a")
exports = list()
exports.append("/home/cluster/clusterdir 192.168.1.0/24(rw,no_subtree_check,async,no_root_squash) \n")
arquivo.writelines(exports)

#iniciar serviço de NFS (apenas Mestre)
os.system("systemctl enable nfs-kernel-server")

#criar e copiar conteudo do diretório compartilhado no1
os.system("ssh no1")
os.system("mkdir clusterdir")
os.system("sudo mount -t nfs 192.168.1.110:/home/cluster/clusterdir /home/cluster/clusterdir")
#editar fstab (apenas Nós)
arquivo = open("/etc/fstab", "a")
fstab = list()
fstab.append("192.168.1.110:/home/cluster/clusterdir /home/cluster/clusterdir nfs rw,sync,hard,int 0 0 \n")
arquivo.writelines(fstab)
os.system("exit")

#criar e copiar conteudo do diretório compartilhado no2
os.system("ssh no2")
os.system("mkdir clusterdir")
os.system("sudo mount -t nfs 192.168.1.110:/home/cluster/clusterdir /home/cluster/clusterdir")
#editar fstab (apenas Nós)
arquivo = open("/etc/fstab", "a")
fstab = list()
fstab.append("192.168.1.110:/home/cluster/clusterdir /home/cluster/clusterdir nfs rw,sync,hard,int 0 0 \n")
arquivo.writelines(fstab)
os.system("exit")
