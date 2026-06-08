# Enterprise IT Support Runbook
## Knowledge Base Document for RAG Support Chatbot

Document Owner: IT Support / Infrastructure Team  
Audience: Employees, Help Desk Agents, System Administrators, Security Analysts, Support Engineers  
Purpose: Internal IT support knowledge base for a retrieval-augmented generation chatbot  
Version: 1.0  
Last Updated: 2026  

---

# 1. Overview

This runbook provides standardized procedures for resolving common enterprise IT support issues. It is designed for use by employees, IT help desk agents, system administrators, security analysts, and automated RAG-based support chatbots.

The chatbot should use this document to provide safe, consistent, and accurate support guidance.

This runbook covers:

- Account access issues
- Password reset support
- Multi-factor authentication issues
- VPN troubleshooting
- Wi-Fi and network support
- Laptop and workstation troubleshooting
- Email and calendar support
- Microsoft Teams and collaboration tools
- Software installation requests
- Printer and scanner support
- File access and shared drives
- Browser troubleshooting
- Remote work issues
- Security incidents
- Phishing response
- Lost or stolen devices
- Data access requests
- Hardware replacement
- Escalation procedures
- Service level expectations

The chatbot may provide troubleshooting steps, but it must not bypass security controls, reveal credentials, expose secrets, approve access, disable MFA, or perform administrative actions without authorization.

---

# 2. General Support Principles

## 2.1 First Response Guidelines

When responding to a user, always:

1. Acknowledge the issue clearly.
2. Identify the affected system or service.
3. Ask only for necessary details.
4. Avoid requesting passwords, MFA codes, private keys, or sensitive personal information.
5. Provide safe troubleshooting steps.
6. Escalate when the issue involves security, data loss, production outage, privileged access, or multiple affected users.

Example response:

I can help troubleshoot this. Please confirm which system you are trying to access and what error message you see. Do not share your password or MFA code.

---

## 2.2 Information Support May Ask For

Support may ask for:

- Employee name
- Corporate email address
- Device type
- Operating system
- Error message
- Screenshot of the error if it does not contain sensitive information
- Time the issue started
- Whether the issue affects one user or multiple users
- Whether the user is in the office, remote, or connected to VPN
- Application name
- Browser name and version
- Device asset tag or serial number
- Business impact

Support must not ask for:

- Passwords
- MFA one-time codes
- Full personal identification numbers
- Private keys
- API secrets
- Recovery seed phrases
- Unmasked access tokens
- Customer confidential data unless approved
- Sensitive HR, payroll, legal, or medical details unless required and authorized

---

## 2.3 Severity Levels

## Severity 1 — Critical

A Severity 1 issue affects company-wide operations, production systems, security, or multiple critical users.

Examples:

- Company-wide SSO outage
- Production application unavailable
- Ransomware alert
- Security breach
- Major network outage
- Email unavailable for all users
- Data exfiltration suspected
- Widespread VPN outage
- Critical customer-facing service down

Response:

Immediate escalation to IT Operations, Security Operations, and Incident Management.

---

## Severity 2 — High

A Severity 2 issue affects a team, department, executive, or business-critical workflow.

Examples:

- VPN outage affecting many remote users
- Payroll system inaccessible
- Executive cannot access email before a major meeting
- Shared drive unavailable for an entire department
- Business-critical application degraded
- Multiple users unable to authenticate

Response:

Escalate to the responsible support team within the same business day or faster depending on impact.

---

## Severity 3 — Medium

A Severity 3 issue affects one user or has a temporary workaround.

Examples:

- One user cannot print
- Laptop is slow
- Outlook crashes occasionally
- Calendar sync issue
- User cannot access a non-critical app
- Software installation request

Response:

Resolve through standard troubleshooting or assign to desktop support.

---

## Severity 4 — Low

A Severity 4 issue is informational, routine, or low urgency.

Examples:

- How to install approved software
- How to request access
- How to update email signature
- How to change display settings
- How to connect to guest Wi-Fi
- General how-to questions

Response:

Provide self-service instructions or direct the user to the correct request process.

---

# 3. Account Access Issues

## 3.1 User Cannot Log In

Common causes:

- Incorrect password
- Expired password
- Locked account
- MFA issue
- SSO outage
- User account disabled
- Conditional access policy block
- Device not compliant
- Network issue
- Browser session issue
- User using personal email instead of corporate email

Troubleshooting steps:

1. Confirm the user is logging in with their full corporate email address.
2. Ask whether the issue happens on all applications or only one application.
3. Ask for the exact error message.
4. Ask whether the user recently changed their password.
5. Ask whether the user can access the company SSO portal.
6. Ask whether the user can access email, VPN, or other company tools.
7. If account is locked, follow the account unlock process.
8. If password is expired, guide the user through password reset.
9. If MFA is failing, follow MFA troubleshooting.
10. If the account is disabled, do not reactivate without HR or manager approval.
11. If multiple users are affected, escalate as possible SSO outage.

Safe chatbot response:

Please try signing in from the company SSO portal using your full corporate email address. If the message says your account is locked or your password expired, use the password reset option. Do not share your password or MFA code.

Escalate if:

- The user cannot access all company systems.
- The account appears disabled.
- The user reports suspicious login attempts.
- Multiple users report the same issue.
- There is evidence of account compromise.
- The user is an executive or business-critical user with urgent impact.

---

## 3.2 Account Locked

Common causes:

- Too many failed login attempts
- Saved old password on phone
- Saved old password in Outlook
- VPN client repeatedly using old password
- Browser password manager using old credentials
- Mapped network drive using old credentials
- Mobile email client using old password
- Unauthorized login attempts

Resolution:

1. Verify the user's identity according to help desk policy.
2. Unlock the account in the identity system if authorized.
3. Ask the user to update saved passwords on:
   - Laptop
   - Mobile phone
   - Outlook
   - VPN client
   - Browser password manager
   - Wi-Fi profile
   - Mapped drives
   - Email clients
4. Ask the user to wait a few minutes and retry.
5. If the account locks again, check sign-in logs.
6. If lockouts are coming from unfamiliar locations, escalate to security.

User-facing response:

Your account may be locked because of repeated failed login attempts. After it is unlocked, please update any saved passwords on your phone, laptop, VPN client, email app, and browser password manager so the lockout does not happen again.

Escalate if:

- Lockout repeats after password update.
- Sign-in logs show suspicious locations.
- User did not attempt the logins.
- There are repeated MFA prompts.
- Account belongs to a privileged user.

---

## 3.3 Password Reset

Employees should reset passwords using the approved self-service password reset portal whenever possible.

Password requirements:

- Must meet company minimum length.
- Must not reuse recent passwords.
- Must not contain the user's name or email.
- Must not use common passwords.
- Must be unique to company systems.
- Must not be shared with anyone.
- Should be stored only in an approved password manager.

Password reset steps:

1. Go to the official password reset portal.
2. Enter corporate email address.
3. Complete MFA verification.
4. Create a new password.
5. Wait for synchronization.
6. Sign out and sign back into all applications.
7. Update saved passwords on all devices.

Important note:

After resetting your password, it may take several minutes for all services to recognize the new password.

Escalate if:

- User cannot complete MFA.
- User does not receive password reset notification.
- Reset portal is unavailable.
- Account appears compromised.
- User is unable to verify identity.
- User has no registered recovery methods.

---

## 3.4 Password Reset Does Not Work

Possible causes:

- Password does not meet policy.
- User is entering old password.
- Browser cache issue.
- Password sync delay.
- Account locked.
- MFA failure.
- Identity provider outage.
- User account disabled.

Troubleshooting:

1. Try a private or incognito browser window.
2. Clear browser cache for the login portal.
3. Wait 5 to 15 minutes after password reset.
4. Confirm Caps Lock is off.
5. Try logging into the SSO portal directly.
6. Try another browser.
7. If using VPN, disconnect and reconnect.
8. If still failing, escalate to identity support.

User-facing response:

If the password reset completed successfully, please wait a few minutes, then try signing into the company SSO portal from a private browser window. Make sure Caps Lock is off and that you are using your full corporate email address.

---

# 4. Multi-Factor Authentication

## 4.1 MFA Prompt Not Received

Common causes:

- Phone has no internet.
- Authenticator notifications are disabled.
- Device time is incorrect.
- User changed phone.
- MFA registration expired.
- Push notifications blocked.
- Conditional access policy issue.
- Authenticator app needs update.
- User is checking the wrong device.

Troubleshooting:

1. Ask the user to open the authenticator app manually.
2. Ask the user to check notification permissions.
3. Confirm the phone has internet connectivity.
4. Confirm date and time are set automatically.
5. Ask the user to try a one-time code instead of push notification.
6. Restart the phone.
7. Update the authenticator app.
8. Try again after a few minutes.
9. If the user changed phones, follow MFA re-registration.

User-facing response:

Open your authenticator app directly and check whether a sign-in request or one-time code is available. Also confirm your phone has internet access, notifications are enabled, and the device time is set automatically.

---

## 4.2 New Phone MFA Setup

If the user has a new phone and cannot access MFA:

1. Verify the user's identity according to help desk procedure.
2. Remove the old MFA device only if authorized.
3. Require the user to re-register MFA through the official security portal.
4. Confirm at least one backup method is configured.
5. Remind the user not to approve unexpected MFA prompts.

User-facing response:

Because MFA protects your account, IT must verify your identity before resetting your MFA device. After verification, you can register your new phone through the official MFA setup portal.

Escalate to security if:

- User says they received MFA prompts they did not initiate.
- User approved a suspicious MFA request.
- User lost their phone and believes it may be stolen.
- User cannot verify identity.
- User is a privileged administrator.

---

## 4.3 MFA Fatigue Attack

An MFA fatigue attack occurs when an attacker repeatedly sends MFA push requests hoping the user approves one.

User instructions:

1. Do not approve unexpected MFA prompts.
2. Change password immediately using the official portal.
3. Report the incident to security.
4. Disconnect suspicious sessions if possible.
5. Contact IT support.
6. Review recent sign-in activity if available.

Chatbot response:

Do not approve the MFA request. Unexpected MFA prompts may indicate someone has your password. Please change your password immediately through the official password reset portal and report this to the security team.

Escalation:

Escalate immediately to Security Operations.

---

## 4.4 MFA Code Invalid

Common causes:

- Device time is incorrect.
- User entered old code.
- User selected wrong account in authenticator.
- Code expired.
- App is out of sync.
- MFA registration is stale.

Troubleshooting:

1. Confirm phone time is set automatically.
2. Open authenticator and select the correct corporate account.
3. Enter the latest code before it expires.
4. Restart authenticator app.
5. Update authenticator app.
6. Try another MFA method if available.
7. Re-register MFA if authorized.

---

# 5. VPN Support

## 5.1 User Cannot Connect to VPN

Common causes:

- No internet connection.
- Incorrect credentials.
- Expired password.
- MFA issue.
- VPN client outdated.
- Device not compliant.
- VPN service outage.
- Firewall or ISP blocking connection.
- Split tunnel configuration issue.
- Certificate expired.
- User not in VPN access group.

Troubleshooting:

1. Confirm internet works without VPN.
2. Restart the VPN client.
3. Restart the laptop.
4. Confirm credentials work in the SSO portal.
5. Check whether the MFA prompt appears.
6. Try another network such as mobile hotspot.
7. Confirm system date and time are correct.
8. Check VPN client version.
9. Reinstall VPN client if corrupted.
10. Confirm user is authorized for VPN access.
11. Escalate if multiple users are affected.

User-facing response:

First confirm your internet works without VPN. Then restart the VPN client and try signing in with your corporate email and current password. If the MFA prompt does not appear, open your authenticator app manually.

---

## 5.2 VPN Connected but Internal Apps Not Working

Common causes:

- DNS issue.
- Split tunnel routing issue.
- Internal application outage.
- User lacks access.
- Browser cache issue.
- Expired session.
- Firewall rule issue.
- Local network conflict.
- Internal app requires a different VPN profile.

Troubleshooting:

1. Disconnect and reconnect VPN.
2. Try accessing a known internal site.
3. Test with a private browser window.
4. Clear DNS cache.
5. Confirm the app URL is correct.
6. Check whether the issue affects other users.
7. Verify user has required access.
8. Try another network.
9. Escalate to network or application team.

Mac DNS flush:

sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder

Windows DNS flush:

ipconfig /flushdns

---

## 5.3 VPN Slow Performance

Common causes:

- Weak home internet.
- VPN congestion.
- Large file transfers.
- Background updates.
- Wi-Fi interference.
- Using far VPN region.
- Heavy video calls.
- ISP throttling.
- Device resource exhaustion.

Troubleshooting:

1. Run speed test without VPN.
2. Connect using wired Ethernet if possible.
3. Restart router.
4. Close unnecessary apps.
5. Pause large downloads.
6. Try a different VPN region if available.
7. Use split tunneling if approved.
8. Restart laptop.
9. Escalate if many users report slowness.

User-facing response:

VPN slowness is often caused by weak Wi-Fi, heavy background traffic, or VPN congestion. Please test your internet without VPN, restart your router, close large downloads, and reconnect to VPN.

---

## 5.4 VPN Authentication Loop

Symptoms:

- User signs in repeatedly.
- MFA prompt repeats.
- VPN never connects.
- Browser opens login repeatedly.

Troubleshooting:

1. Sign out of VPN client.
2. Quit VPN client completely.
3. Clear browser cookies for SSO portal.
4. Restart VPN client.
5. Try private browser authentication if supported.
6. Confirm password is current.
7. Confirm MFA is working.
8. Reinstall VPN client if needed.

---

# 6. Wi-Fi and Network Issues

## 6.1 Cannot Connect to Office Wi-Fi

Common causes:

- Incorrect Wi-Fi profile.
- Expired password.
- Certificate issue.
- Device not enrolled.
- MAC address randomization.
- Wi-Fi outage.
- Weak signal.
- User not authorized for corporate Wi-Fi.
- Old saved credentials.

Troubleshooting:

1. Forget the Wi-Fi network.
2. Restart the device.
3. Reconnect using corporate credentials.
4. Confirm device is managed and compliant.
5. Disable private/random MAC address for corporate Wi-Fi if required.
6. Move closer to access point.
7. Try guest Wi-Fi if allowed.
8. Escalate if multiple users are affected.

Windows forget Wi-Fi:

Settings > Network & Internet > Wi-Fi > Manage known networks > Forget

Mac forget Wi-Fi:

System Settings > Wi-Fi > Details > Forget This Network

---

## 6.2 Internet Works but Company Apps Do Not

Likely causes:

- VPN disconnected.
- DNS issue.
- SSO issue.
- App outage.
- Browser cache.
- Firewall block.
- Account access issue.
- Required access missing.

Troubleshooting:

1. Confirm VPN is connected if app requires VPN.
2. Try the company SSO portal.
3. Try another browser.
4. Clear browser cache.
5. Check app status page if available.
6. Verify user access.
7. Escalate to app owner.

---

## 6.3 Network Troubleshooting Commands

Windows:

ipconfig /all
ipconfig /flushdns
ping google.com
ping internal.company.com
nslookup internal.company.com
tracert internal.company.com

Mac:

ifconfig
scutil --dns
ping google.com
nslookup internal.company.com
traceroute internal.company.com

Linux:

ip addr
resolvectl status
ping google.com
dig internal.company.com
traceroute internal.company.com

---

## 6.4 Cannot Access Internet

Troubleshooting:

1. Confirm Wi-Fi is enabled.
2. Confirm user is connected to correct network.
3. Restart browser.
4. Restart device.
5. Restart router if at home.
6. Try another website.
7. Try another device on same network.
8. Disable VPN temporarily.
9. Renew IP address.
10. Escalate if office-wide issue.

Windows renew IP:

ipconfig /release
ipconfig /renew

Mac renew DHCP:

System Settings > Network > Wi-Fi > Details > TCP/IP > Renew DHCP Lease

---

# 7. Email and Outlook Support

## 7.1 Outlook Not Opening

Troubleshooting:

1. Restart Outlook.
2. Restart computer.
3. Check internet connection.
4. Open Outlook Web.
5. Start Outlook in safe mode.
6. Disable suspicious add-ins.
7. Repair Office installation.
8. Recreate Outlook profile if needed.

Windows safe mode:

outlook.exe /safe

Escalate if:

- Mailbox appears corrupted.
- User cannot access Outlook Web.
- Multiple users are affected.
- Email delivery is delayed company-wide.
- User is missing critical mailbox data.

---

## 7.2 Emails Not Sending

Common causes:

- Offline mode.
- Large attachment.
- Expired login session.
- Mailbox full.
- Blocked recipient.
- Incorrect address.
- Network issue.
- Email security policy.
- Mail server issue.

Troubleshooting:

1. Check Outbox.
2. Confirm Outlook is not in offline mode.
3. Try sending a small test email.
4. Remove large attachments.
5. Use file-sharing link instead of attachment.
6. Sign out and sign back in.
7. Test Outlook Web.
8. Escalate if delivery failure includes security block.

---

## 7.3 Emails Not Receiving

Troubleshooting:

1. Check Junk or Spam folder.
2. Check Focused Inbox or filters.
3. Check mailbox storage quota.
4. Search by sender email.
5. Check email rules.
6. Confirm sender address.
7. Test with another sender.
8. Check Outlook Web.
9. Escalate to email admin if external mail is blocked.

---

## 7.4 Calendar Sync Issue

Troubleshooting:

1. Refresh calendar.
2. Check Outlook Web calendar.
3. Remove and re-add account on mobile.
4. Confirm user has permissions for shared calendar.
5. Check timezone settings.
6. Restart Outlook.
7. Recreate Outlook profile if needed.

User-facing response:

Please check whether the calendar appears correctly in Outlook Web. If it works there but not in the desktop app, the issue is likely local sync or profile-related.

---

## 7.5 Shared Mailbox Access

Shared mailbox access requires manager or mailbox owner approval.

Process:

1. User submits access request.
2. Manager or mailbox owner approves.
3. Email admin grants access.
4. User waits for propagation.
5. User restarts Outlook.
6. Mailbox appears automatically or is manually added.

Expected propagation:

Access changes may take 15 minutes to several hours to appear.

---

## 7.6 Email Signature Setup

General steps:

1. Open Outlook.
2. Go to Settings or Options.
3. Select Mail.
4. Select Compose and Reply or Signatures.
5. Create or update signature.
6. Include approved name, title, department, phone, and company details.
7. Save changes.
8. Send a test email.

Do not include unapproved logos, legal disclaimers, or personal quotes if company policy prohibits them.

---

# 8. Microsoft Teams and Collaboration Tools

## 8.1 Teams Not Opening

Troubleshooting:

1. Restart Teams.
2. Quit Teams completely.
3. Restart computer.
4. Clear Teams cache.
5. Try Teams web app.
6. Check for updates.
7. Reinstall Teams.

Windows Teams cache path:

%appdata%\Microsoft\Teams

Mac Teams cache path:

~/Library/Application Support/Microsoft/Teams

---

## 8.2 Teams Audio or Camera Not Working

Troubleshooting:

1. Check microphone and camera permissions.
2. Confirm correct audio device is selected.
3. Test in Teams settings.
4. Restart Teams.
5. Close other apps using camera.
6. Restart computer.
7. Try Teams web version.
8. Update audio or video drivers if needed.

User-facing response:

Please check Teams device settings and confirm the correct microphone, speaker, and camera are selected. Also close other apps that may be using the camera.

---

## 8.3 User Cannot Join Meeting

Common causes:

- Expired meeting link.
- User not invited.
- External access blocked.
- Browser issue.
- Teams outage.
- Account authentication issue.
- Organizer lobby settings.

Troubleshooting:

1. Try opening the link in a browser.
2. Try Teams desktop app.
3. Sign out and sign back in.
4. Ask organizer to resend invite.
5. Check if external guests are allowed.
6. Escalate if many users are affected.

---

## 8.4 Teams Messages Not Syncing

Troubleshooting:

1. Refresh Teams.
2. Sign out and sign back in.
3. Check Teams web.
4. Clear Teams cache.
5. Update Teams.
6. Restart computer.
7. Escalate if messages are missing for multiple users.

---

# 9. Software Installation

## 9.1 Requesting Software

Employees must install software only through approved channels.

Approved sources:

- Company software portal
- Managed app store
- IT-approved installer
- Vendor website approved by IT

Do not install:

- Pirated software
- Cracked tools
- Unknown browser extensions
- Unapproved VPN tools
- Crypto miners
- Unverified remote access tools
- Software from suspicious links
- Unknown AI tools handling company data without approval

Software request process:

1. Submit software request.
2. Provide business justification.
3. Manager approves if required.
4. Security reviews if needed.
5. IT deploys software.
6. User confirms installation.

---

## 9.2 Software Requires Admin Rights

Standard users should not receive permanent local admin rights unless approved.

Options:

- Temporary privilege elevation
- IT-assisted installation
- Managed deployment
- Approved self-service installation

Chatbot response:

For security reasons, standard accounts do not have permanent admin rights. Please submit a software installation request with the application name, vendor, download link, and business justification.

---

## 9.3 Application Crashes

Troubleshooting:

1. Restart the app.
2. Restart computer.
3. Check for updates.
4. Clear application cache.
5. Confirm license status.
6. Reinstall app.
7. Check logs.
8. Escalate to application owner.

Information to collect:

- App name
- Version
- Operating system
- Error message
- Steps to reproduce
- Screenshot
- Time issue started
- Whether other users are affected

---

## 9.4 License Activation Issue

Common causes:

- User not assigned license.
- License expired.
- User signed into wrong account.
- Device limit reached.
- Vendor service outage.
- Network blocked license activation.

Troubleshooting:

1. Confirm user is signed in with corporate account.
2. Confirm license assignment.
3. Ask user to sign out and sign back in.
4. Check internet or VPN requirement.
5. Check vendor status.
6. Reassign license if authorized.
7. Escalate to software asset management.

---

# 10. Laptop and Workstation Support

## 10.1 Laptop Is Slow

Common causes:

- Too many startup apps.
- Low disk space.
- Low memory.
- Background updates.
- Malware.
- Old hardware.
- Too many browser tabs.
- Cloud sync overload.
- Failing disk.
- Heavy antivirus scan.

Troubleshooting:

1. Restart laptop.
2. Check disk space.
3. Close unused applications.
4. Check Task Manager or Activity Monitor.
5. Install pending updates.
6. Run approved security scan.
7. Remove unnecessary startup apps.
8. Escalate for hardware assessment.

Windows:

Ctrl + Shift + Esc > Task Manager

Mac:

Applications > Utilities > Activity Monitor

---

## 10.2 Laptop Will Not Turn On

Troubleshooting:

1. Connect charger.
2. Check power outlet.
3. Try another charger if available.
4. Hold power button for 15 seconds.
5. Disconnect peripherals.
6. Try power reset.
7. Check for charging light.
8. Escalate to hardware support.

Do not advise the user to open the laptop unless they are authorized.

---

## 10.3 Blue Screen or Kernel Panic

Collect:

- Screenshot or error code
- Time of crash
- Recent changes
- Connected peripherals
- Whether crash repeats
- Device serial number

Troubleshooting:

1. Restart device.
2. Disconnect external devices.
3. Install OS updates.
4. Check storage health.
5. Update drivers.
6. Run diagnostics.
7. Escalate if repeated.

---

## 10.4 Disk Space Full

Troubleshooting:

1. Empty recycle bin or trash.
2. Remove temporary files.
3. Move large files to approved cloud storage.
4. Delete old downloads.
5. Clear browser cache.
6. Check sync folders.
7. Do not delete system folders.
8. Escalate if system drive remains full.

Windows:

Settings > System > Storage

Mac:

System Settings > General > Storage

---

## 10.5 External Monitor Not Working

Troubleshooting:

1. Confirm monitor is powered on.
2. Check cable connection.
3. Try another cable.
4. Try another port.
5. Restart laptop.
6. Detect displays manually.
7. Confirm dock is powered.
8. Update display drivers.
9. Test monitor with another device.

Windows:

Settings > System > Display > Multiple displays > Detect

Mac:

System Settings > Displays

---

## 10.6 Docking Station Not Working

Troubleshooting:

1. Disconnect and reconnect dock.
2. Confirm dock power adapter is connected.
3. Restart laptop.
4. Try another USB-C or Thunderbolt port.
5. Update dock firmware if applicable.
6. Test with another laptop.
7. Replace dock if hardware failure is confirmed.

---

# 11. Printer and Scanner Support

## 11.1 Cannot Print

Common causes:

- Printer offline.
- Wrong printer selected.
- Paper jam.
- No toner.
- Network issue.
- Driver issue.
- User not authorized.
- Print queue stuck.
- Printer out of paper.

Troubleshooting:

1. Confirm printer is powered on.
2. Check printer display for errors.
3. Confirm correct printer is selected.
4. Restart printer.
5. Clear print queue.
6. Restart computer.
7. Reinstall printer driver.
8. Try another printer.
9. Escalate to facilities or printer vendor if hardware issue.

---

## 11.2 Print Job Stuck

Windows:

Settings > Bluetooth & devices > Printers & scanners > Select printer > Open print queue > Cancel jobs

Mac:

System Settings > Printers & Scanners > Select printer > Open Print Queue > Cancel jobs

Then restart printer and try again.

---

## 11.3 Scanner Not Working

Troubleshooting:

1. Confirm scanner is powered on.
2. Check connection.
3. Restart scanner.
4. Confirm user has scanning permissions.
5. Try scan-to-email.
6. Try scan-to-folder.
7. Check address book entry.
8. Escalate if network folder permissions fail.

---

# 12. File Access and Shared Drives

## 12.1 User Cannot Access Shared Folder

Common causes:

- User lacks permission.
- Group membership not updated.
- VPN disconnected.
- Folder moved.
- Mapped drive stale.
- File server issue.
- User signed into wrong account.

Troubleshooting:

1. Confirm exact folder path.
2. Confirm user is on VPN if remote.
3. Ask whether colleagues can access it.
4. Verify access request approval.
5. Refresh group membership.
6. Ask user to sign out and sign back in.
7. Re-map drive if needed.
8. Escalate to file services team.

---

## 12.2 Requesting Shared Folder Access

Process:

1. User submits access request.
2. Folder owner approves.
3. Manager approves if required.
4. IT adds user to access group.
5. User signs out and signs back in.
6. Access is verified.

Chatbot response:

Access to shared folders requires approval from the folder owner or manager. Please submit the folder path and business reason for access.

---

## 12.3 File Deleted Accidentally

Troubleshooting:

1. Check recycle bin.
2. Check cloud storage version history.
3. Check previous versions.
4. Ask when file was last seen.
5. Ask exact file name and path.
6. Escalate to backup team if not recoverable.

Important:

The sooner a deleted file is reported, the better the chance of recovery.

---

## 12.4 File Locked by Another User

Troubleshooting:

1. Ask the other user to close the file.
2. Wait a few minutes.
3. Check whether file is open in Office web app.
4. Restart Office application.
5. Avoid force-unlocking unless approved.
6. Escalate if file remains locked.

---

## 12.5 OneDrive or Cloud Sync Issue

Common causes:

- User not signed in.
- Sync paused.
- File path too long.
- Invalid file name.
- Storage full.
- Network issue.
- Conflicting file versions.

Troubleshooting:

1. Check sync client status.
2. Confirm user is signed in.
3. Resume sync.
4. Rename files with invalid characters.
5. Shorten long folder paths.
6. Check storage quota.
7. Restart sync client.
8. Check web version of file.
9. Escalate if files are missing.

---

# 13. Browser Issues

## 13.1 Website Not Loading

Troubleshooting:

1. Refresh page.
2. Try another browser.
3. Try private or incognito mode.
4. Clear cache and cookies.
5. Disable extensions temporarily.
6. Confirm internet or VPN.
7. Check if website works for others.
8. Escalate to app owner if internal site.

---

## 13.2 Clear Browser Cache

Chrome:

Settings > Privacy and security > Delete browsing data

Edge:

Settings > Privacy, search, and services > Clear browsing data

Safari:

Safari > Settings > Privacy > Manage Website Data

Recommended first step:

Clear cache and cookies only for the affected website if possible.

---

## 13.3 Browser Extension Issue

Signs:

- Page elements missing.
- Login loops.
- Buttons do not work.
- Site works in incognito but not normal browser.
- Ads or pop-ups appear unexpectedly.
- Browser redirects to unknown pages.

Resolution:

1. Disable extensions.
2. Reload site.
3. Re-enable extensions one at a time.
4. Remove unapproved extensions.
5. Escalate suspicious extensions to security.

---

## 13.4 SSO Login Loop in Browser

Troubleshooting:

1. Open the site in private or incognito mode.
2. Clear cookies for the SSO domain.
3. Sign out of all accounts.
4. Close and reopen browser.
5. Try a different browser.
6. Confirm system time is correct.
7. Confirm third-party cookies are not blocked if required.
8. Escalate if multiple users are affected.

---

# 14. Remote Work Support

## 14.1 Remote Employee Cannot Work

Check:

- Internet connection
- VPN access
- MFA
- Device compliance
- Email access
- Required applications
- Hardware condition
- Power availability

Basic remote work recovery steps:

1. Restart laptop.
2. Restart home router.
3. Confirm internet works.
4. Connect to VPN.
5. Test SSO portal.
6. Test email.
7. Test required application.
8. Escalate according to severity.

---

## 14.2 Home Wi-Fi Is Unstable

Recommendations:

- Move closer to router.
- Restart router.
- Use 5 GHz Wi-Fi if close to router.
- Use Ethernet if possible.
- Avoid heavy streaming during calls.
- Use mobile hotspot temporarily.
- Contact ISP if home internet is down.

IT should not directly manage personal routers unless company policy allows it.

---

## 14.3 Mobile Hotspot Guidance

Use mobile hotspot temporarily when:

- Home internet is down.
- VPN does not work on home Wi-Fi.
- User needs urgent access.
- ISP has an outage.

Security notes:

- Use phone hotspot with WPA2 or WPA3 security.
- Do not use public open Wi-Fi for sensitive work unless VPN is connected.
- Avoid large downloads on mobile hotspot.

---

# 15. Security Incidents

## 15.1 Suspected Phishing Email

User instructions:

1. Do not click links.
2. Do not open attachments.
3. Do not reply.
4. Use the phishing report button if available.
5. Forward to security mailbox only if policy allows.
6. Delete only after reporting.

Chatbot response:

Do not click any links or open attachments. Please report the email using the company phishing report button. If you already clicked a link or entered credentials, tell IT immediately.

Escalate immediately if:

- User clicked the link.
- User entered credentials.
- User opened an attachment.
- User approved MFA prompt.
- Multiple employees received the same email.
- Email impersonates an executive or vendor payment request.

---

## 15.2 User Clicked Phishing Link

Immediate actions:

1. Ask the user to stop interacting with the page.
2. Ask whether they entered credentials.
3. Ask whether they downloaded or opened anything.
4. Ask whether they approved MFA.
5. Change password from a trusted device if credentials were entered.
6. Report to Security Operations.
7. Scan device.
8. Check mailbox rules.
9. Review sign-in logs.
10. Monitor account.

Chatbot response:

Since you clicked the link, please stop interacting with the page. If you entered your password or approved MFA, change your password immediately from a trusted device and contact Security Operations.

Escalate:

Immediate Security Operations escalation.

---

## 15.3 Malware Suspicion

Signs:

- Pop-ups.
- Unknown applications.
- Browser redirects.
- Antivirus alerts.
- Slow system.
- Files encrypted.
- Unexpected admin prompts.
- Suspicious network activity.
- Unknown remote access tools.

Immediate user instructions:

1. Disconnect from Wi-Fi or unplug Ethernet if instructed by security.
2. Do not power off unless told by security.
3. Do not delete files.
4. Take a photo of any warning message.
5. Contact IT security.

Escalate:

Immediate Security Operations escalation.

---

## 15.4 Lost or Stolen Device

User instructions:

1. Report immediately to IT.
2. Provide device type and serial number if known.
3. Provide last known location and time.
4. Change password.
5. Security may remotely lock or wipe the device.
6. File police report if required by policy.

Chatbot response:

Please report the lost or stolen device immediately. IT may need to remotely lock or wipe it to protect company data. Also change your corporate password from a trusted device.

Escalate:

Immediate escalation to IT asset management and security.

---

## 15.5 Suspicious Login Alert

Common signs:

- Login from unfamiliar country.
- Login at unusual time.
- Login from unknown device.
- MFA prompt not initiated by user.
- Impossible travel alert.
- New inbox forwarding rule.

Response:

1. Ask user whether they recognize the login.
2. If not recognized, reset password.
3. Revoke active sessions if authorized.
4. Review MFA methods.
5. Remove suspicious mailbox rules.
6. Escalate to security.

Chatbot response:

If you do not recognize the login, treat it as suspicious. Change your password immediately, do not approve any MFA prompts, and report this to Security Operations.

---

# 16. Data Protection and Access Control

## 16.1 Requesting Application Access

Access requests require approval.

Process:

1. User submits request.
2. User provides business justification.
3. Manager approves.
4. Application owner approves if required.
5. IT grants access through role-based group.
6. User signs out and signs back in.
7. User confirms access.

Chatbot response:

Application access requires approval. Please submit the application name, role needed, business reason, and manager approval.

---

## 16.2 Privileged Access Request

Privileged access includes admin rights, production access, database admin rights, cloud admin access, and security tool access.

Requirements:

- Manager approval
- System owner approval
- Security approval
- Time-bound access where possible
- MFA required
- Logging enabled
- Least privilege applied

Chatbot must not approve privileged access.

Chatbot response:

Privileged access requires formal approval and security review. Please submit a privileged access request with the business justification, required permissions, duration, and approver details.

---

## 16.3 Data Loss Prevention Alert

Common triggers:

- Sending sensitive data externally.
- Uploading confidential files to unapproved services.
- Copying sensitive files to USB.
- Sharing customer data publicly.
- Emailing financial or HR data.

Response:

1. Do not bypass DLP controls.
2. Verify business need.
3. Use approved secure sharing method.
4. Contact security or compliance if blocked.
5. Escalate if data was sent externally by mistake.

Chatbot response:

The DLP alert is designed to protect sensitive data. Please do not bypass it. Use an approved secure sharing method or contact Security/Compliance for review.

---

# 17. Hardware Requests and Replacement

## 17.1 New Laptop Request

Process:

1. User submits hardware request.
2. Manager approves.
3. IT checks eligibility.
4. Asset team assigns device.
5. Device is configured.
6. User receives device.
7. User confirms setup.

Required information:

- Employee name
- Department
- Manager
- Business justification
- Role requirements
- Required software
- Shipping address if remote
- Desired start date

---

## 17.2 Replacement Laptop Request

Valid reasons:

- Device failure
- Device lost or stolen
- Device too old
- Performance issue confirmed by IT
- Role requires upgraded hardware
- Battery failure

Troubleshooting should be attempted before replacement unless device is lost, stolen, physically damaged, or unsafe.

---

## 17.3 Damaged Laptop

User instructions:

1. Stop using device if unsafe.
2. Do not attempt self-repair.
3. Report damage to IT.
4. Provide photos if requested.
5. Provide asset tag.
6. IT will advise repair or replacement.

Escalate if:

- Battery swelling.
- Smoke or burning smell.
- Liquid damage.
- Device overheating.
- Electrical hazard.

---

## 17.4 Returning Equipment

Process:

1. IT or HR initiates return.
2. User receives return instructions.
3. User packs device securely.
4. User includes charger and accessories.
5. User ships using approved label.
6. Asset team confirms receipt.
7. Device is wiped and inventoried.

---

# 18. Mobile Device Support

## 18.1 Email Not Working on Phone

Troubleshooting:

1. Confirm internet works.
2. Confirm password was not recently changed.
3. Open Outlook mobile app.
4. Sign out and sign back in.
5. Complete MFA.
6. Update Outlook app.
7. Remove and re-add account.
8. Confirm device compliance.

---

## 18.2 Mobile Device Compliance Issue

Common causes:

- Device encryption disabled.
- Screen lock missing.
- OS outdated.
- Device jailbroken or rooted.
- Management profile missing.
- Company portal app not installed.

Resolution:

1. Update mobile OS.
2. Enable screen lock.
3. Install company portal or MDM app.
4. Enroll device.
5. Wait for compliance check.
6. Retry access.

---

## 18.3 Lost Phone With Company Email

Actions:

1. Report immediately.
2. Change corporate password.
3. Remove device from account if authorized.
4. Security may wipe company data.
5. Re-register MFA if phone was MFA device.

Escalate to security.

---

# 19. Cloud and SaaS Application Support

## 19.1 SaaS App Login Issue

Troubleshooting:

1. Confirm user is using SSO login.
2. Confirm user has app access.
3. Try private browser.
4. Clear cookies.
5. Try another browser.
6. Confirm app is not down.
7. Check user license.
8. Escalate to app owner.

---

## 19.2 SaaS App Permission Issue

Common causes:

- Wrong role assigned.
- Group membership not synced.
- Manager approval missing.
- App owner approval missing.
- License missing.
- User logged into wrong account.

Resolution:

1. Confirm required access level.
2. Confirm business justification.
3. Confirm approval.
4. Assign correct role if authorized.
5. Ask user to sign out and sign back in.
6. Escalate to app owner.

---

## 19.3 SaaS App Data Missing

Troubleshooting:

1. Confirm user is in correct workspace or tenant.
2. Check filters.
3. Check permissions.
4. Check whether data was archived.
5. Check audit logs if authorized.
6. Escalate to app owner.

---

# 20. Database and Developer Support

## 20.1 Developer Cannot Connect to Database

Common causes:

- VPN disconnected.
- IP not allowlisted.
- Credentials expired.
- Database user locked.
- Firewall rule missing.
- Wrong hostname or port.
- SSL certificate issue.
- Database service down.

Troubleshooting:

1. Confirm VPN connection.
2. Confirm hostname and port.
3. Confirm credentials.
4. Check database status.
5. Test network connectivity.
6. Check access group membership.
7. Confirm SSL requirements.
8. Escalate to database team.

---

## 20.2 API Key or Secret Request

Rules:

- Do not share secrets in chat.
- Do not send secrets over email.
- Use approved secret manager.
- Provide least privilege.
- Rotate secrets regularly.
- Revoke unused secrets.
- Escalate suspicious secret exposure.

Chatbot response:

API keys and secrets must be created and shared only through the approved secret management system. Do not paste secrets into chat, tickets, email, or documents.

---

## 20.3 Secret Accidentally Exposed

Immediate actions:

1. Revoke the exposed secret.
2. Rotate credentials.
3. Identify where it was exposed.
4. Remove from repository or document.
5. Check logs for misuse.
6. Notify security.
7. Document incident.

Escalate immediately to security.

---

# 21. RAG Chatbot Support

## 21.1 Chatbot Gives Incorrect Answer

Possible causes:

- Outdated document.
- Missing knowledge base article.
- Poor retrieval.
- Ambiguous user question.
- Model hallucination.
- Incorrect source content.
- Ingestion failure.
- Embedding mismatch.

Resolution:

1. Ask user for the incorrect answer and expected answer.
2. Identify source documents retrieved.
3. Check document freshness.
4. Update or remove stale content.
5. Add clearer article.
6. Re-index knowledge base.
7. Test same query again.
8. Escalate to AI platform team.

---

## 21.2 Chatbot Cannot Find Document

Troubleshooting:

1. Confirm document was uploaded.
2. Confirm document format is supported.
3. Confirm ingestion job completed.
4. Confirm document has readable text.
5. Check chunking configuration.
6. Check embedding generation.
7. Check vector database records.
8. Re-index document.

---

## 21.3 RAG Search Returns Bad Results

Possible causes:

- Query too vague.
- Chunks too large.
- Chunks too small.
- Missing metadata.
- Wrong embedding model.
- Vector dimension mismatch.
- Poor document titles.
- Duplicate outdated documents.

Fixes:

1. Improve document headings.
2. Add FAQ-style sections.
3. Add synonyms and common user phrases.
4. Remove duplicate stale documents.
5. Re-index documents.
6. Tune chunk size.
7. Tune top-k retrieval.
8. Add metadata filters.

---

## 21.4 Embedding Dimension Error

Error example:

expected 1536 dimensions, not 768

Meaning:

The database vector column expects embeddings of one size, but the embedding model is returning a different size.

Common case:

- Database created for OpenAI 1536-dimensional embeddings.
- Local embedding model returns 768-dimensional embeddings.

Resolution options:

Option 1: Use an embedding model that returns the expected dimension.

Option 2: Change vector database schema to match current embedding dimension and re-index all documents.

Important:

All stored document embeddings and query embeddings must use the same embedding model and same dimension.

---

## 21.5 RAG Chatbot API Error

Possible causes:

- Backend API unavailable.
- Vector database unavailable.
- Embedding model unavailable.
- LLM provider unavailable.
- Missing API key.
- Wrong API base URL.
- CORS issue.
- Timeout.
- Model returns unexpected response.

Troubleshooting:

1. Check frontend logs.
2. Check API logs.
3. Check database container.
4. Check embedding provider.
5. Check LLM provider.
6. Verify environment variables.
7. Restart services.
8. Test API endpoint directly.
9. Escalate to platform team.

---

# 22. Docker and Local Development Support

## 22.1 Docker Compose Build Fails

Common causes:

- Dependency lock file out of sync.
- Wrong Python version.
- Missing environment file.
- Docker cache issue.
- Network issue during package install.
- Invalid Dockerfile.
- Missing build context files.

Troubleshooting:

1. Read the first real error in the logs.
2. Rebuild without cache.
3. Confirm Python version.
4. Regenerate lock file if needed.
5. Confirm .env exists.
6. Confirm Docker Desktop is running.
7. Run docker compose ps.
8. Run service-specific logs.

Commands:

docker compose down
docker compose build --no-cache
docker compose up

---

## 22.2 Poetry Lock Error

Error:

pyproject.toml changed significantly since poetry.lock was last generated

Fix:

poetry lock
docker compose up --build

If Python version mismatch occurs:

poetry env use $(which python3)
poetry lock
docker compose up --build

---

## 22.3 Python Version Command

Correct:

python3 --version

Incorrect:

python3--version

There must be a space between python3 and --version.

---

## 22.4 Docker Service Logs

Check all services:

docker compose logs -f

Check API only:

docker compose logs -f api

Check Streamlit UI only:

docker compose logs -f streamlit-ui

Check recent logs:

docker compose logs --tail=100 api

---

## 22.5 Streamlit UI Running but API Error

If Streamlit opens but shows:

Support API error: An unexpected error occurred

Then the UI is running, but backend API returned an error.

Troubleshooting:

1. Check API logs.
2. Confirm API service is running.
3. Confirm Streamlit API URL points to Docker service name.
4. Confirm database is running.
5. Confirm model provider is running.
6. Confirm embedding model dimensions match database.
7. Restart services.

Inside Docker, API URL should usually use service name:

http://api:8000

Not:

http://localhost:8000

---

# 23. Logging and Monitoring

## 23.1 What to Include in a Support Ticket

A useful ticket should include:

- User name
- User email
- Affected device
- Affected application
- Error message
- Screenshot if safe
- Time issue started
- Business impact
- Troubleshooting already attempted
- Whether issue affects others
- Urgency
- Required deadline if any

---

## 23.2 Application Logs

When reviewing logs:

1. Start with timestamp of user issue.
2. Search for user ID or request ID.
3. Look for error level logs.
4. Check upstream dependencies.
5. Check recent deployments.
6. Check authentication failures.
7. Check rate limits.
8. Escalate with relevant log snippets.

Do not expose sensitive logs to end users.

---

## 23.3 Common Error Types

Authentication error:

User cannot prove identity or token is invalid.

Authorization error:

User is authenticated but lacks permission.

Network error:

Client cannot reach server or service.

Timeout:

Service did not respond in expected time.

Validation error:

Input format is incorrect.

Server error:

Application failed internally.

Dependency error:

Database, API, model, or external system is unavailable.

---

# 24. Escalation Matrix

## 24.1 Escalate to Identity Team

Escalate when:

- Account is disabled unexpectedly.
- User cannot reset password.
- MFA reset required.
- SSO outage suspected.
- Conditional access issue.
- Privileged account login issue.
- Repeated lockouts from unknown source.

---

## 24.2 Escalate to Network Team

Escalate when:

- Office Wi-Fi outage.
- VPN outage.
- DNS issue.
- Routing issue.
- Firewall issue.
- Multiple users cannot access internal apps.
- Network latency impacts business operations.

---

## 24.3 Escalate to Security Operations

Escalate when:

- Phishing clicked.
- Credentials entered on suspicious site.
- Malware suspected.
- Lost or stolen device.
- Suspicious login.
- MFA fatigue attack.
- Data leakage.
- Secret exposed.
- Ransomware suspected.
- Unapproved remote access tool found.

---

## 24.4 Escalate to Desktop Support

Escalate when:

- Laptop hardware failure.
- OS corruption.
- Repeated blue screen.
- Docking station failure.
- Printer setup requiring hands-on support.
- Device imaging required.
- Local profile corruption.

---

## 24.5 Escalate to Application Owner

Escalate when:

- User has app-specific error.
- App permissions are incorrect.
- Application data missing.
- Application integration failing.
- Application outage suspected.
- Vendor support required.

---

## 24.6 Escalate to Database Team

Escalate when:

- Database unavailable.
- Connection refused.
- Database permissions issue.
- Query performance issue.
- Backup restore required.
- Data integrity concern.
- Migration failure.

---

## 24.7 Escalate to AI Platform Team

Escalate when:

- RAG retrieval fails.
- Embedding generation fails.
- LLM provider unavailable.
- Vector database error.
- Chatbot hallucination issue.
- Document ingestion failure.
- Model configuration issue.
- Prompt injection concern.

---

# 25. User Communication Templates

## 25.1 Initial Acknowledgement

Thanks for reporting this. I can help troubleshoot. Please share the affected application, the exact error message, and when the issue started. Do not share your password or MFA code.

---

## 25.2 Waiting for Approval

Your request requires approval before IT can make the change. Please submit the business justification and manager or application owner approval.

---

## 25.3 Issue Resolved

This should now be resolved. Please sign out and sign back in, then test again. If the issue continues, reply with the exact error message and timestamp.

---

## 25.4 Escalated to Specialist Team

I’m escalating this to the appropriate support team because it requires deeper access or investigation. Please include any screenshots, timestamps, and steps you already tried.

---

## 25.5 Security Warning

For security reasons, do not share passwords, MFA codes, API keys, private keys, or confidential data in this chat. Use the approved secure process instead.

---

## 25.6 Phishing Response

Do not click any links, open attachments, or reply to the message. Please report it using the company phishing report button. If you already clicked or entered credentials, contact Security Operations immediately.

---

# 26. Common Employee Questions and Answers

## Q: I forgot my password. What should I do?

Use the official company password reset portal. Enter your corporate email, complete MFA, and create a new password. After resetting, update saved passwords on your phone, laptop, VPN client, Outlook, and browser password manager.

---

## Q: My account is locked. Can you unlock it?

Your account may be locked due to repeated failed login attempts. IT must verify your identity before unlocking it. After unlock, update saved passwords on all devices to prevent another lockout.

---

## Q: I got an MFA prompt I did not request. What should I do?

Do not approve it. Change your password immediately from the official password reset portal and report the incident to Security Operations.

---

## Q: My VPN is not connecting. What should I try?

Confirm your internet works without VPN. Restart the VPN client and your laptop. Check that your password works in the SSO portal and that MFA is working. If possible, try another network such as a mobile hotspot.

---

## Q: VPN is connected, but internal sites do not open. What should I do?

Disconnect and reconnect VPN, try a private browser window, clear DNS cache, and confirm the internal URL is correct. If colleagues also cannot access the site, it may be an application or network issue.

---

## Q: Outlook is not sending emails. What should I check?

Check your Outbox, confirm Outlook is not offline, remove large attachments, try sending a small test email, and test Outlook Web. If Outlook Web also fails, escalate to email support.

---

## Q: I need access to a shared folder. What is the process?

Submit an access request with the folder path, business reason, and manager or folder owner approval. After access is granted, sign out and sign back in.

---

## Q: I need admin rights to install software. Can I get them?

Permanent admin rights are restricted. Submit a software installation request with the app name, vendor, download link, and business justification. IT can install it through approved methods.

---

## Q: I clicked a suspicious email link. What should I do?

Stop interacting with the page. If you entered credentials or approved MFA, change your password immediately from a trusted device and contact Security Operations.

---

## Q: My laptop is very slow. What should I do?

Restart the laptop, close unused apps, check disk space, install updates, and check Task Manager or Activity Monitor for high CPU or memory usage. If slowness continues, contact desktop support.

---

## Q: My device was stolen. What should I do?

Report it immediately to IT and Security. Provide the device type, asset tag or serial number if known, last known location, and time of loss. Change your corporate password from a trusted device.

---

## Q: The chatbot gave a wrong answer. What should I do?

Report the incorrect answer, the question you asked, and the expected answer. The AI platform team should review the retrieved source documents, update stale content, and re-index the knowledge base.

---

# 27. Safety Rules for the Chatbot

The chatbot must never:

- Ask for passwords.
- Ask for MFA codes.
- Reveal secrets.
- Provide private keys.
- Approve access requests.
- Disable security controls.
- Bypass MFA.
- Tell users how to evade monitoring.
- Provide malware instructions.
- Expose confidential logs.
- Share another user's information.
- Make HR, legal, payroll, or compliance decisions.
- Claim an issue is fixed without confirmation.
- Guess when the answer is not in the knowledge base.

The chatbot should:

- Ask for safe troubleshooting details.
- Provide step-by-step guidance.
- Encourage official portals and approved processes.
- Escalate security issues immediately.
- State when approval is required.
- State when it does not have enough information.
- Recommend contacting IT for identity verification.
- Cite or reference relevant internal policy where available.

---

# 28. Knowledge Base Writing Guidelines for RAG

To improve chatbot retrieval quality:

1. Use clear headings.
2. Include common user phrases.
3. Include symptoms and causes.
4. Include step-by-step fixes.
5. Add escalation conditions.
6. Keep each topic self-contained.
7. Avoid vague references like “see above.”
8. Include synonyms.
9. Remove outdated content.
10. Re-index after updates.

Good heading:

VPN Connected But Internal Apps Not Working

Bad heading:

More troubleshooting

Good content:

If VPN connects but internal applications do not load, the likely causes are DNS, routing, app permissions, or internal app outage.

Bad content:

This sometimes happens. Try the usual stuff.

---

# 29. Approved Troubleshooting Checklist

Before escalating a normal user issue, check:

- Has the user restarted the application?
- Has the user restarted the device?
- Is the user connected to internet?
- Is VPN required?
- Is the user signed into the correct account?
- Does the issue happen in another browser?
- Does the issue happen in web version?
- Is there an exact error message?
- Is the issue affecting multiple users?
- Did the issue start after a password change?
- Did the issue start after a software update?
- Is there a known outage?
- Does the user have required access?

---

# 30. Incident Response Quick Guide

## Security Incident Priority

Immediate escalation required for:

- Ransomware
- Malware
- Phishing with credential entry
- Suspicious login
- MFA fatigue
- Lost or stolen device
- Data leak
- Secret exposure
- Unauthorized admin access
- Unapproved remote control tool

## User Instructions During Security Incident

Tell the user:

1. Stop interacting with suspicious content.
2. Do not delete evidence.
3. Do not forward suspicious files broadly.
4. Do not approve MFA prompts.
5. Contact Security Operations.
6. Change password only through official portal.
7. Use a trusted device if account compromise is suspected.

---

# 31. Service Restart Guidance

Restarting a local application is safe for users.

Examples:

- Restart browser.
- Restart Outlook.
- Restart Teams.
- Restart VPN client.
- Restart laptop.

Restarting servers or production services requires authorization.

The chatbot must not instruct regular users to restart production services, disable firewalls, stop endpoint protection, or delete system files.

---

# 32. Common Command Reference

## Windows

Check IP:

ipconfig

Flush DNS:

ipconfig /flushdns

Ping:

ping google.com

Trace route:

tracert internal.company.com

Open Task Manager:

Ctrl + Shift + Esc

Open Outlook safe mode:

outlook.exe /safe

---

## Mac

Check network:

ifconfig

Flush DNS:

sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder

Ping:

ping google.com

Trace route:

traceroute internal.company.com

Open Activity Monitor:

Applications > Utilities > Activity Monitor

---

## Docker

Start services:

docker compose up

Start and rebuild:

docker compose up --build

Stop services:

docker compose down

Stop and remove volumes:

docker compose down -v

View all logs:

docker compose logs -f

View API logs:

docker compose logs -f api

View Streamlit logs:

docker compose logs -f streamlit-ui

Check running containers:

docker compose ps

Rebuild without cache:

docker compose build --no-cache

---

## Python and Poetry

Check Python version:

python3 --version

Set Poetry environment:

poetry env use $(which python3)

Update lock file:

poetry lock

Install dependencies:

poetry install

Export requirements:

poetry export -f requirements.txt --without-hashes -o requirements.txt

---

# 33. Known Issues and Fixes

## Known Issue: Poetry Lock Out of Sync

Error:

pyproject.toml changed significantly since poetry.lock was last generated

Fix:

poetry lock
docker compose up --build

If Python mismatch:

poetry env use $(which python3)
poetry lock
docker compose up --build

---

## Known Issue: Python Version Not Allowed

Error:

Current Python version is not allowed by the project

Fix:

Use a Python version allowed by the project.

Example:

python3 --version
poetry env use $(which python3)
poetry lock

---

## Known Issue: Streamlit Shows Support API Error

Error:

Support API error: An unexpected error occurred

Meaning:

Frontend is running, but backend API failed.

Fix:

docker compose logs --tail=100 api
docker compose ps

Check for:

- API crash
- Database issue
- Embedding model issue
- Missing environment variable
- Wrong API URL
- LLM provider issue

---

## Known Issue: pgvector Dimension Mismatch

Error:

expected 1536 dimensions, not 768

Meaning:

Database vector column expects 1536-dimensional embeddings, but current embedding model returns 768-dimensional embeddings.

Fix option 1:

Use an embedding model that returns 1536 dimensions.

Fix option 2:

Change database schema to 768 dimensions and re-index all documents.

Important:

After changing embedding dimensions, remove old vector database volume or migrate schema properly.

Example for local dev reset:

docker compose down -v
docker compose up --build

---

# 34. Access Approval Rules

Access should follow least privilege.

Before granting access:

1. Confirm user identity.
2. Confirm business need.
3. Confirm manager approval.
4. Confirm system owner approval if required.
5. Grant only required role.
6. Prefer group-based access.
7. Set expiration for temporary access.
8. Log the change.

Do not grant access based only on chat request if policy requires approval.

---

# 35. Data Handling Rules

Employees must:

- Store company data only in approved systems.
- Avoid saving sensitive data locally unless approved.
- Use secure sharing links.
- Avoid public file-sharing sites.
- Avoid sending confidential data to personal email.
- Report accidental data sharing.
- Follow data retention policies.

Chatbot response for risky sharing:

Company data should only be shared through approved tools. Please avoid sending confidential files through personal email or public file-sharing services.

---

# 36. AI Tool Usage Rules

Employees using AI tools must:

- Use only approved AI tools.
- Not paste confidential company data into unapproved AI services.
- Not upload customer data without approval.
- Review AI-generated output before use.
- Avoid sharing secrets, credentials, or proprietary code.
- Follow company AI policy.

Chatbot response:

Please use only approved AI tools for company work. Do not paste confidential data, customer records, source code secrets, API keys, or credentials into unapproved AI services.

---

# 37. End-User Device Security

Employees should:

- Keep devices updated.
- Use screen lock.
- Do not share laptops.
- Do not install unapproved software.
-