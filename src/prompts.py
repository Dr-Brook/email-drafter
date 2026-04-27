"""AI prompt templates for each email type."""

from src.profile import PROFILE_CONTEXT

SYSTEM_PROMPT = """You are a professional email writing assistant. You write concise, polished, 
job-search-related emails. The emails should be:
- Professional but not stiff
- Concise (under 200 words unless specified)
- Specific to the recipient and role
- Written from the perspective of the profile provided
- Free of filler phrases like "I hope this email finds you well" or "I am writing to"
- Direct and confident
- Properly formatted with subject line, greeting, body, and sign-off
"""


def _base_context(fields: dict) -> str:
    """Build context string from input fields."""
    parts = [f"{k.replace('_', ' ').title()}: {v}" for k, v in fields.items() if v]
    return "\n".join(parts)


def build_prompt(email_type: str, fields: dict, tone: str) -> str:
    """Build the full prompt for a given email type."""
    context = _base_context(fields)

    type_instructions = {
        "cover_letter": f"""Write a cover letter email applying for the position of "{fields.get('position', 'the role')}" at {fields.get('company', 'the organization')}. 
The email should:
- Open with a strong hook about why this role excites the candidate
- Connect the candidate's MD + MPH background to the specific role requirements
- Highlight 2-3 key qualifications that match the job
- Include a clear call to action for an interview
- Be professional and confident""",

        "follow_up": f"""Write a follow-up email sent {fields.get('days_ago', 'one week')} after applying for "{fields.get('position', 'the position')}" at {fields.get('company', 'the organization')}.
The email should:
- Reiterate genuine interest in the role
- Briefly remind them of a key qualification
- Be polite, not pushy
- Keep it short (under 100 words)""",

        "thank_you": f"""Write a post-interview thank you email for the "{fields.get('position', 'position')}" interview at {fields.get('company', 'the organization')}.
The email should:
- Thank them for their time
- Reference specific topics from the interview
- Reinforce 1-2 key qualifications
- Express continued enthusiasm
- Be warm but professional""",

        "networking": f"""Write a networking/outreach email to {fields.get('recipient_name', 'the recipient')}.
The email should:
- Open with the connection/reason for reaching out
- Briefly introduce the sender's background
- Make a clear, specific ask
- Be concise and respectful of their time
- Sound genuine, not generic""",

        "reference_request": f"""Write a reference request email to {fields.get('recipient_name', 'the reference')}.
The email should:
- Warmly remind them of the relationship
- Explain the position being applied for
- Ask if they'd be comfortable serving as a reference
- Make it easy for them to say yes or no
- Be considerate and professional""",

        "salary_negotiation": f"""Write a salary negotiation email responding to an offer of {fields.get('offered_salary', 'the offered salary')} for "{fields.get('position', 'the position')}" at {fields.get('company', 'the organization')}.
The email should:
- Express gratitude for the offer first
- Present the counter with confidence, not apology
- Back up the ask with specific justification points
- Keep it collaborative, not adversarial
- Be professional and positive""",

        "rejection_response": f"""Write a professional response to a rejection for "{fields.get('position', 'the position')}" at {fields.get('company', 'the organization')}.
The email should:
- Thank them for the opportunity
- Be gracious and positive (no bitterness)
- If appropriate, ask for feedback or express interest in future roles
- Leave the door open
- Be brief and dignified""",
    }

    instruction = type_instructions.get(email_type, "Write a professional job-search email.")

    return f"""{SYSTEM_PROMPT}

CANDIDATE PROFILE:
{PROFILE_CONTEXT}

EMAIL DETAILS:
{context}

TONE: {tone}

INSTRUCTIONS:
{instruction}

Generate a professional email with a subject line, greeting, body, and sign-off. Do not include placeholders like [Your Name] — use the candidate's actual name from the profile."""