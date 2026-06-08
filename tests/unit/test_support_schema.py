from src.schemas.answer_schema import SourceReference, SupportAnswer


def test_support_answer_schema_validates_sources_and_confidence():
    answer = SupportAnswer(
        answer="Validate schema drift and rerun the DAG.",
        confidence="high",
        sources=[SourceReference(file="airflow_failure_runbook.md", section="Schema Drift", score=0.92)],
        next_action="Escalate to Data Platform on-call.",
        escalation_required=True,
    )

    assert answer.confidence == "high"
    assert answer.escalation_required is True
    assert answer.sources[0].file == "airflow_failure_runbook.md"
