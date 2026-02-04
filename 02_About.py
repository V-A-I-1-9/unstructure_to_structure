import streamlit as st


# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="About | Unstruct2Struct",
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

.section-divider {
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(29, 27, 22, 0.2), transparent);
  margin: 2.2rem 0;
}

.about-hero {
  position: relative;
  overflow: hidden;
  background: rgba(255, 255, 255, 0.8);
  border: 1px solid var(--border);
  border-radius: 28px;
  padding: 2.6rem 3rem;
  box-shadow: var(--shadow);
}

.about-hero::before {
  content: "";
  position: absolute;
  inset: -40%;
  background: radial-gradient(circle at 30% 30%, rgba(227, 184, 108, 0.35), transparent 55%),
              radial-gradient(circle at 70% 60%, rgba(46, 107, 93, 0.25), transparent 50%);
  animation: drift 18s ease-in-out infinite;
}

.about-hero-grid {
  position: relative;
  z-index: 1;
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  gap: 2.2rem;
  align-items: center;
}

@media (max-width: 900px) {
  .about-hero-grid {
    grid-template-columns: 1fr;
  }
}

.about-kicker {
  text-transform: uppercase;
  letter-spacing: 0.2em;
  font-size: 0.75rem;
  color: var(--muted);
  margin-bottom: 0.6rem;
}

.about-title {
  font-size: 2.6rem;
  font-weight: 600;
  margin-bottom: 0.8rem;
  line-height: 1.1;
}

.about-subtitle {
  color: var(--muted);
  font-size: 1.05rem;
}

.about-tags {
  display: flex;
  gap: 0.8rem;
  flex-wrap: wrap;
  margin-top: 1.6rem;
}

.about-tag {
  display: inline-flex;
  align-items: center;
  padding: 0.45rem 0.95rem;
  border-radius: 999px;
  background: rgba(46, 107, 93, 0.12);
  border: 1px solid rgba(46, 107, 93, 0.2);
  color: var(--accent-dark);
  font-size: 0.82rem;
  letter-spacing: 0.04em;
}

.about-card {
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid var(--border);
  border-radius: 22px;
  padding: 1.6rem 1.8rem;
  box-shadow: var(--shadow);
}

.about-card h3 {
  font-size: 1.2rem;
  margin-bottom: 0.6rem;
}

.about-card p {
  margin-bottom: 0.75rem;
}

.about-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: grid;
  gap: 0.6rem;
  color: var(--muted);
}

.about-list li {
  padding-left: 1.1rem;
  position: relative;
}

.about-list li::before {
  content: "";
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--accent);
  position: absolute;
  left: 0;
  top: 0.6rem;
}

.feature-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.4rem;
}

.feature-card {
  background: #fffdf8;
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 1.4rem 1.6rem;
  box-shadow: var(--shadow);
  display: grid;
  gap: 0.85rem;
}

.feature-title {
  font-size: 1.05rem;
  font-weight: 600;
}

.example {
  background: #f6efe2;
  border-radius: 14px;
  padding: 0.85rem 0.95rem;
  font-size: 0.9rem;
  color: #3d3428;
}

.example-label {
  text-transform: uppercase;
  letter-spacing: 0.18em;
  font-size: 0.65rem;
  color: var(--muted);
  margin-bottom: 0.35rem;
}

.example-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: grid;
  gap: 0.35rem;
}

.steps {
  display: grid;
  gap: 0.5rem;
  margin: 0;
  padding: 0;
  list-style: none;
}

.steps li {
  display: grid;
  grid-template-columns: 26px 1fr;
  gap: 0.6rem;
  align-items: start;
}

.step-index {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  background: rgba(46, 107, 93, 0.15);
  color: var(--accent-dark);
  font-size: 0.8rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  justify-content: center;
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
</style>
""",
    unsafe_allow_html=True
)

# --------------------------------------------------
# Hero
# --------------------------------------------------
st.markdown(
    """
<div class="about-hero">
  <div class="about-hero-grid">
    <div>
      <div class="about-kicker">About</div>
      <div class="about-title">Unstruct2Struct</div>
      <div class="about-subtitle">
        Unstruct2Struct is an AI-powered utility that turns messy, unclear text into clean and structured output.
        It helps organize scattered ideas into something you can actually work on.
      </div>
      <div class="about-tags">
        <div class="about-tag">Thinking tool</div>
        <div class="about-tag">Planning assistant</div>
        <div class="about-tag">Structured outputs</div>
      </div>
    </div>
    <div class="about-card">
      <h3>What it is</h3>
      <p>Many times we have ideas, notes, or instructions in our head, but they are not clear or organized.</p>
      <p>This app helps you organize your thoughts and convert them into something you can actually work on.</p>
      <p>It is not a chatbot. It is a thinking and planning tool.</p>
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True
)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# --------------------------------------------------
# Why and When
# --------------------------------------------------
left_col, right_col = st.columns(2, gap="large")

with left_col:
    st.markdown(
        """
<div class="about-card">
  <h3>Why was this app built?</h3>
  <ul class="about-list">
    <li>I know what I want to do, but I do not know where to start.</li>
    <li>The instructions are confusing.</li>
    <li>I have requirements, but no clear checklist.</li>
    <li>My idea is good, but it is not structured.</li>
  </ul>
  <p>Unstruct2Struct solves this by converting confusion into clarity.</p>
</div>
""",
        unsafe_allow_html=True
    )

with right_col:
    st.markdown(
        """
<div class="about-card">
  <h3>When should you use this app?</h3>
  <ul class="about-list">
    <li>You feel confused about what to do next.</li>
    <li>You have messy notes or ideas.</li>
    <li>You want to plan a project.</li>
    <li>You want to prepare for hackathons or assignments.</li>
    <li>You want clarity before starting work.</li>
  </ul>
</div>
""",
        unsafe_allow_html=True
    )

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# --------------------------------------------------
# Capabilities
# --------------------------------------------------
st.markdown(
    """
<div class="about-card" style="margin-bottom: 1.4rem;">
  <h3>What can this app do?</h3>
  <p>Unstruct2Struct offers four core transformations that keep your output clean, actionable, and ready to use.</p>
</div>
""",
    unsafe_allow_html=True
)

st.markdown(
    """
<div class="feature-grid">
  <div class="feature-card">
    <div class="feature-title">Messy Text to Action Plan</div>
    <div class="example">
      <div class="example-label">Example input</div>
      Hackathon project using AI, need to code, deploy, submit GitHub.
    </div>
    <div class="example">
      <div class="example-label">Output</div>
      <ul class="example-list">
        <li>Clear goal</li>
        <li>Step-by-step plan</li>
        <li>Deliverables</li>
        <li>Time estimate</li>
      </ul>
    </div>
  </div>
  <div class="feature-card">
    <div class="feature-title">Problem Statement to Project Blueprint</div>
    <div class="example">
      <div class="example-label">Example input</div>
      Build something useful using GenAI.
    </div>
    <div class="example">
      <div class="example-label">Output</div>
      <ul class="example-list">
        <li>Problem summary</li>
        <li>Target users</li>
        <li>Core features</li>
        <li>Tech stack</li>
        <li>MVP scope</li>
      </ul>
    </div>
  </div>
  <div class="feature-card">
    <div class="feature-title">Requirements to Checklist</div>
    <div class="example">
      <div class="example-label">Example input</div>
      Frontend, backend, deployment, README.
    </div>
    <div class="example">
      <div class="example-label">Output</div>
      <ul class="example-list">
        <li>Clean checklist</li>
        <li>Easy to track progress</li>
        <li>No missed requirements</li>
      </ul>
    </div>
  </div>
  <div class="feature-card">
    <div class="feature-title">Text to Multiple Formats</div>
    <div class="example">
      <div class="example-label">Output formats</div>
      <ul class="example-list">
        <li>JSON</li>
        <li>Bullet points</li>
        <li>Markdown</li>
      </ul>
    </div>
    <div class="example">
      <div class="example-label">Use cases</div>
      Useful for documentation, reports, and submissions.
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True
)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# --------------------------------------------------
# Build and AI Concepts
# --------------------------------------------------
left_col, right_col = st.columns(2, gap="large")

with left_col:
    st.markdown(
        """
<div class="about-card">
  <h3>How is this app built?</h3>
  <ul class="about-list">
    <li>Python</li>
    <li>Streamlit for the user interface</li>
    <li>Groq LLM API for AI reasoning</li>
    <li>Prompt engineering to control output</li>
    <li>Structured JSON outputs for reliability</li>
  </ul>
  <p>The AI is used with fixed rules, so the output is predictable, clean, and easy to understand.</p>
</div>
""",
        unsafe_allow_html=True
    )

with right_col:
    st.markdown(
        """
<div class="about-card">
  <h3>What AI concepts does it use?</h3>
  <ul class="about-list">
    <li>Prompt engineering</li>
    <li>Few-shot learning</li>
    <li>Deterministic AI output</li>
    <li>Text structuring using LLMs</li>
    <li>AI safety through formatting and normalization</li>
  </ul>
</div>
""",
        unsafe_allow_html=True
    )

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# --------------------------------------------------
# How to Use
# --------------------------------------------------
st.markdown(
    """
<div class="about-card">
  <h3>How should you use this app?</h3>
  <ul class="steps">
    <li><span class="step-index">1</span><div>Paste your text or idea.</div></li>
    <li><span class="step-index">2</span><div>Select what you want to generate.</div></li>
    <li><span class="step-index">3</span><div>Click Transform.</div></li>
    <li><span class="step-index">4</span><div>Use the structured output to take action.</div></li>
  </ul>
</div>
""",
    unsafe_allow_html=True
)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# --------------------------------------------------
# Final Note
# --------------------------------------------------
st.markdown(
    """
<div class="about-card">
  <h3>Final note</h3>
  <p>Unstruct2Struct helps you think clearly before you act. It is built to save time, reduce confusion, and improve productivity.</p>
</div>
""",
    unsafe_allow_html=True
)

st.markdown(
    '<div class="footer">Built with Streamlit and Groq LLMs. Unstruct2Struct Utility.</div>',
    unsafe_allow_html=True
)
