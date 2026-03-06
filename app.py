import streamlit as st
import pandas as pd
import altair as alt
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(
    page_title="Yuhan Ren - Intelligent Resume Copilot",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ======== Advanced CSS + Neo-Brutalist Design ========
st.markdown("""
<style>
    :root {
        --primary: #0f0f0f;
        --accent: #00d4ff;
        --warning: #ff006e;
        --success: #00ff41;
    }
    
    * {
        font-family: 'IBM Plex Mono', 'Courier New', monospace;
    }
    
    .hero-section {
        background: linear-gradient(135deg, #0f0f0f 0%, #1a1a2e 100%);
        border: 3px solid var(--accent);
        padding: 2rem;
        margin: 1rem 0;
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: 
            repeating-linear-gradient(
                0deg,
                rgba(0, 212, 255, 0.03) 0px,
                rgba(0, 212, 255, 0.03) 1px,
                transparent 1px,
                transparent 2px
            );
        pointer-events: none;
    }
    
    .conversation-turn {
        background: #1a1a2e;
        border-left: 5px solid var(--accent);
        padding: 1.5rem;
        margin: 1rem 0;
        transform: skewX(-2deg);
        position: relative;
        color: #f0f0f0;
    }
    
    .user-intent {
        background: #2d2d44;
        border: 2px dashed var(--warning);
        padding: 1rem;
        margin: 1rem 0;
        font-style: italic;
        color: var(--warning);
    }
    
    .neural-badge {
        display: inline-block;
        background: linear-gradient(90deg, var(--accent), #00ff41);
        color: #0f0f0f;
        padding: 0.4rem 0.8rem;
        font-weight: bold;
        font-size: 0.75rem;
        letter-spacing: 1px;
        margin: 0.3rem;
        clip-path: polygon(0 0, 100% 0, 95% 100%, 0 100%);
    }
    
    .skill-gauge {
        background: #1a1a2e;
        border: 1px solid var(--accent);
        padding: 0.8rem;
        margin: 0.5rem 0;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 0.8rem;
        color: #f0f0f0;
    }
    
    .timeline-event {
        border: 2px solid var(--accent);
        padding: 1.5rem;
        margin: 1.5rem 0;
        background: rgba(0, 212, 255, 0.05);
        position: relative;
        color: #f0f0f0;
    }
    
    .timeline-event::after {
        content: '';
        position: absolute;
        width: 20px;
        height: 20px;
        background: var(--accent);
        border: 3px solid #0f0f0f;
        border-radius: 50%;
        right: -40px;
        top: 1.5rem;
        z-index: 10;
    }
    
    .agentic-suggestion {
        background: linear-gradient(90deg, rgba(0, 255, 65, 0.1), rgba(0, 212, 255, 0.1));
        border: 2px solid var(--success);
        padding: 1rem;
        margin: 1rem 0;
        position: relative;
        color: #f0f0f0;
    }
    
    .agentic-suggestion::before {
        content: '🤖 AI AGENT INSIGHT';
        display: block;
        color: var(--success);
        font-weight: bold;
        margin-bottom: 0.5rem;
        font-size: 0.8rem;
        letter-spacing: 1px;
    }
    
    .generative-ui {
        animation: slideIn 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-20px) rotate(-1deg);
        }
        to {
            opacity: 1;
            transform: translateX(0) rotate(0deg);
        }
    }
    
    .micro-interaction {
        transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    
    .micro-interaction:hover {
        transform: scale(1.05) skewY(-1deg);
        border-color: var(--success);
        box-shadow: 0 0 20px rgba(0, 255, 65, 0.3);
    }
    
    .turn-counter {
        position: fixed;
        top: 20px;
        right: 20px;
        background: var(--accent);
        color: #0f0f0f;
        padding: 0.5rem 1rem;
        font-weight: bold;
        font-size: 0.9rem;
        z-index: 100;
        clip-path: polygon(0 0, 100% 0, 95% 100%, 0 100%);
    }
</style>
""", unsafe_allow_html=True)

# ======== Session State & Data ========
if 'turn_count' not in st.session_state:
    st.session_state.turn_count = 0

skills_data = [
    {"Skill": "Python", "Category": "Data & Analytics", "Proficiency": 90, "Years": 3},
    {"Skill": "SQL", "Category": "Data & Analytics", "Proficiency": 85, "Years": 3},
    {"Skill": "R", "Category": "Data & Analytics", "Proficiency": 75, "Years": 2},
    {"Skill": "Tableau", "Category": "Data & Analytics", "Proficiency": 80, "Years": 2},
    {"Skill": "Power BI", "Category": "Data & Analytics", "Proficiency": 70, "Years": 1},
    {"Skill": "JavaScript", "Category": "Software & AI", "Proficiency": 80, "Years": 3},
    {"Skill": "TypeScript", "Category": "Software & AI", "Proficiency": 75, "Years": 2},
    {"Skill": "LLM Integration", "Category": "Software & AI", "Proficiency": 85, "Years": 1},
    {"Skill": "AI Agents", "Category": "Software & AI", "Proficiency": 80, "Years": 1},
    {"Skill": "React", "Category": "Software & AI", "Proficiency": 75, "Years": 2},
    {"Skill": "NodeJS", "Category": "Software & AI", "Proficiency": 75, "Years": 2},
    {"Skill": "AWS", "Category": "Cloud & DevOps", "Proficiency": 75, "Years": 2},
    {"Skill": "Docker", "Category": "Cloud & DevOps", "Proficiency": 80, "Years": 2},
    {"Skill": "Git", "Category": "Cloud & DevOps", "Proficiency": 85, "Years": 3},
]
skills_df = pd.DataFrame(skills_data)

experience_data = [
    {
        "Company": "CIBC",
        "Role": "Analyst Intern",
        "Duration": "Jan 2026 – Present",
        "Details": [
            "Built AI-driven extraction tool automating 100+ compliance exam data retrieval",
            "Leveraged LLMs + RAG to reduce manual documentation lifecycle by 580+ hours/exam",
            "Designed scalable solution for US & Caribbean examination teams"
        ]
    },
    {
        "Company": "Sunrise Group",
        "Role": "Digital Marketing Coordinator",
        "Duration": "Oct 2022 – Apr 2025",
        "Details": [
            "Engineered Python automation scripts reducing manual workload by 30%",
            "Executed A/B tests optimizing digital strategy, created automated insight dashboards",
            "Data-driven budget allocation for partnership targeting & campaigns"
        ]
    },
    {
        "Company": "Teledyne-CARIS",
        "Role": "Web Application Developer Intern",
        "Duration": "May 2021 – Dec 2021",
        "Details": [
            "Architected interactive dashboard templates for customer-facing web apps",
            "Delivered 20+ features across 10+ Agile sprints, 11% satisfaction boost",
            "Complex analytical gadget visualization & UX optimization"
        ]
    },
    {
        "Company": "Gray Wolf Analytics",
        "Role": "Blockchain Researcher & Mobile App Dev Intern",
        "Duration": "Jan 2020 – Aug 2020",
        "Details": [
            "Conducted in-depth data mining on blockchain networks using 10+ OSINT tools",
            "Built data pipeline harvesting tens of thousands Bitcoin wallet addresses",
            "Graph network visualization for advanced pattern recognition"
        ]
    }
]

# ======== Hero Section ========
st.markdown('<div class="turn-counter">INTENT: ACTIVE</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    <div class="hero-section">
        <h1 style="color: #00d4ff; font-size: 3.5rem; margin: 0; line-height: 1;">YUHAN REN</h1>
        <p style="color: #00ff41; font-size: 1.2rem; margin: 0.3rem 0; letter-spacing: 2px;">
            AI × DATA × WEB ENGINEER
        </p>
        <p style="color: #888; font-size: 0.9rem; margin: 0.5rem 0;">
            mark.ren@rotman.utoronto.ca
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: #1a1a2e; border: 2px solid #00d4ff; padding: 1.5rem; height: 100%; display: flex; flex-direction: column; justify-content: center;">
        <div style="text-align: center;">
            <div style="color: #00d4ff; font-weight: bold; font-size: 2rem;">6+</div>
            <div style="color: #888; font-size: 0.9rem;">Years Active</div>
        </div>
        <hr style="border: 1px solid #00ff41; margin: 1rem 0;">
        <div style="text-align: center;">
            <div style="color: #00ff41; font-weight: bold; font-size: 2rem;">3</div>
            <div style="color: #888; font-size: 0.9rem;">Awards Won</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ======== Generative Conversation UI ========
st.markdown("---")
st.markdown("### 🧠 INTELLIGENT INTENT SCANNER")
st.write("This interface detects your intent and **generates personalized micro-apps in real-time**.")

user_prompt = st.text_input(
    "Query Your Profile:",
    placeholder="e.g., 'AI/ML skills', 'Timeline', 'Awards', 'Growth'",
    key="main_input"
)

def detect_intent(prompt):
    intent_map = {
        "skills": ["skill", "proficiency", "technical", "language", "framework", "competency"],
        "experience": ["experience", "timeline", "job", "work", "career", "role", "employment"],
        "projects": ["project", "award", "achievement", "accomplishment", "built", "first"],
        "growth": ["growth", "learning", "trajectory", "evolution", "progress", "years"],
        "summary": ["summary", "overview", "about", "intro", "profile", "brief"]
    }
    
    prompt_lower = prompt.lower()
    for intent, keywords in intent_map.items():
        if any(kw in prompt_lower for kw in keywords):
            return intent
    return "summary"

if user_prompt:
    st.session_state.turn_count += 1
    detected_intent = detect_intent(user_prompt)
    
    st.markdown(f'<div class="conversation-turn generative-ui">', unsafe_allow_html=True)
    
    col_left, col_mid = st.columns([1, 3])
    with col_left:
        st.markdown(f'<div class="user-intent">INTENT:<br/><strong>{detected_intent.upper()}</strong></div>', unsafe_allow_html=True)
    
    with col_mid:
        st.markdown(f'<div class="agentic-suggestion">Generating micro-UI for: <strong>{detected_intent}</strong> cluster...</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ======== INTENT-DRIVEN GENERATIVE UI ========
    if detected_intent == "skills":
        st.markdown("### ⚙️ SKILL MATRIX INTERFACE")
        
        skill_focus = st.selectbox("Category Filter", ["All", "Data & Analytics", "Software & AI", "Cloud & DevOps"])
        filtered_skills = skills_df if skill_focus == "All" else skills_df[skills_df['Category'] == skill_focus]
        
        for idx, skill in filtered_skills.iterrows():
            col_name, col_bar, col_years = st.columns([2, 3, 1])
            with col_name:
                st.markdown(f'<div class="skill-gauge">{skill["Skill"]}</div>', unsafe_allow_html=True)
            with col_bar:
                st.progress(skill["Proficiency"] / 100)
            with col_years:
                st.markdown(f'<div style="text-align: right; color: #00d4ff; font-weight: bold;">{skill["Years"]}y exp</div>', unsafe_allow_html=True)
        
        st.markdown("#### PROFICIENCY RADAR")
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=filtered_skills['Proficiency'].tolist() + [filtered_skills['Proficiency'].iloc[0]],
            theta=filtered_skills['Skill'].tolist() + [filtered_skills['Skill'].iloc[0]],
            fill='toself',
            fillcolor='rgba(0, 212, 255, 0.2)',
            line=dict(color='#00d4ff', width=2)
        ))
        fig.update_layout(
            polar=dict(
                bgcolor='rgba(26, 26, 46, 0.5)',
                radialaxis=dict(visible=True, range=[0, 100], gridcolor='#00d4ff', gridwidth=0.5)
            ),
            paper_bgcolor='rgba(15, 15, 15, 0)',
            font=dict(color='#00d4ff'),
            showlegend=False,
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    elif detected_intent == "experience":
        st.markdown("### 📍 CAREER EVOLUTION TIMELINE")
        
        for idx, exp in enumerate(experience_data):
            st.markdown(f"""
            <div class="timeline-event micro-interaction" style="border-color: {'#00ff41' if idx == 0 else '#00d4ff'};">
                <h3 style="margin: 0; color: {'#00ff41' if idx == 0 else '#00d4ff'};">{'[CURRENT] ' if idx == 0 else ''}{exp['Company']}</h3>
                <p style="margin: 0.3rem 0; color: #ff006e; font-weight: bold;">{exp['Role']}</p>
                <p style="margin: 0.3rem 0; color: #888; font-size: 0.9rem;">{exp['Duration']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            for detail in exp['Details']:
                st.markdown(f"▪ {detail}")
            if idx < len(experience_data) - 1:
                st.markdown("---")
    
    elif detected_intent == "projects":
        st.markdown("### 🚀 AWARD-WINNING ACHIEVEMENTS")
        
        projects = {
            "BTA x Meta Competition": {
                "rank": "🥈 2nd Place",
                "desc": "Designed Meta-first digital marketing strategy for Gen Z & Millennial demographics",
                "tech": ["Marketing", "Data Analysis", "Strategy"]
            },
            "Rotman Datathon": {
                "rank": "🥇 1st Place",
                "desc": "$245K SEM campaign optimization via Difference-in-Differences regression analysis",
                "tech": ["Python", "Statistics", "Causality"]
            },
            "Personal Baking Business": {
                "rank": "👑 Founder",
                "desc": "Full-stack e-commerce with AI-powered inventory & recipe optimization engine",
                "tech": ["Full Stack", "Operations", "AI"]
            }
        }
        
        for proj_name, proj_data in projects.items():
            st.markdown(f"""
            <div class="timeline-event micro-interaction" style="border-color: #00ff41;">
                <h3 style="margin: 0; color: #00ff41;">{proj_data['rank']} {proj_name}</h3>
                <p style="margin: 0.5rem 0; color: #ddd;">{proj_data['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            for tech in proj_data['tech']:
                st.markdown(f'<span class="neural-badge">{tech}</span>', unsafe_allow_html=True)
            st.markdown("")
    
    elif detected_intent == "growth":
        st.markdown("### 📈 NEURAL PROFICIENCY TRAJECTORY")
        
        growth_data = pd.DataFrame({
            'Year': ['2020', '2021', '2022', '2023', '2024', '2025', '2026'],
            'Proficiency': [30, 45, 65, 75, 82, 90, 95]
        })
        
        chart = alt.Chart(growth_data).mark_line(point=True, size=3, color='#00d4ff').encode(
            x='Year:O',
            y=alt.Y('Proficiency:Q', scale=alt.Scale(domain=[0, 100])),
            tooltip=['Year', 'Proficiency']
        ).properties(width=600, height=300, title="6-Year Skill Elevation Arc")
        
        st.altair_chart(chart, use_container_width=True)
    
    else:  # summary
        st.markdown("### 📋 NEURAL PROFILE SNAPSHOT")
        st.markdown("""
        **🎓 Educational Foundation**  
        • Master of Management Analytics @ Rotman School (2025-2026)  
        • BSc Computer Science @ University of New Brunswick (GPA: 4.0/4.3)
        
        **🔬 Technical Specializations**  
        • Large Language Models & Generative AI Integration  
        • Data-Driven Decision Architecture  
        • Full-Stack Web Engineering & Cloud Infrastructure
        """)
        
        metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
        with metric_col1:
            st.metric("Languages", "14")
        with metric_col2:
            st.metric("Experience", "6+ yrs")
        with metric_col3:
            st.metric("Projects", "10+")
        with metric_col4:
            st.metric("Awards", "3")

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888; font-size: 0.85rem; margin-top: 3rem;">
    <strong style="color: #00d4ff;">GENERATIVE UI INTERFACE</strong> | Powered by Intent Detection & Dynamic Rendering  
    <br/>
    <em style="color: #00ff41;">2026 HCI Paradigm: Agentic + Spatial + Emotion-Aware</em>
    <br/>
    Micro-interactions • Neo-Brutalist Aesthetics • Real-time Micro-apps
</div>
""", unsafe_allow_html=True)
