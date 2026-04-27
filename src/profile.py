"""Brook Eshete's professional profile — used in all AI prompts."""

PROFILE = {
    "name": "Brook S. Eshete",
    "credentials": "MD, MPH",
    "full_title": "Brook S. Eshete, MD, MPH",
    "education": [
        {"degree": "MPH", "school": "Johns Hopkins Bloomberg School of Public Health"},
        {"degree": "MD", "school": "Medical School"},
    ],
    "skills": {
        "data_analysis": ["STATA", "Python", "R", "SQL"],
        "visualization": ["Power BI", "Tableau", "Matplotlib"],
        "research": ["Epidemiology", "Program Evaluation", "Biostatistics"],
        "clinical": ["Patient Care", "Clinical Research"],
    },
    "target_roles": [
        "Public Health Data Analyst",
        "Health Informatics Specialist",
        "Program Evaluator",
        "Epidemiologist",
        "Health Data Scientist",
    ],
    "location": "DMV area (DC, Maryland, Virginia), Remote",
    "summary": (
        "Clinical medicine background transitioning to public health data analytics. "
        "Bridging clinical insight and public health strategy through data. "
        "MD + MPH from Johns Hopkins with strong analytical skills in STATA, Python, SQL, and Power BI."
    ),
}

PROFILE_CONTEXT = f"""
Name: {PROFILE['name']}
Credentials: {PROFILE['credentials']}
Education: MPH from Johns Hopkins Bloomberg School of Public Health, MD from Medical School
Skills: STATA, Python, R, SQL, Power BI, Tableau, Epidemiology, Program Evaluation, Biostatistics
Target Roles: {', '.join(PROFILE['target_roles'])}
Location: {PROFILE['location']}
Background: {PROFILE['summary']}
"""