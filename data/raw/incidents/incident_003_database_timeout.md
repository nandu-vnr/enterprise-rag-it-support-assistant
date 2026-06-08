# Database Connection Timeout

## Overview
Applications are experiencing intermittent database timeouts while connecting to the primary PostgreSQL cluster.

## Symptoms
- Connection timeout errors in application logs
- Reduced throughput and failed API requests
- Database connection pools are saturated

## Troubleshooting Steps
1. Confirm database availability and status.
2. Inspect connection pool usage in the application.
3. Review recent changes to queries or database indexes.
4. Validate network connectivity between application servers and the database.
5. Restart the application connection pool if safe.

## Escalation
Escalate to the DBA team when the issue persists after connection pool tuning and network validation.
