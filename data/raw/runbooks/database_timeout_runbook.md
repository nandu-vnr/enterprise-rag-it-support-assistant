# Database Timeout Runbook

## Connection Timeouts
This runbook explains how to resolve database timeouts and connection saturation.

### Step 1: Confirm Database Health
Validate that the PostgreSQL cluster is healthy and reachable.

### Step 2: Review Connection Pools
Inspect application connection pool settings and current active connections.

### Step 3: Check Query Performance
Identify expensive queries or missing indexes that could cause timeouts.

### Step 4: Restart Connection Pool
If safe, restart the application connection pool after resolving the root cause.

### Escalation
Escalate to the DBA team when the timeout persists after connection and query tuning.
