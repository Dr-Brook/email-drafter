# Email Drafter — Job Search Email Generator

Professional email drafting tool powered by local AI. Generate cover letters, follow-ups, thank-yous, networking outreach, and more.

Built by **Brook Eshete, MD, MPH** — Johns Hopkins Bloomberg School of Public Health.

## Setup

```bash
python3.13 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## AI Setup

Requires Ollama with glm-5.1:cloud model:
```bash
ollama pull glm-5.1:cloud
ollama serve
```

## Email Types

1. Cover Letter — applying to a specific position
2. Follow-Up — after submitting an application
3. Thank You — post-interview
4. Networking/Outreach — cold email to a professional contact
5. Reference Request — asking someone to be a reference
6. Salary Negotiation — responding to an offer
7. Rejection Response — professional reply to a rejection

## Deploy

Push to GitHub → connect to [Streamlit Cloud](https://streamlit.io/cloud) → deploy.

## License

MIT