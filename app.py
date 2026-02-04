import streamlit as st

from transformers import (
    generate_action_plan,
    generate_project_blueprint,
    generate_checklist,
    generate_formatted_output
)

from formatter import format_output


# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Unstructure to Structure",
    page_icon="U",
    layout="wide"
)

# --------------------------------------------------
# Style
# --------------------------------------------------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400;9..144,600;9..144,700&display=swap');

:root {
  --ink: #1d1b16;
  --muted: #5b5448;
  --accent: #2e6b5d;
  --accent-dark: #21443d;
  --highlight: #e3b86c;
  --bg-1: #f7f2ea;
  --bg-2: #efe6d6;
  --card: #ffffff;
  --border: rgba(29, 27, 22, 0.12);
  --shadow: 0 18px 40px rgba(29, 27, 22, 0.12);
}

html, body, [class*="css"] {
  font-family: "Fraunces", "Times New Roman", serif;
  color: var(--ink);
}

div[data-testid="stAppViewContainer"] {
  background:
    radial-gradient(900px 420px at 12% 0%, #fff7e9 0%, transparent 60%),
    radial-gradient(920px 480px at 90% 10%, #f4efe4 0%, transparent 55%),
    linear-gradient(180deg, var(--bg-1) 0%, var(--bg-2) 100%);
}

header[data-testid="stHeader"] {
  background: transparent;
}

section[data-testid="stSidebar"] {
  background: linear-gradient(180deg, #f4ede0 0%, #efe5d5 100%);
  border-right: 1px solid rgba(29, 27, 22, 0.08);
}

section[data-testid="stSidebar"] > div:first-child {
  padding-top: 1.6rem;
}

div[data-testid="stSidebarNav"] ul {
  padding-left: 0.5rem;
  padding-right: 0.5rem;
}

div[data-testid="stSidebarNav"] li {
  margin: 0.35rem 0;
}

div[data-testid="stSidebarNav"] a {
  display: block;
  padding: 0.6rem 0.9rem;
  border-radius: 14px;
  background: rgba(255, 255, 255, 0.75);
  border: 1px solid transparent;
  color: var(--ink);
  text-decoration: none;
  font-weight: 600;
  letter-spacing: 0.02em;
  text-transform: capitalize;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}

div[data-testid="stSidebarNav"] a:hover {
  border-color: rgba(46, 107, 93, 0.3);
  background: rgba(255, 255, 255, 0.95);
  transform: translateX(4px);
}

div[data-testid="stSidebarNav"] a[aria-current="page"] {
  background: linear-gradient(120deg, rgba(46, 107, 93, 0.22), rgba(227, 184, 108, 0.2));
  border-color: rgba(46, 107, 93, 0.4);
  color: var(--accent-dark);
  box-shadow: 0 10px 18px rgba(29, 27, 22, 0.12);
}

button[title="Collapse sidebar"],
button[title="Open sidebar"],
div[data-testid="stSidebarCollapsedControl"] button {
  width: 2.6rem;
  height: 2.6rem;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(29, 27, 22, 0.12);
  box-shadow: 0 10px 18px rgba(29, 27, 22, 0.12);
}

button[title="Collapse sidebar"] svg,
button[title="Open sidebar"] svg,
div[data-testid="stSidebarCollapsedControl"] button svg {
  width: 1.4rem;
  height: 1.4rem;
}

div.block-container {
  max-width: 1200px;
  padding-top: 3.5rem;
  padding-bottom: 3rem;
}

h1, h2, h3, h4 {
  letter-spacing: -0.02em;
}

p, label, span, input, textarea {
  font-size: 0.98rem;
  line-height: 1.6;
}

.hero {
  position: relative;
  overflow: hidden;
  background: rgba(255, 255, 255, 0.78);
  border: 1px solid var(--border);
  border-radius: 28px;
  padding: 2.8rem 3rem;
  box-shadow: var(--shadow);
}

.hero::before {
  content: "";
  position: absolute;
  inset: -40%;
  background: radial-gradient(circle at 30% 30%, rgba(227, 184, 108, 0.35), transparent 55%),
              radial-gradient(circle at 70% 60%, rgba(46, 107, 93, 0.25), transparent 50%);
  animation: drift 18s ease-in-out infinite;
}

.hero::after {
  content: "";
  position: absolute;
  width: 220px;
  height: 220px;
  right: -90px;
  top: -90px;
  background: radial-gradient(circle, rgba(46, 107, 93, 0.25) 0%, transparent 65%);
  animation: float 10s ease-in-out infinite;
}

.site-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1.5rem;
  margin-bottom: 1.8rem;
}

.brand {
  font-size: 0.85rem;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  font-weight: 600;
}

.nav-links {
  font-size: 0.75rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
}

.hero-grid {
  position: relative;
  z-index: 1;
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 2.4rem;
  align-items: center;
}

@media (max-width: 900px) {
  .hero-grid {
    grid-template-columns: 1fr;
  }
  .nav-links {
    display: none;
  }
}

.hero-eyebrow {
  text-transform: uppercase;
  letter-spacing: 0.18em;
  font-size: 0.75rem;
  color: var(--muted);
  margin-bottom: 0.6rem;
}

.hero-title {
  font-size: 2.6rem;
  font-weight: 600;
  margin-bottom: 0.8rem;
  line-height: 1.1;
}

.hero-subtitle {
  color: var(--muted);
  font-size: 1.05rem;
}

.hero-actions {
  display: flex;
  gap: 1rem;
  margin-top: 1.6rem;
  flex-wrap: wrap;
}

.hero-pill {
  display: inline-flex;
  align-items: center;
  padding: 0.5rem 1rem;
  border-radius: 999px;
  background: rgba(46, 107, 93, 0.12);
  border: 1px solid rgba(46, 107, 93, 0.2);
  color: var(--accent-dark);
  font-size: 0.85rem;
  letter-spacing: 0.04em;
}

.hero-preview {
  position: relative;
  background: #fffdf8;
  border-radius: 22px;
  border: 1px solid var(--border);
  padding: 1.6rem 1.8rem;
  box-shadow: 0 16px 34px rgba(29, 27, 22, 0.12);
  overflow: hidden;
}

.hero-preview::before {
  content: "";
  position: absolute;
  inset: 0;
  border-top: 3px solid transparent;
  border-image: linear-gradient(90deg, transparent, var(--highlight), transparent) 1;
  animation: scan 6s linear infinite;
}

.preview-title {
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  color: var(--muted);
  margin-bottom: 1rem;
}

.preview-list {
  display: grid;
  gap: 0.75rem;
  list-style: none;
  padding: 0;
  margin: 0;
}

.preview-line {
  display: grid;
  grid-template-columns: 80px 1fr;
  gap: 0.8rem;
  font-size: 0.95rem;
}

.preview-line span {
  text-transform: uppercase;
  letter-spacing: 0.14em;
  color: var(--accent);
  font-size: 0.7rem;
}

.hero-metrics {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 1rem;
  margin-top: 1.8rem;
}

.metric {
  background: rgba(255, 255, 255, 0.7);
  border-radius: 16px;
  border: 1px solid var(--border);
  padding: 0.9rem 1rem;
}

.metric-value {
  font-size: 1.4rem;
  font-weight: 600;
}

.metric-label {
  font-size: 0.75rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
}

.section-divider {
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(29, 27, 22, 0.2), transparent);
  margin: 2.2rem 0;
}

.panel-title {
  font-size: 1.15rem;
  font-weight: 600;
  margin-bottom: 0.7rem;
}

.section-title {
  font-size: 1.4rem;
  font-weight: 600;
  margin-bottom: 0.4rem;
}

.section-subtitle {
  color: var(--muted);
  font-size: 0.95rem;
}

.empty-state {
  border: 1px dashed rgba(29, 27, 22, 0.2);
  border-radius: 16px;
  padding: 1.6rem;
  color: var(--muted);
  background: rgba(255, 255, 255, 0.65);
}

div[data-testid="stHorizontalBlock"] > div {
  position: relative;
  overflow: hidden;
  background: rgba(255, 255, 255, 0.86);
  border: 1px solid var(--border);
  border-radius: 24px;
  padding: 1.9rem 2rem 2.1rem;
  box-shadow: var(--shadow);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  display: flex;
  flex-direction: column;
  min-height: 560px;
}

div[data-testid="stHorizontalBlock"] > div::before {
  content: "";
  position: absolute;
  inset: 0;
  border-top: 3px solid transparent;
  border-image: linear-gradient(90deg, transparent, var(--accent), transparent) 1;
  animation: scan 7s linear infinite;
  opacity: 0.6;
}

div[data-testid="stHorizontalBlock"] > div:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 38px rgba(29, 27, 22, 0.18);
}

div[data-testid="stTextArea"] textarea {
  background: #fbf7ef;
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 0.9rem 1rem;
  font-size: 0.98rem;
}

div[data-testid="stTextArea"] textarea[disabled] {
  color: var(--ink);
}

div[data-testid="stCodeBlock"] {
  flex: 1;
}

div[data-testid="stCodeBlock"] pre {
  background: #0f172a;
  color: #e2e8f0;
  border-radius: 16px;
  padding: 1.1rem 1.2rem;
  min-height: 460px;
  max-height: 640px;
  overflow: auto;
  border: 1px solid rgba(226, 232, 240, 0.1);
  box-shadow: inset 0 0 0 1px rgba(15, 23, 42, 0.15);
}

div[data-testid="stCodeBlock"] code {
  font-family: "JetBrains Mono", "Fira Code", "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
  font-size: 0.88rem;
  line-height: 1.6;
}

.hljs-attr {
  color: #9cdcfe;
}

.hljs-string {
  color: #ce9178;
}

.hljs-number {
  color: #b5cea8;
}

.hljs-literal {
  color: #569cd6;
}

.hljs-punctuation {
  color: #d4d4d4;
}

.hljs-comment {
  color: #6a9955;
}

@media (max-width: 900px) {
  div[data-testid="stHorizontalBlock"] > div {
    min-height: auto;
  }
  div[data-testid="stCodeBlock"] pre {
    min-height: 360px;
    max-height: 560px;
  }
}

div[data-testid="stTextArea"] textarea:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px rgba(46, 107, 93, 0.18);
}

div[data-baseweb="select"] > div {
  background: #fbf7ef;
  border: 1px solid var(--border);
  border-radius: 14px;
  box-shadow: none;
}

div[data-baseweb="select"] > div:focus-within {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px rgba(46, 107, 93, 0.18);
}

div[data-testid="stButton"] > button {
  width: 100%;
  background: linear-gradient(120deg, var(--accent) 0%, var(--accent-dark) 50%, var(--accent) 100%);
  background-size: 200% 100%;
  color: #ffffff;
  border: none;
  border-radius: 999px;
  padding: 0.75rem 1.4rem;
  font-weight: 600;
  letter-spacing: 0.02em;
  box-shadow: 0 14px 26px rgba(33, 68, 61, 0.25);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  animation: sheen 8s linear infinite;
}

div[data-testid="stButton"] > button:hover {
  transform: translateY(-2px);
  box-shadow: 0 18px 32px rgba(33, 68, 61, 0.28);
}

div[data-testid="stButton"] > button:active {
  transform: translateY(0);
  box-shadow: 0 10px 22px rgba(33, 68, 61, 0.2);
}

div[data-testid="stAlert"] {
  border-radius: 14px;
}

.footer {
  text-align: center;
  color: var(--muted);
  font-size: 0.85rem;
  margin-top: 2.4rem;
}

@keyframes drift {
  0% {
    transform: translate3d(0, 0, 0);
  }
  50% {
    transform: translate3d(4%, -3%, 0);
  }
  100% {
    transform: translate3d(0, 0, 0);
  }
}

@keyframes float {
  0% {
    transform: translate3d(0, 0, 0);
  }
  50% {
    transform: translate3d(-10px, 12px, 0);
  }
  100% {
    transform: translate3d(0, 0, 0);
  }
}

@keyframes scan {
  0% {
    border-image-source: linear-gradient(90deg, transparent, var(--highlight), transparent);
  }
  50% {
    border-image-source: linear-gradient(90deg, transparent, var(--accent), transparent);
  }
  100% {
    border-image-source: linear-gradient(90deg, transparent, var(--highlight), transparent);
  }
}

@keyframes sheen {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}
</style>
""",
    unsafe_allow_html=True
)

# --------------------------------------------------
# Hero
# --------------------------------------------------
st.markdown(
    """
<div class="site-nav">
  <div class="brand">Unstructure to Structure</div>
  <div class="nav-links">Action plans · Blueprints · Checklists · Formats</div>
</div>
<div class="hero">
  <div class="hero-grid">
    <div>
      <div class="hero-eyebrow">AI structure studio</div>
      <div class="hero-title">Give your notes a clean, confident shape</div>
      <div class="hero-subtitle">
        Transform raw thoughts into actionable steps, scoped projects, and structured outputs that feel ready to ship.
      </div>
      <div class="hero-actions">
        <div class="hero-pill">Powered by Groq LLMs</div>
        <div class="hero-pill">Precision formatting</div>
      </div>
      <div class="hero-metrics">
        <div class="metric">
          <div class="metric-value">4</div>
          <div class="metric-label">Output types</div>
        </div>
        <div class="metric">
          <div class="metric-value">1</div>
          <div class="metric-label">Unified flow</div>
        </div>
        <div class="metric">
          <div class="metric-value">0</div>
          <div class="metric-label">Manual cleanup</div>
        </div>
      </div>
    </div>
    <div class="hero-preview">
      <div class="preview-title">Sample structured output</div>
      <div class="preview-list">
        <div class="preview-line"><span>Goal</span><div>Launch the AI utility and publish the repo.</div></div>
        <div class="preview-line"><span>Steps</span><div>Define scope, design UI, implement flows, deploy.</div></div>
        <div class="preview-line"><span>Deliver</span><div>Live app, README, demo walkthrough.</div></div>
        <div class="preview-line"><span>Time</span><div>5 to 7 days, staggered milestones.</div></div>
      </div>
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True
)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# --------------------------------------------------
# Main Layout
# --------------------------------------------------
left_col, right_col = st.columns([1.05, 0.95], gap="large")

TRANSFORM_OPTIONS = {
    "Messy text to action plan": "action_plan",
    "Problem statement to project blueprint": "project_blueprint",
    "Requirements to checklist": "checklist",
    "Text to multiple formats": "multi_format"
}

run_clicked = False
selected_key = "action_plan"
output_format = "JSON"

with left_col:
    st.markdown(
        """
<div class="section-title">Workspace</div>
<div class="section-subtitle">Choose a transformation, add your text, and review the structured result.</div>
""",
        unsafe_allow_html=True
    )
    st.markdown("<div style='height: 0.8rem;'></div>", unsafe_allow_html=True)
    st.markdown('<div class="panel-title">Input</div>', unsafe_allow_html=True)

    selected_label = st.selectbox(
        "Choose transformation",
        list(TRANSFORM_OPTIONS.keys())
    )
    selected_key = TRANSFORM_OPTIONS[selected_label]

    user_input = st.text_area(
        "Paste your text here",
        height=220,
        placeholder="Paste messy notes, requirements, or problem statements.",
        label_visibility="collapsed"
    )

    if selected_key == "multi_format":
        output_format = st.selectbox(
            "Output format",
            ["JSON", "Bullet Points", "Markdown"]
        )

    run_clicked = st.button("Transform", use_container_width=True)

formatted = None
error_message = None
exception = None

if run_clicked:
    if not user_input.strip():
        error_message = "Please enter some text to transform."
    else:
        with st.spinner("Structuring your content..."):
            try:
                if selected_key == "action_plan":
                    raw_output = generate_action_plan(user_input)
                    formatted = format_output(raw_output, "json")

                elif selected_key == "project_blueprint":
                    raw_output = generate_project_blueprint(user_input)
                    formatted = format_output(raw_output, "json")

                elif selected_key == "checklist":
                    raw_output = generate_checklist(user_input)
                    formatted = format_output(raw_output, "json")

                elif selected_key == "multi_format":
                    raw_output = generate_formatted_output(user_input, output_format)
                    formatted = format_output(raw_output, output_format)

            except Exception as e:
                exception = e

with left_col:
    if error_message:
        st.warning(error_message)
    if exception:
        st.error("Something went wrong while processing your request.")
        st.exception(exception)
    if formatted:
        st.success("Transformation complete.")

with right_col:
    st.markdown('<div class="panel-title">Structured Output</div>', unsafe_allow_html=True)
    if formatted:
        is_json_output = selected_key != "multi_format" or output_format == "JSON"
        if is_json_output:
            st.code(formatted, language="json")
        else:
            st.code(formatted, language="markdown")
    else:
        st.markdown(
            '<div class="empty-state">Your structured output will appear here after you run a transformation.</div>',
            unsafe_allow_html=True
        )

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown(
    '<div class="footer">Built with Streamlit and Groq LLMs. Unstructure to Structure Utility.</div>',
    unsafe_allow_html=True
)
