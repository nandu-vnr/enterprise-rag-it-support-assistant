# Production Deployment Checklist

## Pre-deployment Validation
- Confirm all P1/P2 incidents are triaged.
- Verify database migrations are tested in staging.
- Confirm rollback plan is available and communicated.

## Deployment Steps
1. Notify stakeholders and support on-call.
2. Deploy code to canary or staging first.
3. Monitor key metrics during the rollout.
4. Validate end-to-end functionality before full traffic cutover.

## Post-deployment
- Confirm success criteria with the release owner.
- Log deployment notes and any deviation in the change ticket.
