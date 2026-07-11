# Task 26 – Dockerized Web Application on AWS EC2

## Objective
Deploy a Dockerized web application on an AWS EC2 instance inside a custom VPC[cite: 7, 32].

## AWS Services Used
- Amazon EC2 [cite: 32]
- Amazon VPC [cite: 32]
- Security Groups [cite: 32]
- Internet Gateway [cite: 32]
- Docker [cite: 32]

## Commands Used

sudo apt update

sudo apt install docker.io -y

docker --version

docker run hello-world

docker pull nginx

docker run -d --name task26-web -p 80:80 nginx

docker ps

docker logs task26-web

docker stop task26-web

docker rm task26-web

## Result
Successfully deployed a Dockerized web application on AWS EC2.
