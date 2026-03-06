import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Yuhan Ren - Interactive Resume", layout="wide")

# ---- personal info ----
st.title("Yuhan Ren")
st.write("mark.ren@rotman.utoronto.ca  ")
st.write("[LinkedIn](https://www.linkedin.com/in/your-profile)")

# ---- sidebar controls ----
st.sidebar.header("Show / hide sections")
show_skills = st.sidebar.checkbox("Skills", True)
show_education = st.sidebar.checkbox("Education", True)
show_experience = st.sidebar.checkbox("Work experience", True)

# additional interactive filters for skills
st.sidebar.header("Skill filters")
min_prof = st.sidebar.slider("Minimum proficiency", 0, 100, 0)
category = st.sidebar.selectbox("Skill category",
                                ["All", "Data & Analytics", "Software & AI Development", "Cloud, DevOps & Tools"])

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
    {"Company": "CIBC", "Role": "Analyst Intern", "Location": "Toronto, ON", "Duration": "Jan 2026 – now",
     "Details": "Spearheaded the development of an AI-driven extraction tool to automate retrieval and analysis of unstructured exam templates..."},
    {"Company": "Sunrise Group", "Role": "Digital Marketing Coordinator", "Location": "Charlottetown, PE", "Duration": "Oct 2022 – Apr 2025",
     "Details": "Engineered Python scripts and AI automations to clean, aggregate and analyze user engagement logs, reducing manual workload by 30%..."},
    {"Company": "Teledyne-CARIS", "Role": "Web Application Developer Intern", "Location": "Fredericton, NB", "Duration": "May 2021 – Dec 2021",
     "Details": "Architected and deployed interactive dashboards, delivered 20+ feature enhancements across 10+ sprints, driving an 11% satisfaction increase..."},
    {"Company": "Gray Wolf Analytics", "Role": "Blockchain Researcher/Developer & Mobile App Developer Intern", "Location": "Fredericton, NB", "Duration": "Jan 2020 – Aug 2020",
     "Details": "Used OSINT tools for data mining on blockchain networks and built pipelines harvesting tens of thousands of wallet addresses..."},
]

projects = {
    "BTA x Meta Case Competition": "Secured 2nd place by designing a Meta-first digital marketing strategy...",
    "Rotman Datathon": "Awarded 1st place for developing a data-driven budget reallocation strategy for a $245K SEM campaign...",
    "Personal Baking Business": "Founded and scaled an artisanal bakery brand, building custom software to manage recipes, inventory and margins..."
}

# ---- rendering ----
if show_skills:
    st.header("Skills")
    filtered = skills_df[skills_df.Proficiency >= min_prof]
    if category != "All":
        filtered = filtered[filtered.Category == category]

    st.table(filtered)
    bar = (alt.Chart(filtered)
           .mark_bar()
           .encode(x=alt.X('Skill', sort='-y'), y='Proficiency', color='Category', tooltip=['Skill','Proficiency']))
    st.altair_chart(bar, use_container_width=True)

if show_education:
    st.header("Education")
    st.table(education_df)

if show_experience:
    st.header("Work Experience")
    for exp in experience_data:
        st.subheader(f"{exp['Company']} — {exp['Role']}")
        st.write(f"{exp['Location']} | {exp['Duration']}")
        st.write(exp['Details'])

# interactive project selector
st.header("Projects")
selection = st.selectbox("Choose a project", ["None"] + list(projects.keys()))
if selection != "None":
    st.write(projects[selection])
