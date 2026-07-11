#!/bin/bash
# GIR Technologies DevSecOps Lab Automation Script
# Task 26 - Automated Nginx Container Deployment

echo "============= Updating System Packages ============="
sudo apt update -y

echo "============= Installing Docker Engine ============="
sudo apt install docker.io -y

echo "============= Starting Docker Service ============="
sudo systemctl start docker
sudo systemctl enable docker

echo "============= Launching Nginx Web Container ============="
docker run -d --name nginx-server -p 80:80 nginx

echo "============= Current Runtime Environment ============="
docker ps
