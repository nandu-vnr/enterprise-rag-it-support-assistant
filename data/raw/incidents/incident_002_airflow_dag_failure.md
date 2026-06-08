# Airflow DAG Failure After Schema Change

## Overview
A daily ETL DAG failed following a schema change in the source data warehouse. Downstream tasks fail with column mismatch and data validation errors.

## Symptoms
- Airflow task failures in the transform step
- Error messages reference missing or unexpected columns
- New nullable column added to the source schema

## Troubleshooting Steps
1. Review the DAG logs and identify the failing task.
2. Compare the source table schema to the ETL model and dbt models.
3. Run schema validation and Great Expectations checks on the affected dataset.
4. Update the dbt model or transform code to account for the new field.
5. Execute a DAG backfill after validation passes.

## Escalation
For P1 issues, notify the data platform on-call and pause the DAG until the schema drift is resolved.
