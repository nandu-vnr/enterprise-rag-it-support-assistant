# Airflow Failure Runbook

## Schema Drift
Use this runbook when an Airflow DAG fails after a schema change.

### Step 1: Review the Failure
Inspect the failed task logs for schema mismatch or column not found errors.

### Step 2: Validate Source Schema
Compare the source table schema to the ETL and dbt model definitions.

### Step 3: Run Data Quality Checks
Execute Great Expectations or other validation tests on the affected dataset.

### Step 4: Adjust the DAG
Update the DAG or dbt model to support the schema change and rerun the pipeline.

### Next Action
If this is a P1 incident, notify the data platform team immediately and delay dependent jobs until the fix is validated.
