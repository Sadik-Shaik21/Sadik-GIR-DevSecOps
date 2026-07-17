# Task 29 — Enable and Review CloudTrail Logs in S3

## Objective
To enable AWS CloudTrail globally across the account, route the management API audit logs to a secure Amazon S3 bucket, simulate administrative console activity by creating and deleting a test IAM user, and parse the resulting JSON log artifacts using terminal utilities to verify forensic audit visibility[cite: 3].

## Tools & Services Used
* **AWS CloudTrail:** For global infrastructure API tracking[cite: 3].
* **Amazon S3:** As the secure log storage vault[cite: 3].
* **AWS IAM:** Used to generate auditable events (`CreateUser`, `DeleteUser`)[cite: 3].
* **Git Bash:** For local JSON data parsing and log inspection[cite: 3].

## Steps Performed & Commands Executed

### 1. Storage & Trail Provisioning
* Created a private S3 bucket named `task29-cloudtrail-logs-sadik-2026`[cite: 3].
* Configured a multi-region trail named `management-events` targeting the created S3 bucket[cite: 3].

### 2. Simulated Activity Generation
* Created a temporary test IAM user named `task29-audit-test-user`[cite: 3].
* Immediately deleted the user to create a matching pair of auditable tracking events[cite: 3].

### 3. Local Log Inspection (Git Bash)
* Verified the presence of the automatically extracted log payload file:
  ```bash
  ls
EDF
