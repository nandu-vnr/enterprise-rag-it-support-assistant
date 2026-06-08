import json
import os
import urllib.request
import urllib.error

import streamlit as st


try:
    API_URL = st.secrets.get("api_url", None)
except Exception:
    API_URL = None

API_URL = os.getenv("API_URL", API_URL or "http://localhost:8000/support/ask")

st.set_page_config(
    page_title="Enterprise RAG IT Support Assistant",
    page_icon="🛠️",
    layout="centered",
)

st.title("Enterprise RAG IT Support Assistant")
st.write(
    "Ask the assistant about incident resolution, troubleshooting, runbooks, and escalation guidance."
)

with st.form("support_form"):
    ticket_id = st.text_input("Ticket ID", "INC-1002")
    priority = st.selectbox("Priority", ["P1", "P2", "P3"], index=0)
    category = st.text_input("Category", "Data Engineering")
    question = st.text_area(
        "Issue description",
        "Airflow DAG failed after schema change. What should I do?",
        height=180,
    )
    submitted = st.form_submit_button("Ask assistant")

if submitted:
    if not ticket_id or not question:
        st.error("Ticket ID and issue description are required.")
    else:
        payload = {
            "ticket_id": ticket_id,
            "priority": priority,
            "category": category,
            "question": question,
        }

        request = urllib.request.Request(
            API_URL,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        try:
            with urllib.request.urlopen(request, timeout=30) as res:
                response_data = json.loads(res.read().decode("utf-8"))
                st.success("Answer generated successfully.")
                st.subheader("Answer")
                st.write(response_data.get("answer", "No answer returned."))

                st.markdown(
                    f"**Confidence:** {response_data.get('confidence', 'unknown')}"
                )
                st.markdown(
                    f"**Escalation Required:** {response_data.get('escalation_required', False)}"
                )
                next_action = response_data.get("next_action")
                if next_action:
                    st.markdown(f"**Next action:** {next_action}")

                sources = response_data.get("sources", [])
                if sources:
                    st.subheader("Sources")
                    for source in sources:
                        st.write(
                            f"• {source.get('file')}"
                            f"{': ' + source.get('section') if source.get('section') else ''}"
                            f" (score={source.get('score', 0):.2f})"
                        )
        except urllib.error.HTTPError as exc:
            try:
                error_body = json.loads(exc.read().decode("utf-8"))
                st.error(f"Support API error: {error_body.get('detail', exc.reason)}")
            except json.JSONDecodeError:
                st.error(f"Unable to call the support API: {exc}")
        except Exception as exc:
            st.error(f"Unable to call the support API: {exc}")
