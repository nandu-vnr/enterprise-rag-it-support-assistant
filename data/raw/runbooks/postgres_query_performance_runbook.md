# PostgreSQL Query Performance Runbook

## Slow Query Investigation
Use this runbook when database requests are slow but the service is still reachable.

### Step 1: Identify the Slow Query
Check logs and APM traces for repeated query patterns with high latency.

### Step 2: Review Execution Plans
Inspect the query plan for sequential scans, missing indexes, or inefficient joins.

### Step 3: Validate Index Coverage
Confirm the affected table has the expected indexes for the filtering and join columns.

### Step 4: Reduce Lock Contention
Look for long-running transactions or lock waits that may be delaying the query.

### Escalation
Escalate to the DBA team if the query remains slow after indexing and transaction review.
