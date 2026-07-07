# Task 24 – NAT Gateway with Public and Private Subnets

## Objective
Create a custom VPC with public and private subnets, configure a NAT Gateway, launch EC2 instances, verify internet connectivity from the private subnet, and clean up all AWS resources.

## Services Used
- Amazon VPC
- Public Subnet
- Private Subnet
- Internet Gateway
- NAT Gateway
- Elastic IP
- Route Tables
- EC2 (Ubuntu)
- Security Groups

## Steps Performed
1. Created a custom VPC.
2. Created a public subnet.
3. Created a private subnet.
4. Attached an Internet Gateway.
5. Created a public route table.
6. Associated the public subnet with the public route table.
7. Allocated an Elastic IP.
8. Created a NAT Gateway in the public subnet.
9. Created a private route table.
10. Added a default route (0.0.0.0/0) to the NAT Gateway.
11. Associated the private subnet with the private route table.
12. Launched a public EC2 instance.
13. Launched a private EC2 instance.
14. Connected to the public EC2 using SSH.
15. Connected to the private EC2 through the public EC2.
16. Verified internet connectivity using:
    ```bash
    sudo apt update
    ```
17. Deleted all AWS resources after verification.

## Result
Successfully configured a NAT Gateway that allowed the private EC2 instance to access the internet without assigning it a public IP.

## Author
Shaik Sadik