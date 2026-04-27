"""Email type definitions and field configurations."""

EMAIL_TYPES = {
    "cover_letter": {
        "label": "📝 Cover Letter Email",
        "description": "Applying to a specific position",
        "fields": [
            {"key": "recipient_name", "label": "Recipient Name", "type": "text", "placeholder": "Dr. Jane Smith"},
            {"key": "recipient_title", "label": "Recipient Title", "type": "text", "placeholder": "Hiring Manager, Director of Public Health"},
            {"key": "company", "label": "Company/Organization", "type": "text", "placeholder": "CDC Foundation"},
            {"key": "position", "label": "Position Title", "type": "text", "placeholder": "Public Health Data Analyst"},
            {"key": "job_url", "label": "Job Posting URL (optional)", "type": "text", "placeholder": "https://..."},
            {"key": "highlights", "label": "Key Highlights to Mention", "type": "textarea", "placeholder": "E.g., MPH from Johns Hopkins, experience with STATA and Python, program evaluation background"},
        ],
    },
    "follow_up": {
        "label": "🔄 Follow-Up Email",
        "description": "After submitting an application",
        "fields": [
            {"key": "recipient_name", "label": "Recipient Name", "type": "text", "placeholder": "Dr. Jane Smith"},
            {"key": "company", "label": "Company/Organization", "type": "text", "placeholder": "CDC Foundation"},
            {"key": "position", "label": "Position Title", "type": "text", "placeholder": "Public Health Data Analyst"},
            {"key": "days_ago", "label": "Days Since Application", "type": "text", "placeholder": "7"},
            {"key": "highlights", "label": "Additional Points (optional)", "type": "textarea", "placeholder": "E.g., recent certification, new portfolio project"},
        ],
    },
    "thank_you": {
        "label": "🙏 Thank You Email",
        "description": "Post-interview follow-up",
        "fields": [
            {"key": "recipient_name", "label": "Interviewer Name", "type": "text", "placeholder": "Dr. Jane Smith"},
            {"key": "company", "label": "Company/Organization", "type": "text", "placeholder": "CDC Foundation"},
            {"key": "position", "label": "Position Title", "type": "text", "placeholder": "Public Health Data Analyst"},
            {"key": "interview_topics", "label": "Topics Discussed", "type": "textarea", "placeholder": "E.g., discussed data visualization projects, program evaluation experience"},
            {"key": "highlights", "label": "Key Points to Reinforce", "type": "textarea", "placeholder": "E.g., my experience with STATA and epidemiological analysis"},
        ],
    },
    "networking": {
        "label": "🤝 Networking/Outreach",
        "description": "Cold email to a professional contact",
        "fields": [
            {"key": "recipient_name", "label": "Recipient Name", "type": "text", "placeholder": "Dr. Jane Smith"},
            {"key": "recipient_title", "label": "Recipient Title/Role", "type": "text", "placeholder": "Director of Epidemiology at CDC"},
            {"key": "connection", "label": "Connection/Reason for Reaching Out", "type": "textarea", "placeholder": "E.g., attended same conference, mutual contact, read their recent paper on X"},
            {"key": "ask", "label": "What You're Asking For", "type": "text", "placeholder": "E.g., 15-min informational interview, advice on transitioning to public health data"},
        ],
    },
    "reference_request": {
        "label": "📋 Reference Request",
        "description": "Asking someone to be a reference",
        "fields": [
            {"key": "recipient_name", "label": "Reference Name", "type": "text", "placeholder": "Dr. Jane Smith"},
            {"key": "relationship", "label": "Your Relationship", "type": "text", "placeholder": "E.g., former supervisor, MPH advisor"},
            {"key": "position", "label": "Position You're Applying For", "type": "text", "placeholder": "Public Health Data Analyst at CDC"},
            {"key": "highlights", "label": "Remind Them of Your Work Together", "type": "textarea", "placeholder": "E.g., co-authored program evaluation report, led data analysis project"},
        ],
    },
    "salary_negotiation": {
        "label": "💰 Salary Negotiation",
        "description": "Responding to an offer",
        "fields": [
            {"key": "recipient_name", "label": "Recipient Name", "type": "text", "placeholder": "Dr. Jane Smith"},
            {"key": "company", "label": "Company/Organization", "type": "text", "placeholder": "CDC Foundation"},
            {"key": "position", "label": "Position Title", "type": "text", "placeholder": "Public Health Data Analyst"},
            {"key": "offered_salary", "label": "Offered Salary", "type": "text", "placeholder": "$75,000"},
            {"key": "target_salary", "label": "Target Salary", "type": "text", "placeholder": "$85,000"},
            {"key": "justification", "label": "Justification Points", "type": "textarea", "placeholder": "E.g., MPH from Johns Hopkins, unique clinical + data background, comparable roles pay $85K+"},
        ],
    },
    "rejection_response": {
        "label": "💌 Rejection Response",
        "description": "Professional reply to a rejection",
        "fields": [
            {"key": "recipient_name", "label": "Recipient Name", "type": "text", "placeholder": "Dr. Jane Smith"},
            {"key": "company", "label": "Company/Organization", "type": "text", "placeholder": "CDC Foundation"},
            {"key": "position", "label": "Position You Applied For", "type": "text", "placeholder": "Public Health Data Analyst"},
            {"key": "ask", "label": "What You Want to Ask (optional)", "type": "textarea", "placeholder": "E.g., feedback on application, keep me in mind for future roles"},
        ],
    },
}

TONES = ["Professional", "Warm", "Formal"]