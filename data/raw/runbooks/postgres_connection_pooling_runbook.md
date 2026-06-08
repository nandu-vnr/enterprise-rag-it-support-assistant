# PostgreSQL Connection Pooling Runbook

## Connection Pool Saturation
Use this runbook when application requests are timing out because the database connection pool is exhausted.

### Step 1: Confirm Database Reachability
Check that the PostgreSQL cluster is up and accepting connections.

### Step 2: Review Active Connections
Inspect active sessions and compare them to the configured pool limits.

### Step 3: Reduce Connection Pressure
Throttle noisy jobs, close idle sessions, and confirm the application is not leaking connections.

### Step 4: Tune Pool Settings
Adjust the pool size and overflow limits if the workload has grown beyond the current configuration.

### Escalation
Escalate to the DBA team if connection saturation continues after tuning and workload reduction.
