# Task 25 — Security Group Rules for a 2-Tier App

## 🎯 Objective
Configure network security groups to restrict application backend access on Port 8080 strictly to frontend sources while keeping the web tier open to the public.

## 🛠️ Tools & Services Used
* AWS VPC & Subnets
* Internet Gateway & Route Tables
* Security Groups
* Amazon EC2 (Ubuntu 24.04 LTS)

## 📋 Steps Performed
1. **Workspace Synchronization:** Configured the isolated regional workspace to US East (N. Virginia) `us-east-1`.
2. **Custom VPC Construction:** Generated a custom virtual network canvas named `task25-vpc` with a `10.0.0.0/16` CIDR block.
3. **Subnet Segmentation:** Partitioned the network canvas into `task25-public-subnet` (`10.0.1.0/24`) and `task25-private-subnet` (`10.0.2.0/24`) inside the `us-east-1a` Availability Zone.
4. **Internet Edge Gateway Integration:** Initialized an Internet Gateway named `task25-igw` and attached it directly to `task25-vpc`.
5. **Edge Routing Configuration:** Built a custom routing table named `task25-public-rt`, added a route mapping `0.0.0.0/0` to `task25-igw`, and explicitly linked it to `task25-public-subnet`.
6. **Web Firewall Provisioning:** Constructed `task25-web-sg` allowing HTTP (80), HTTPS (443) from everywhere (`0.0.0.0/0`), and SSH (22) restricted to administrative IP access.
7. **App Nested Firewall Provisioning:** Constructed `task25-app-sg` targeting Port 8080 and explicitly chained its Source target to the dynamic Security Group ID of `task25-web-sg` instead of an open IP string.
8. **Compute Instance Deployment:** Provisioned `task25-web-server` in the public subnet with an Apache bootstrap user data script, and provisioned `task25-app-server` wrapped inside the private subnet.
9. **Architectural Verification:** Validated external packet flow by accessing the web server's public IP address via a web browser, successfully rendering the user data initialization page.
10. **Internal Network Hop:** Verified multi-tier transport routing by executing a nested SSH hop from the public web tier server (`10.0.1.50`) directly into the isolated private application tier backend (`10.0.2.203`).
11. **Environment Teardown:** Terminated all compute units, detached/purged the internet edge gateway components, and thoroughly deleted the parent custom VPC frame to ensure absolute protection against accidental Free Tier resource overages.

## 💻 Key Commands & Bootstrap Scripts
```bash
#!/bin/bash
# Inbound Metadata Initialization Script (EC2 User Data Module)
sudo apt update
sudo apt install apache2 -y
echo "<h1>Task 25 - Web Server</h1>" > /var/www/html/index.html
sudo systemctl enable apache2
sudo systemctl start apache2