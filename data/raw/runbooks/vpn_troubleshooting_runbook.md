# VPN Troubleshooting Runbook

## Authentication Failure
This runbook explains how to diagnose and resolve VPN authentication failure issues.

### Step 1: Confirm AD Login
Ensure the impacted user can authenticate successfully to Active Directory.

### Step 2: Verify Password Propagation
Check that the password reset propagated to the VPN authentication backend.

### Step 3: Review MFA Sync
Validate that MFA requests are being accepted and that the MFA service is healthy.

### Step 4: Check Time Sync
Confirm NTP synchronization between the VPN appliance and domain controllers.

### Escalation
If the issue persists, escalate to IAM and provide relevant VPN logs.
