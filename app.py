import os
import streamlit as st
import requests
import json

SYSTEM_PROMPT = """
You are an expert AI career advisor for a specific OPT/STEM OPT international student profile.
The user will paste a job posting. Analyze it against this profile and return a clear structured assessment.

Student profile:
- Visa: F-1, STEM OPT eligible, MS in Data Science at GVSU, graduating December 2026
- Skills: Python, R, SQL, Power BI, ETL pipelines, machine learning, data analytics
- Target cities: Atlanta, Austin, Raleigh-Durham, Washington D.C.
- Target roles: Data Analyst, Data Engineer, Data Scientist
- Experience: 2 years (Graduate Assistant + internship work)
- Sponsorship plan: needs OPT immediately, and H-1B sponsorship within 3 years

Your output MUST use these labeled sections:
1. Fit Score (0-100)
2. Sponsorship Risk
3. Skills Match
4. Red Flags
5. Application Strategy

Use the job posting details to assess:
- whether the role is a strong fit,
- whether the employer likely supports OPT/H-1B,
- missing skills or experience gaps,
- relevant strengths,
- recommended application strategy for OPT timeline, visa strategy, and next steps.
Be honest and concise. If a section is not applicable, say 'Not enough information'. Do not invent details about the employer.
"""


def analyze_job_posting(job_posting: str) -> str:
    api_key = os.environ.get("OPENROUTER_API_KEY", "")
    if not api_key:
        raise ValueError("Missing OPENROUTER_API_KEY environment variable.")

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    body = {
        "model": "meta-llama/llama-3.2-3b-instruct:free",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": job_posting.strip()},
        ],
    }

    resp = requests.post(url, headers=headers, json=body, timeout=60)
    resp.raise_for_status()
    data = resp.json()

    # Safely extract the assistant content
    try:
        return data["choices"][0]["message"]["content"]
    except Exception:
        return json.dumps(data)


def main() -> None:
    st.set_page_config(
        page_title="OPT Job Advisor",
        page_icon="🧭",
        layout="centered",
    )

    st.title("OPT Job Advisor")
    st.markdown(
        "Paste a job posting below and get a personalized assessment for a GVSU MS Data Science student on F-1 STEM OPT."
    )

    st.info(
        "This tool uses a hardcoded profile and does not store your job posting. Set ANTHROPIC_API_KEY in your environment before running."
    )

    job_posting = st.text_area(
        "Job posting text",
        height=320,
        placeholder="Paste the full job description here...",
    )

    if st.button("Analyze Job Posting"):
        if not job_posting.strip():
            st.warning("Please paste a job posting before analyzing.")
            return

        with st.spinner("Analyzing job posting…"):
            try:
                analysis = analyze_job_posting(job_posting)
                st.markdown("## Analysis Result")
                st.markdown(analysis)
            except Exception as exc:
                st.error("Unable to analyze the job posting.")
                st.write(exc)

    st.markdown("---")
    st.markdown(
        "**Profile used for analysis:** F-1 STEM OPT eligible MS Data Science student at GVSU, graduating Dec 2026, with Python, R, SQL, Power BI, ETL, machine learning, data analytics. Target cities: Atlanta, Austin, Raleigh-Durham, Washington D.C. Target roles: Data Analyst, Data Engineer, Data Scientist. Needs OPT now and H-1B sponsorship within 3 years."
    )


if __name__ == "__main__":
    main()
