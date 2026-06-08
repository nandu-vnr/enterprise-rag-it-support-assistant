# AWS Lambda Failure Runbook

## Lambda Execution Errors
This runbook covers AWS Lambda failures caused by permission issues, deployment bugs, or configuration drift.

### Step 1: Inspect CloudWatch Logs
Open the Lambda execution logs and identify the error type.

### Step 2: Validate IAM Permissions
Ensure the Lambda execution role has the required IAM permissions for resources such as S3, DynamoDB, and Secrets Manager.

### Step 3: Confirm Deployment Artifacts
Verify that the latest deployment package and environment variables are correct.

### Step 4: Retry the Function
Retry the Lambda after correcting the root cause and monitor for repeated failures.

### Escalation
Escalate to the cloud operations team if the failure impacts production deployment or downstream jobs.
