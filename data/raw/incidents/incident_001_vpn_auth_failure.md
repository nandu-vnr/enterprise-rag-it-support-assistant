# VPN Authentication Failure

## Overview
Users are unable to authenticate to the corporate VPN after a password reset. The authentication gateway reports credential and MFA failures.

## Symptoms
- VPN login page returns authentication failure
- MFA challenge does not complete
- Password reset was recently performed

## Troubleshooting Steps
1. Verify the user can log in to Active Directory.
2. Confirm password propagation to the VPN authentication service.
3. Check the VPN auth gateway logs for invalid credential or MFA timeout errors.
4. Confirm time synchronization between the VPN appliance and AD domain controllers.

## Relevant Systems
- Corporate VPN
- Active Directory
- MFA provider

## Escalation
Escalate to IAM if password propagation and MFA sync are confirmed but users still cannot authenticate.
