\# Task 23 - Build a Custom VPC from Scratch



\## Objective

Create a custom VPC in AWS with a public subnet, Internet Gateway, and Route Table. Launch an EC2 instance, install Docker, verify Docker functionality, and perform cleanup.



\## AWS Services Used

\- Amazon VPC

\- EC2

\- Internet Gateway

\- Route Table

\- Security Group

\- Amazon Linux 2023

\- Docker



\## Steps Performed

1\. Created a custom VPC (10.0.0.0/16).

2\. Created a public subnet (10.0.1.0/24).

3\. Attached an Internet Gateway.

4\. Created and associated a Route Table.

5\. Enabled Auto-assign Public IPv4.

6\. Created a Security Group.

7\. Launched an EC2 instance.

8\. Connected using SSH.

9\. Installed Docker.

10\. Verified Docker using the hello-world container.

11\. Cleaned up all AWS resources.



\## Docker Commands



```bash

sudo dnf update -y

sudo dnf install docker -y

sudo systemctl start docker

sudo systemctl enable docker

docker --version

sudo docker run hello-world

