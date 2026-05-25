# OPT Job Advisor

## What This Is

OPT Job Advisor is a Streamlit-powered AI tool built tonight to analyze job postings against a hardcoded F-1 STEM OPT student profile. It evaluates fit, sponsorship risk, skills match, red flags, and application strategy for a Michigan-based MS Data Science student aiming for U.S. data roles.

## Live Demo

https://opt-job-advisor-ojkmzderuszyv8e6wuculh.streamlit.app/

## The Problem It Solves

International students on F-1 OPT waste hours applying to jobs that will never sponsor them. This tool gives an honest, personalized assessment in seconds so a job seeker can decide quickly whether a role is worth pursuing.

## System Prompt Design

The app embeds the student profile directly into the system prompt instead of building a form. This keeps the UI simple, removes form state complexity, and ensures every request is analyzed against the same exact profile.

The prompt is intentionally hardcoded with the student’s visa status, academic program, timeline, target cities, target roles, skills, experience, and sponsorship plan.

### Actual System Prompt

```
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
```

## Prompt Engineering Decisions

- Structured output with 5 mandatory sections ensures consistent responses and easy readout in Streamlit.
- The model is explicitly told to say "Not enough information" rather than guess when details are missing.
- The prompt prioritizes honesty over encouragement, so assessments are realistic and not overly positive.
- The app uses low temperature / deterministic settings through the model choice and prompt instructions to keep output stable.

## Grounding Strategy

The model is grounded with a specific profile context that includes:
- visa status: F-1, STEM OPT eligible
- degree and university: MS in Data Science at GVSU
- graduation timeline: December 2026
- skills: Python, R, SQL, Power BI, ETL pipelines, machine learning, data analytics
- target cities: Atlanta, Austin, Raleigh-Durham, Washington D.C.
- target roles: Data Analyst, Data Engineer, Data Scientist
- experience: 2 years of graduate assistant and internship work
- sponsorship plan: needs OPT now and H-1B within 3 years

## Build Log

- Started with Anthropic API using the deprecated completions endpoint.
- Fixed to Anthropic messages API when the legacy API path failed.
- Switched to Gemini for free-tier access, then halted due to quota issues.
- Switched to OpenRouter for better flexibility, then encountered rate limits and model availability issues.
- Landed on Groq with `llama-3.3-70b-versatile`, which was stable and free for this prototype.

Each platform switch was a deliberate decision based on testing availability, API stability, and deployment speed.

## Evaluation

### Test case 1: Strong fit role
- Expected: high fit score, low sponsorship risk, strong skills overlap, few red flags, optimistic application strategy.
- Actual: Fit Score 90/100. Sponsorship Risk: Low — employer explicitly welcomes OPT and sponsors H-1B. Skills Match: 80% — Python, SQL, Power BI confirmed. Red Flags: None. Strategy: Apply immediately, discuss OPT eligibility in interview.

### Test case 2: Weak fit role
- Expected: low fit score, high sponsorship risk, poor skills match, clear red flags, recommendation to skip or deprioritize.
- Actual: Fit Score: 0 — role is Marketing Coordinator, no overlap with target roles. Sponsorship Risk: High — employer explicitly cannot sponsor. Skills Match: None — Adobe Creative Suite and copywriting don't match profile. Red Flags: No sponsorship, wrong field, wrong city (Seattle). Strategy: Not recommended.

### Test case 3: Ambiguous role
- Expected: moderate fit score, conditional sponsorship risk, mixed skills match, note missing sponsorship information, and cautious strategy.
- Actual: Fit Score: 80 — Data Scientist role matches target. Sponsorship Risk: Not enough information — no visa policy mentioned, model correctly flagged uncertainty. Skills Match: 90% — Python, ML, analytics confirmed; Power BI covers visualization gap. Red Flags: None. Strategy: Apply but research sponsorship policy first, ask HR directly.

### What the Evaluation Shows
The model correctly identified a strong fit, correctly rejected a completely mismatched role, and appropriately flagged uncertainty on an ambiguous posting — exactly the behavior the system prompt was designed to produce.

## Where It Works and Where It Breaks

### Where It Works
- Good for quickly filtering roles that match the fixed profile.
- Useful for seeing whether a posting appears likely to support OPT/H-1B.
- Effective for jobs that list clear requirements and sponsorship or location details.

### Where It Breaks
- Limited by model errors or hallucinations when the job posting is poorly formatted.
- Cannot adapt to different student profiles without code changes.
- May misinterpret vague postings or fail when sponsor language is not explicit.

## Tech Stack

- Python
- Streamlit
- Groq API
- `llama-3.3-70b-versatile`
- Deployed on Streamlit Community Cloud
- Version controlled on GitHub
