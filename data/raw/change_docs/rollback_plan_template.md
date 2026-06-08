# Rollback Plan Template

## Rollback Trigger
A rollback should occur when the deployment causes severe production degradation or a P1 incident.

## Rollback Steps
1. Stop the failed deployment and revert to the last known good version.
2. Reconfigure any feature flags or routing changes.
3. Verify system health after rollback.
4. Notify stakeholders and document the reason for rollback.

## Communication
- Announce the rollback in the incident channel.
- Update the ticket with the timeline and next action.
