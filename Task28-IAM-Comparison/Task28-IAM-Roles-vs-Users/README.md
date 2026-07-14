# Task 28 – IAM Roles vs Users Comparison

## Objective
To securely access an Amazon S3 bucket from an EC2 instance using an IAM Role instead of static AWS access keys.

## Tools Used
- AWS EC2
- Amazon S3
- AWS IAM
- AWS CLI
- Ubuntu Linux (Git Bash)

## Key Commands Run
- `curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/iam/security-credentials/`
- `aws sts get-caller-identity`
- `aws s3 ls s3://task28-sadik-2026`
- `aws s3 cp s3://task28-sadik-2026/task28.txt .`
- `aws configure list`

## Identity Verification Summary
- **Credential Type:** `iam-role` (Dynamic, short-lived tokens starting with the `ASIA` prefix)
- **Static Credentials Status:** `~/.aws` configuration directory verified completely absent, confirming zero static keys are hardcoded on disk.
