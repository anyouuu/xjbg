#!/bin/bash
# 初始化 新机器，安装docker
sudo yum -f install  epel-release 
sudo yum -y update
sudo yum -y install docker && htop && 
sudo systemctl enable docker \
sudo systemctl start docker

## fix start docker waining 
# vim /etc/sysconfig/docker

# Modify these options if you want to change the way the docker daemon runs
#OPTIONS='--selinux-enabled=false --log-driver=journald --signature-verification=false'
#if [ -z "${DOCKER_CERT_PATH}" ]; then
#    DOCKER_CERT_PATH=/etc/docker
#
#fi

# centos docker 操作
# echo '{ "insecure-registries":["xxx.xxx.xxx.xxx:5000"] }' > /etc/docker/daemon.json

# systemctl restart docker


