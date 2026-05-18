# OPT Job Advisor Roadmap

## 1. Project Context

This project is an AI-powered job advisor for a specific international student profile: F-1 visa holder on STEM OPT, earning an MS in Data Science from GVSU, graduating December 2026. The application must analyze a pasted job posting and return a structured fit assessment based on:
- visa and work authorization needs,
- sponsorship risk,
- skills match,
- target cities,
- target roles,
- experience level,
- application strategy.

The app will be a simple, public web app with no login required. The only input is the job posting text.

## 2. Core Strategy

### 2.1 User experience
- Single-page app with a clean input box for pasting job postings.
- One action button: Analyze Job Posting.
- Clear structured output with sections for fit, sponsorship risk, strengths, weaknesses, and recommended next steps.
- No profile form, since the profile is hardcoded into the system prompt.

### 2.2 AI prompt and system design
- Use a strong system prompt that embeds the fixed profile and agent role.
- Ground the model with explicit profile context and rubric priorities.
- Craft a user prompt that asks for:
  - role fit score,
  - visa/sponsorship risk,
  - top matched skills,
  - missing skills or red flags,
  - application strategy tailored to OPT and H-1B timelines.
- Ensure output is structured and consistent, e.g. JSON-like or clearly labeled sections.

### 2.3 Grounding with context
- Hardcode the student profile directly into the prompt.
- Include relevant domain context: STEM OPT timing, target regions, target job titles.
- If applicable, include a short explanation of how job posts suggest sponsorship or remote eligibility.

## 3. Toolchain

### 3.1 Framework and deployment
- Use Streamlit for the web UI and quick public deployment.
- Host publicly via Streamlit Community Cloud or Streamlit Deployment.
- Alternative deployment option: Vercel if using a static frontend + API backend, but Streamlit is preferred for speed.

### 3.2 Model and APIs
- Use OpenAI-compatible generative model (GPT-4-style or best available API in the environment).
- If local/OpenAI access is unavailable, use a Streamlit-compatible model provider or mock the response structure in development.

### 3.3 Code and version control
- Use Git for commit history.
- Push code to GitHub with descriptive commits for:
  - app setup,
  - prompt engineering,
  - UI polish,
  - deployment configuration,
  - evaluation/iteration.
- Keep the repository clean and documented.

## 4. Build Plan

### Phase 1: Initialization
- Create a Streamlit app scaffold.
- Add required dependencies, including `streamlit` and the OpenAI client.
- Initialize Git if needed and make the first commit.

### Phase 2: System prompt and app logic
- Design the system prompt with the fixed profile.
- Build the prompt assembly logic.
- Add a function that sends the job posting to the model and returns structured results.

### Phase 3: UI and output formatting
- Build the Streamlit UI: textarea input, Analyze button, result display.
- Format results with headings and bullet sections.
- Add a sample job posting or instructions.

### Phase 4: Iteration and polish
- Test with sample job postings across Data Analyst / Data Engineer / Data Scientist roles.
- Refine the prompt to improve sponsor risk assessment and fit accuracy.
- Adjust output structure for clarity and honesty.

### Phase 5: Deployment and documentation
- Deploy publicly on Streamlit Cloud.
- Add `README.md` content describing the app, usage, prompt design, and deployment link.
- Document build choices and evaluation notes.

## 5. Success Metrics

### Functional success
- Publicly deployed and accessible with a stable link.
- User can paste a job posting and receive a response immediately.
- Response includes structured sections for:
  - fit assessment,
  - sponsorship risk,
  - skills match,
  - application strategy.

### Course rubric fit
- Public deployment: app is live with a shareable URL.
- Deliberate prompt engineering: system prompt includes explicit profile and analysis criteria.
- System prompt design: hardcoded profile and advisor instructions are central to behavior.
- Grounding with context: profile details are fixed and used to guide model responses.
- Code on GitHub: repository has app code and commit history.
- Build log / README: documented process and usage instructions.
- Originality: tailored advisor for OPT/STEM OPT international student job search in data roles.
- Intellectual ownership: design, prompts, and evaluation are directly owned by the student.
- Iteration and evaluation: prompt refinement and result testing will be logged.

### Quality metrics
- Output is concise, honest, and actionable.
- Sponsor risk is explicitly stated, not just implied.
- Recommendations are practical for OPT and H-1B strategy.
- Role fit aligns with job requirements and student strengths.

## 6. Immediate next step
- Build the Streamlit app and commit the initial working prototype.
- Use the hardcoded student profile inside the model prompt.
- Validate with real or sample job postings across target cities and roles.
