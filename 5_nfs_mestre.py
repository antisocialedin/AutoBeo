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
exports.append("/home/cluster/clusterdir 192.168.40.0/24(rw,no_subtree_check,async,no_root_squash) \n")
arquivo.writelines(exports)

#iniciar serviço de NFS (apenas Mestre)
os.system("systemctl enable nfs-kernel-server")


