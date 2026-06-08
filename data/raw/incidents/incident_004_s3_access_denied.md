# S3 Access Denied

## Overview
A service account cannot access S3 objects after IAM policy changes. The storage gateway returns AccessDenied errors.

## Symptoms
- S3 access denied errors in application logs
- IAM policy changes were recently applied
- The service account is used by a deployment pipeline or file transfer service

## Troubleshooting Steps
1. Review the S3 bucket policy and IAM role trust relationship.
2. Confirm the service account has the correct permissions for PutObject/GetObject.
3. Check whether a deny statement is overriding allow permissions.
4. Validate that the AWS role session is assumed properly and the temporary credentials are valid.

## Escalation
Escalate to the cloud operations team if IAM policy rollback is required to restore production access.
