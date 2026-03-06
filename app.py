import streamlit as st
import pandas as pd
import altair as alt
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(
    page_title="Yuhan Ren - Interactive Resume",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for fancy styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .tech-badge {
        display: inline-block;
        background-color: #e1f5fe;
        color: #0277bd;
        padding: 0.3rem 0.6rem;
        margin: 0.2rem;
        border-radius: 0.5rem;
        font-size: 0.8rem;
        font-weight: bold;
    }
    .achievement-metric {
        text-align: center;
        padding: 1rem;
        background-color: #f0f8ff;
        border-radius: 0.5rem;
        margin: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# ---- data definitions ----
skills_data = [
    {"Skill": "Python", "Category": "Data & Analytics", "Proficiency": 90},
    {"Skill": "SQL", "Category": "Data & Analytics", "Proficiency": 85},
    {"Skill": "R", "Category": "Data & Analytics", "Proficiency": 75},
    {"Skill": "Excel (VBA)", "Category": "Data & Analytics", "Proficiency": 70},
    {"Skill": "Tableau", "Category": "Data & Analytics", "Proficiency": 80},
    {"Skill": "Power BI", "Category": "Data & Analytics", "Proficiency": 70},
    {"Skill": "JavaScript", "Category": "Software & AI Development", "Proficiency": 80},
    {"Skill": "TypeScript", "Category": "Software & AI Development", "Proficiency": 75},
    {"Skill": "LLM Integration", "Category": "Software & AI Development", "Proficiency": 60},
    {"Skill": "AI Agents", "Category": "Software & AI Development", "Proficiency": 60},
    {"Skill": "JAVA", "Category": "Software & AI Development", "Proficiency": 70},
    {"Skill": "C", "Category": "Software & AI Development", "Proficiency": 65},
    {"Skill": "PHP", "Category": "Software & AI Development", "Proficiency": 60},
    {"Skill": "HTML/CSS", "Category": "Software & AI Development", "Proficiency": 80},
    {"Skill": "C#", "Category": "Software & AI Development", "Proficiency": 65},
    {"Skill": "React Native", "Category": "Software & AI Development", "Proficiency": 70},
    {"Skill": "NodeJS", "Category": "Software & AI Development", "Proficiency": 75},
    {"Skill": "AngularJS", "Category": "Software & AI Development", "Proficiency": 70},
    {"Skill": "AWS (S3/API Gateway)", "Category": "Cloud, DevOps & Tools", "Proficiency": 75},
    {"Skill": "Google Cloud Platform", "Category": "Cloud, DevOps & Tools", "Proficiency": 70},
    {"Skill": "Docker", "Category": "Cloud, DevOps & Tools", "Proficiency": 80},
    {"Skill": "Kubernetes", "Category": "Cloud, DevOps & Tools", "Proficiency": 60},
    {"Skill": "Git", "Category": "Cloud, DevOps & Tools", "Proficiency": 85},
    {"Skill": "JIRA", "Category": "Cloud, DevOps & Tools", "Proficiency": 80},
    {"Skill": "RESTful APIs", "Category": "Cloud, DevOps & Tools", "Proficiency": 80},
]
skills_df = pd.DataFrame(skills_data)

education_data = [
    {"Institution": "Rotman School of Management, University of Toronto", "Degree": "Master of Management Analytics (candidate)", "Year": "2025–2026"},
    {"Institution": "University of New Brunswick", "Degree": "BSc Computer Science", "Year": "2018–2022", "GPA": "4.0/4.3"}
]
education_df = pd.DataFrame(education_data)

experience_data = [
    {
        "Company": "CIBC",
        "Role": "Analyst Intern",
        "Location": "Toronto, ON",
        "Duration": "Jan 2026 – now",
        "Start": "2026-01-01",
        "End": datetime.now().strftime("%Y-%m-%d"),
        "Details": [
            "Spearheaded the development of an AI-driven extraction tool to automate the retrieval and analysis of data from complex, unstructured test templates across 100+ annual compliance examinations.",
            "Leveraged Large Language Models (LLMs) and RAG architectures to radically simplify the manual documentation lifecycle, targeting a significant reduction in the 580 hours required per individual exam.",
            "Collaborated cross-functionally with Directors and compliance teams to define technical test criteria, designing a scalable solution poised for adoption by US and Caribbean examination teams."
        ]
    },
    {
        "Company": "Sunrise Group",
        "Role": "Digital Marketing Coordinator",
        "Location": "Charlottetown, PE",
        "Duration": "Oct 2022 – Apr 2025",
        "Start": "2022-10-01",
        "End": "2025-04-30",
        "Details": [
            "Digital Marketing Coordinator: Engineered Python scripts and AI-driven automations to clean, aggregate, and analyze complex user engagement logs, successfully reducing manual data processing workload by 30%.",
            "Designed and executed rigorous A/B tests to optimize digital content strategy, developing weekly automated insight dashboards to guide data-driven partnership targeting and campaign budget allocation."
        ]
    },
    {
        "Company": "Teledyne-CARIS",
        "Role": "Web Application Developer Intern",
        "Location": "Fredericton, NB",
        "Duration": "May 2021 – Dec 2021",
        "Start": "2021-05-01",
        "End": "2021-12-31",
        "Details": [
            "Architected and deployed new data visualization layouts and interactive dashboard templates to effectively render complex analytical gadgets for customer-facing web applications.",
            "Delivered 20+ critical feature enhancements across 10+ Agile sprint cycles, streamlining data product usability and directly driving an 11% increase in measurable client satisfaction scores."
        ]
    },
    {
        "Company": "Gray Wolf Analytics",
        "Role": "Blockchain Researcher/Developer & Mobile App Developer Intern",
        "Location": "Fredericton, NB",
        "Duration": "Jan 2020 – Aug 2020",
        "Start": "2020-01-01",
        "End": "2020-08-31",
        "Details": [
            "Leveraged 10+ open-source intelligence (OSINT) tools to conduct in-depth data mining and threat analysis on complex blockchain networks.",
            "Developed a robust data collection pipeline to harvest and process tens of thousands of Bitcoin wallet addresses, building comprehensive graph networks for advanced data visualization and pattern recognition."
        ]
    }
]

projects = {
    "BTA x Meta Case Competition": [
        "Secured 2nd Place by designing a Meta-first digital marketing strategy tailored to modernize brand relevance and drive measurable, incremental sales among Gen Z and Millennial demographics.",
        "Architected a high-converting two-channel marketing funnel, applying lift-based measurement techniques and data-driven budget allocation to optimize real-world marketing ROI."
    ],
    "Rotman Datathon": [
        "Awarded 1st Place for developing a data-driven budget reallocation strategy for a $245K search engine marketing campaign based on causality testing.",
        "Analyzed 6,800+ hours of embedded A/B testing data (PPC vs. SEO) across US and Canadian markets using Difference-in-Differences (DiD) regression and Poisson GLM to evaluate traffic substitution rates.",
        "Delivered actionable business insights, uncovering a 71% organic substitution rate in Canada versus 25% in the US, and modeled ROI profitability to recommend a highly optimized $155K–$170K marketing spend."
    ],
    "Personal Baking Business": [
        "Founded and scaled an artisanal bakery brand, managing end-to-end commercial operations, from product development and B2B catering to social media marketing strategy.",
        "Developed a custom software tool to optimize backend business operations, implementing features for robust recipe management, ingredient inventory tracking, and granular profit margin analysis."
    ]
}

# ---- sidebar controls ----
st.sidebar.title("🎛️ Controls")
theme = st.sidebar.radio("Theme", ["Light", "Dark"], index=0)
show_home = st.sidebar.checkbox("Home", True)
show_skills = st.sidebar.checkbox("Skills", True)
show_experience = st.sidebar.checkbox("Experience", True)
show_projects = st.sidebar.checkbox("Projects", True)
show_education = st.sidebar.checkbox("Education", True)

# Skill filters
st.sidebar.subheader("Skill Filters")
min_prof = st.sidebar.slider("Minimum Proficiency", 0, 100, 0)
category = st.sidebar.selectbox("Category", ["All", "Data & Analytics", "Software & AI Development", "Cloud, DevOps & Tools"])
selected_skills = st.sidebar.multiselect("Select Skills", skills_df['Skill'].tolist(), default=skills_df['Skill'].tolist()[:5])

# ---- main content ----
st.markdown('<div class="main-header">🚀 Yuhan Ren - Interactive Resume</div>', unsafe_allow_html=True)
st.write("mark.ren@rotman.utoronto.ca | [LinkedIn](https://www.linkedin.com/in/your-profile)")

# Tabs
if show_home:
    with st.expander("🏠 Home - Quick Overview", expanded=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Years of Experience", "6+")
        with col2:
            st.metric("Projects Completed", "3+")
        with col3:
            st.metric("Skills Mastered", "20+")
        
        st.subheader("Tech Stack Highlights")
        tech_stack = ["Python", "JavaScript", "SQL", "AWS", "Docker", "LLMs", "React", "Tableau"]
        badges = "".join([f'<span class="tech-badge">{tech}</span>' for tech in tech_stack])
        st.markdown(badges, unsafe_allow_html=True)

if show_skills:
    with st.expander("🛠️ Skills", expanded=True):
        filtered = skills_df[(skills_df.Proficiency >= min_prof) & (skills_df.Skill.isin(selected_skills))]
        if category != "All":
            filtered = filtered[filtered.Category == category]
        
        st.table(filtered)
        
        chart_type = st.selectbox("Chart Type", ["Bar Chart", "Radar Chart"])
        if chart_type == "Bar Chart":
            bar = alt.Chart(filtered).mark_bar().encode(
                x=alt.X('Skill', sort='-y'),
                y='Proficiency',
                color='Category',
                tooltip=['Skill', 'Proficiency']
            ).properties(width=600, height=400)
            st.altair_chart(bar, use_container_width=True)
        else:
            # Radar chart with Plotly
            categories = filtered['Skill'].tolist()
            values = filtered['Proficiency'].tolist()
            fig = go.Figure()
            fig.add_trace(go.Scatterpolar(
                r=values + [values[0]],
                theta=categories + [categories[0]],
                fill='toself',
                name='Proficiency'
            ))
            fig.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                showlegend=False,
                title="Skill Proficiency Radar"
            )
            st.plotly_chart(fig, use_container_width=True)

if show_experience:
    with st.expander("💼 Work Experience", expanded=True):
        # Timeline chart
        exp_df = pd.DataFrame(experience_data)
        timeline = alt.Chart(exp_df).mark_bar().encode(
            x=alt.X('Start:T', title='Time'),
            x2='End:T',
            y=alt.Y('Company', sort=alt.SortField('Start', order='descending')),
            color='Role',
            tooltip=['Company', 'Role', 'Duration']
        ).properties(width=600, height=300, title="Experience Timeline")
        st.altair_chart(timeline, use_container_width=True)
        
        for exp in experience_data:
            with st.expander(f"{exp['Company']} - {exp['Role']} ({exp['Duration']})"):
                st.write(f"**Location:** {exp['Location']}")
                for detail in exp['Details']:
                    st.write(f"• {detail}")

if show_projects:
    with st.expander("🚀 Projects", expanded=True):
        selection = st.selectbox("Choose a project", ["None"] + list(projects.keys()))
        if selection != "None":
            st.subheader(selection)
            for detail in projects[selection]:
                st.write(f"• {detail}")

if show_education:
    with st.expander("🎓 Education", expanded=True):
        st.table(education_df)

# Footer
st.markdown("---")
st.write("Built with Streamlit | Last updated: March 2026")