# Database Connection Timeout

## Overview
An application began timing out when opening database connections during peak traffic.

## Symptoms
- Requests fail with connection timeout errors
- Connection pool usage stays at or near the maximum
- New sessions wait longer than expected before acquiring a connection

## Investigation
1. Confirm the PostgreSQL server is reachable.
2. Compare the active connection count with the configured pool size.
3. Check for long-running queries or idle transactions that hold connections open.
4. Review recent deployment changes that may have increased connection usage.

## Resolution
Reduce connection pressure, close stale sessions, and tune the pool if the workload is expected to remain high.

## Escalation
Escalate to the DBA team if the timeouts persist after pool and workload tuning.
