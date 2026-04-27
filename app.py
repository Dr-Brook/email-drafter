"""
Email Drafter — AI-powered job search email generator.

Built for Brook Eshete, MD, MPH — Johns Hopkins Bloomberg School of Public Health.
"""

import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

from src.email_types import EMAIL_TYPES, TONES
from src.prompts import build_prompt
from src.ai_service import check_ollama_available, generate_email, regenerate_email
from src.profile import PROFILE

# ─── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Email Drafter — Job Search",
    page_icon="✉️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1A1A2E 0%, #0D7377 100%);
        padding: 1.5rem 2rem;
        border-radius: 0.5rem;
        color: white;
        margin-bottom: 1.5rem;
    }
    .main-header h1 { margin: 0; font-size: 1.8rem; }
    .main-header p { margin: 0.3rem 0 0; opacity: 0.85; }
    .email-output {
        background: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 0.5rem;
        padding: 1.5rem;
        white-space: pre-wrap;
        font-family: inherit;
        line-height: 1.7;
    }
    .email-type-card {
        padding: 0.75rem 1rem;
        border-radius: 0.5rem;
        cursor: pointer;
        border: 2px solid transparent;
        transition: all 0.2s;
    }
    .email-type-card:hover { border-color: #0D7377; background: #f0f9f9; }
    .email-type-card.selected { border-color: #0D7377; background: #e6f5f5; }
    .history-item {
        padding: 0.75rem 1rem;
        border-radius: 0.5rem;
        border: 1px solid #dee2e6;
        margin-bottom: 0.5rem;
        cursor: pointer;
    }
    .history-item:hover { background: #f0f9f9; }
</style>
""", unsafe_allow_html=True)

# ─── Session State ──────────────────────────────────────────────────────────────
if "current_email" not in st.session_state:
    st.session_state.current_email = ""
    st.session_state.current_prompt = ""
    st.session_state.history = []

# ─── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ✉️ Email Drafter")
    st.markdown("---")

    # AI Status
    ollama_ok = check_ollama_available()
    if ollama_ok:
        st.success("🟢 AI connected")
    else:
        st.warning("🔴 AI unavailable")
        st.caption("Start Ollama for email generation")

    st.markdown("---")

    # Profile summary
    st.markdown("#### Your Profile")
    st.markdown(f"**{PROFILE['full_title']}**")
    st.caption(PROFILE["summary"][:100] + "...")
    if st.button("✏️ View Full Profile"):
        st.markdown(f"**Name:** {PROFILE['name']}")
        st.markdown(f"**Credentials:** {PROFILE['credentials']}")
        st.markdown(f"**Education:** MPH — Johns Hopkins, MD — Medical School")
        st.markdown(f"**Skills:** {', '.join(PROFILE['skills']['data_analysis'] + PROFILE['skills']['visualization'])}")
        st.markdown(f"**Focus:** {', '.join(PROFILE['target_roles'][:3])}")

    st.markdown("---")

    # Email history
    st.markdown("#### 📜 History")
    if st.session_state.history:
        for i, item in enumerate(reversed(st.session_state.history)):
            email_type_label = EMAIL_TYPES.get(item["type"], {}).get("label", item["type"])
            if st.button(f"{email_type_label} → {item['recipient']}", key=f"hist_{i}"):
                st.session_state.current_email = item["email"]
                st.rerun()
    else:
        st.caption("No emails generated yet")

    st.markdown("---")
    st.caption("Built by **Brook Eshete, MD, MPH**")

# ─── Main Content ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <h1>✉️ Job Search Email Drafter</h1>
    <p>AI-powered professional emails — cover letters, follow-ups, networking & more</p>
</div>
""", unsafe_allow_html=True)

# ─── Email Type Selection ──────────────────────────────────────────────────────
st.markdown("### What type of email?")

type_cols = st.columns(4)
selected_type = st.session_state.get("selected_type", "cover_letter")

for i, (key, val) in enumerate(EMAIL_TYPES.items()):
    with type_cols[i % 4]:
        is_selected = selected_type == key
        if st.button(
            val["label"],
            key=f"type_{key}",
            use_container_width=True,
            type="primary" if is_selected else "secondary",
        ):
            st.session_state.selected_type = key
            st.rerun()

# Fill remaining columns if needed
for i in range(len(EMAIL_TYPES), 8):
    with type_cols[i % 4]:
        pass

# Get current type config
email_type = st.session_state.get("selected_type", "cover_letter")
type_config = EMAIL_TYPES[email_type]
st.caption(f"_{type_config['description']}_")

# ─── Input Form ────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("### Fill in the details")

form_fields = {}
cols = st.columns(2)
for i, field in enumerate(type_config["fields"]):
    with cols[i % 2]:
        if field["type"] == "text":
            form_fields[field["key"]] = st.text_input(
                field["label"],
                placeholder=field.get("placeholder", ""),
                key=f"input_{field['key']}",
            )
        elif field["type"] == "textarea":
            form_fields[field["key"]] = st.text_area(
                field["label"],
                placeholder=field.get("placeholder", ""),
                height=100,
                key=f"input_{field['key']}",
            )

tone = st.selectbox("Tone", TONES, index=0, key="tone_select")

# ─── Generate Button ────────────────────────────────────────────────────────────
st.markdown("---")

col1, col2 = st.columns([1, 1])
with col1:
    generate_btn = st.button("✨ Generate Email", type="primary", use_container_width=True, disabled=not ollama_ok)
with col2:
    tweak = st.text_input("Tweak instructions (optional)", placeholder="E.g., make it shorter, more formal...", key="tweak_input")
    regenerate_btn = st.button("🔄 Regenerate", use_container_width=True, disabled=not ollama_ok or not st.session_state.current_email)

# ─── Generate ──────────────────────────────────────────────────────────────────
if generate_btn:
    # Filter out empty fields
    filled_fields = {k: v for k, v in form_fields.items() if v}
    if not filled_fields:
        st.warning("Please fill in at least a few fields before generating.")
    else:
        prompt = build_prompt(email_type, filled_fields, tone)
        st.session_state.current_prompt = prompt
        with st.spinner("Generating email..."):
            try:
                email = generate_email(prompt)
                st.session_state.current_email = email
                # Save to history
                recipient = filled_fields.get("recipient_name", "Unknown")
                st.session_state.history.append({
                    "type": email_type,
                    "recipient": recipient,
                    "email": email,
                    "fields": filled_fields,
                    "tone": tone,
                })
            except Exception as e:
                st.error(f"Error generating email: {e}")
        st.rerun()

if regenerate_btn and st.session_state.current_email:
    with st.spinner("Regenerating..."):
        try:
            email = regenerate_email(st.session_state.current_prompt, tweak)
            st.session_state.current_email = email
            # Update last history item
            if st.session_state.history:
                st.session_state.history[-1]["email"] = email
        except Exception as e:
            st.error(f"Error regenerating email: {e}")
    st.rerun()

# ─── Output ────────────────────────────────────────────────────────────────────
if st.session_state.current_email:
    st.markdown("### Generated Email")
    st.markdown(f'<div class="email-output">{st.session_state.current_email}</div>', unsafe_allow_html=True)

    # Copy button
    st.code(st.session_state.current_email, language=None)

    st.caption("Copy the text above to paste into your email client.")