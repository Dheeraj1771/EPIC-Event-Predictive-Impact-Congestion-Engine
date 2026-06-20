import streamlit as st

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="E.P.I.C. System | Home",
    page_icon="🚨",
    layout="wide"
)

# 2. CSS STYLING (Theme-Adaptive & Equal Height Fix)
st.markdown("""
    <style>
    /* Gradient text for the main title that adapts to Light & Dark mode */
    .title-gradient {
        text-align: center;
        font-size: 4.5rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #FF4B4B, #FF904B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
        padding-bottom: 0;
    }
    .subtitle {
        text-align: center;
        font-size: 1.5rem;
        font-weight: 600;
        color: gray;
        margin-top: -10px;
    }
    .mission-statement {
        text-align: center;
        font-size: 1.1rem;
        color: gray;
        max-width: 800px;
        margin: 20px auto 40px auto;
        line-height: 1.6;
    }
    
    /* CSS Grid to force Equal Height Cards */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        margin-bottom: 30px;
    }
    @media (max-width: 800px) {
        .grid-container {
            grid-template-columns: 1fr; /* Stacks on mobile automatically */
        }
    }
    .grid-card {
        border: 1px solid rgba(150, 150, 150, 0.3); /* Neutral border for Light/Dark mode */
        border-radius: 10px;
        padding: 24px;
        background-color: transparent;
        display: flex;
        flex-direction: column;
        height: 100%; /* Forces equal height */
    }
    .grid-card h3 {
        margin-top: 0;
        margin-bottom: 12px;
        font-size: 1.3rem;
    }
    .grid-card p {
        color: gray;
        margin: 0;
        line-height: 1.6;
        flex-grow: 1; /* Pushes text evenly */
    }
    </style>
""", unsafe_allow_html=True)

# 3. HERO SECTION
st.markdown("<h1 class='title-gradient'>E.P.I.C. Command</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Event Predictive Impact & Congestion Engine</div>", unsafe_allow_html=True)
st.markdown("""
    <div class='mission-statement'>
        A proactive, AI-driven traffic command suite designed exclusively for the <b>Bengaluru Traffic Police</b>. 
        Transitioning city infrastructure from experience-driven guesswork to mathematical resource deployment.
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 4. VALUE PROPOSITION CARDS (Perfectly Aligned Custom Grid)
st.markdown("### ⚙️ Core System Capabilities")
st.write("E.P.I.C. analyzes historical traffic breakdowns to forecast future gridlocks.")
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
    <div class="grid-container">
        <div class="grid-card">
            <h3>🧠 Predictive AI</h3>
            <p>Using Machine Learning on historical event datasets, E.P.I.C. forecasts the localized traffic breakdown radius before an event even begins.</p>
        </div>
        <div class="grid-card">
            <h3>🗺️ Live Mapping</h3>
            <p>Visually map planned rallies or unplanned tree falls. The system generates high-fidelity heatmap shockwaves and automated diversion routes.</p>
        </div>
        <div class="grid-card">
            <h3>⚡ Auto-Dispatch</h3>
            <p>Converts raw ML confidence scores into plain-English tactical directives, detailing exact manpower requirements and barricading strategies.</p>
        </div>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 5. SYSTEM WORKFLOW (For the Judges)
st.markdown("### 🔄 How E.P.I.C. Works")
st.markdown("<br>", unsafe_allow_html=True)

flow_col1, flow_col2, flow_col3, flow_col4 = st.columns(4)

with flow_col1:
    st.info("**Step 1: Ingest**\n\nOfficer inputs event parameters (e.g., Political Rally at Lalbagh with Road Closure).")
with flow_col2:
    st.warning("**Step 2: Forecast**\n\nML Engine predicts spatial congestion spread and resolution time.")
with flow_col3:
    st.error("**Step 3: Visualize**\n\nPyDeck renders a 3D congestion shockwave over Bengaluru streets.")
with flow_col4:
    st.success("**Step 4: Dispatch**\n\nSystem issues automated manpower and barricading directives to field units.")