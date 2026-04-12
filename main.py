import streamlit as st
import streamlit.components.v1 as components
import base64
import os


# ── Resume loader ──────────────────────────────────────────────────────
def get_base64_file(filename: str):
    """Return base64-encoded string of file if found, else None."""
    for path in [
        os.path.join(os.path.dirname(os.path.abspath(__file__)), filename),
        os.path.join(os.getcwd(), filename),
        filename,
    ]:
        if os.path.isfile(path):
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode("utf-8")
    return None

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Priyanka Pal | Data Scientist & AI Engineer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Session state ─────────────────────────────────────────────────────────────
if "theme" not in st.session_state:
    st.session_state.theme = "dark"
if "active_section" not in st.session_state:
    st.session_state.active_section = "Home"
if "project_filter" not in st.session_state:
    st.session_state.project_filter = "All"

# ── Theme colours ─────────────────────────────────────────────────────────────
DARK = {
    "bg":        "#12131f",
    "bg2":       "#181929",
    "bg3":       "#1e1f35",
    "card":      "rgba(30,32,58,0.95)",
    "card2":     "rgba(38,40,70,0.90)",
    "glass":     "rgba(255,255,255,0.07)",
    "border":    "rgba(130,140,255,0.28)",
    "accent1":   "#b1adf5",
    "accent2":   "#a0e9f8",
    "accent3":   "#fa98bd",
    "text":      "#f0f0ff",
    "subtext":   "#b8b8d8",
    "muted":     "#8c8ca4",
    "grad1":     "linear-gradient(135deg,#7c74ff 0%,#38d9fa 100%)",
    "grad2":     "linear-gradient(135deg,#ff80b0 0%,#7c74ff 100%)",
    "grad3":     "linear-gradient(135deg,#38d9fa 0%,#00ffa3 100%)",
    "sidebar":   "#0e0f1e",
}
LIGHT = {
    "bg":        "#f0f0fa",
    "bg2":       "#e8e8f5",
    "bg3":       "#dcdcf0",
    "card":      "rgba(255,255,255,0.90)",
    "card2":     "rgba(235,235,250,0.85)",
    "glass":     "rgba(100,99,255,0.06)",
    "border":    "rgba(100,99,255,0.25)",
    "accent1":   "#493ee8",
    "accent2":   "#0099cc",
    "accent3":   "#e0456b",
    "text":      "#1a1a2e",
    "subtext":   "#4a4a6a",
    "muted":     "#2d2d65",
    "grad1":     "linear-gradient(135deg,#5046e5 0%,#0099cc 100%)",
    "grad2":     "linear-gradient(135deg,#e0456b 0%,#5046e5 100%)",
    "grad3":     "linear-gradient(135deg,#0099cc 0%,#00cc88 100%)",
    "sidebar":   "#e2e2f2",
}

C = DARK if st.session_state.theme == "dark" else LIGHT

# ── SVG logos ─────────────────────────────────────────────────────────────────
GH_LOGO_LG = """<svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor" style="flex-shrink:0;vertical-align:middle;">
  <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/>
</svg>"""

LI_LOGO_LG = """<svg width="17" height="17" viewBox="0 0 24 24" fill="#0A66C2" style="flex-shrink:0;vertical-align:middle;">
  <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
</svg>"""

GH_LOGO_CONTACT = """<svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor">
  <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/>
</svg>"""

LI_LOGO_CONTACT = """<svg width="22" height="22" viewBox="0 0 24 24" fill="#0A66C2">
  <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
</svg>"""

GH_LOGO_SM = """<svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor">
  <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/>
</svg>"""

# ── Global CSS ────────────────────────────────────────────────────────────────
def inject_css():
    st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;600&display=swap');

*, *::before, *::after {{ box-sizing: border-box; }}

html, body, [data-testid="stAppViewContainer"] {{
    background: {C['bg']} !important;
    color: {C['text']} !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 16px !important;
    line-height: 1.6 !important;
}}

[data-testid="stAppViewContainer"] {{
    background: radial-gradient(ellipse 80% 60% at 50% -10%, rgba(108,99,255,0.18) 0%, transparent 60%),
                radial-gradient(ellipse 60% 40% at 90% 80%,  rgba(0,212,255,0.12) 0%, transparent 60%),
                {C['bg']} !important;
    min-height: 100vh;
}}

[data-testid="stSidebar"] {{
    background: {C['sidebar']} !important;
    border-right: 1px solid {C['border']} !important;
    backdrop-filter: blur(20px);
}}
[data-testid="stSidebar"] > div {{ padding: 0 !important; }}

#MainMenu, footer, header {{ visibility: hidden; }}
[data-testid="stDecoration"] {{ display: none; }}
.stDeployButton {{ display: none; }}
[data-testid="collapsedControl"] {{ color: {C['accent1']} !important; }}

h1, h2, h3, h4, h5 {{
    font-family: 'Syne', sans-serif !important;
    color: {C['text']} !important;
    line-height: 1.25 !important;
    letter-spacing: -0.01em !important;
    margin-top: 0 !important;
}}

[data-testid="stMainBlockContainer"] {{
    padding: 1rem 3rem !important;
    max-width: 1100px;
}}

p, div, span, li {{ font-family: 'DM Sans', sans-serif; line-height: 1.7; }}

[data-testid="stMarkdownContainer"] p {{
    color: {C['subtext']} !important;
    font-size: 1rem !important;
    line-height: 1.75 !important;
}}

::-webkit-scrollbar {{ width: 5px; }}
::-webkit-scrollbar-track {{ background: {C['bg']}; }}
::-webkit-scrollbar-thumb {{ background: {C['accent1']}44; border-radius: 8px; }}
::-webkit-scrollbar-thumb:hover {{ background: {C['accent1']}88; }}

@keyframes fadeInUp {{
    from {{ opacity: 0; transform: translateY(28px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
}}
@keyframes fadeInLeft {{
    from {{ opacity: 0; transform: translateX(-24px); }}
    to   {{ opacity: 1; transform: translateX(0); }}
}}
@keyframes float {{
    0%, 100% {{ transform: translateY(0px); }}
    50%       {{ transform: translateY(-8px); }}
}}
@keyframes pulse-ring {{
    0%   {{ box-shadow: 0 0 0 0 {C['accent1']}55; }}
    70%  {{ box-shadow: 0 0 0 16px {C['accent1']}00; }}
    100% {{ box-shadow: 0 0 0 0   {C['accent1']}00; }}
}}
@keyframes gradientMove {{
    0%   {{ background-position: 0%   50%; }}
    50%  {{ background-position: 100% 50%; }}
    100% {{ background-position: 0%   50%; }}
}}

.section-wrapper {{
    animation: fadeInUp 0.7s ease both;
    padding-bottom: 1.5rem;
}}

/* ── Glass card ── */
.glass-card {{
    background: {C['card']};
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border: 1px solid {C['border']};
    border-radius: 20px;
    padding: 1.5rem;
    transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
    position: relative;
    overflow: hidden;
    color: {C['text']};
}}
.glass-card p, .glass-card div, .glass-card span, .glass-card li {{ color: {C['subtext']}; }}
.glass-card::before {{
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(255,255,255,0.04) 0%, transparent 60%);
    pointer-events: none;
    z-index: 0;
}}
.glass-card > * {{ position: relative; z-index: 1; }}
.glass-card:hover {{
    transform: translateY(-4px);
    box-shadow: 0 20px 60px rgba(124,116,255,0.20);
    border-color: {C['accent1']}66;
}}

/* ── Hero ── */
.hero-container {{
    text-align: center;
    padding: 1.5rem 2rem 1.2rem;
    position: relative;
    animation: fadeInUp 0.8s ease both;
}}
.hero-avatar {{
    width: 160px; height: 160px;
    border-radius: 50%;
    margin: 0 auto 1.1rem;
    position: relative;
    z-index: 1;
    overflow: hidden;
    box-shadow: 0 0 0 3px {C['accent1']}66, 0 10px 50px {C['accent1']}40;
    animation: float 5s ease-in-out infinite;
}}
.hero-avatar img {{
    width: 100%; height: 100%;
    object-fit: cover;
    object-position: center top;
    border-radius: 50%;
    display: block;
}}
.hero-avatar-fallback {{
    width: 160px; height: 160px;
    border-radius: 50%;
    background: {C['grad1']};
    display: flex; align-items: center; justify-content: center;
    font-size: 4rem;
    margin: 0 auto 1.1rem;
    animation: float 5s ease-in-out infinite, pulse-ring 2.5s infinite;
    border: 3px solid {C['border']};
}}
.hero-name {{
    font-family: 'Syne', sans-serif !important;
    font-size: 2.8rem !important;
    font-weight: 800 !important;
    background: {C['grad1']};
    background-size: 200% auto;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    animation: gradientMove 4s linear infinite;
    line-height: 1.2 !important;
    margin-bottom: 0.3rem !important;
    display: block !important;
}}
.hero-role {{
    font-family: 'DM Sans', sans-serif;
    font-size: 1.05rem;
    color: {C['subtext']};
    letter-spacing: 0.06em;
    margin-bottom: 0.7rem;
    font-weight: 500;
    display: block;
}}
.hero-tagline {{
    font-size: 0.95rem;
    color: {C['subtext']};
    max-width: 520px;
    margin: 0 auto 0.9rem;
    line-height: 1.7;
    display: block;
}}
.hero-badge {{
    display: inline-block;
    background: {C['glass']};
    border: 1px solid {C['border']};
    border-radius: 999px;
    padding: 0.25rem 0.8rem;
    font-size: 0.76rem;
    color: {C['accent2']};
    margin: 0.12rem;
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 0.04em;
    transition: background 0.2s, transform 0.2s;
}}
.hero-badge:hover {{ background: {C['accent1']}22; transform: scale(1.06); }}

.hero-btns {{
    margin-top: 1rem;
    display: flex;
    gap: 0.8rem;
    justify-content: center;
    flex-wrap: wrap;
    align-items: center;
}}
.btn-primary {{
    display: inline-flex; align-items: center; gap: 0.45rem;
    background: {C['grad1']};
    color: #fff !important;
    padding: 0.6rem 1.5rem;
    border-radius: 999px;
    font-weight: 600;
    font-size: 0.88rem;
    text-decoration: none !important;
    transition: opacity 0.2s, transform 0.2s, box-shadow 0.2s;
    box-shadow: 0 4px 20px {C['accent1']}44;
    letter-spacing: 0.03em;
    cursor: pointer;
    font-family: 'DM Sans', sans-serif;
    border: none;
    outline: none;
    -webkit-text-fill-color: #fff !important;
}}
.btn-primary:hover {{
    opacity: 0.88;
    transform: translateY(-2px);
    box-shadow: 0 8px 30px {C['accent1']}66;
}}
.btn-secondary {{
    display: inline-flex; align-items: center; gap: 0.45rem;
    background: {C['glass']};
    border: 1px solid {C['border']};
    color: {C['text']} !important;
    padding: 0.6rem 1.4rem;
    border-radius: 999px;
    font-weight: 600;
    font-size: 0.88rem;
    text-decoration: none !important;
    transition: background 0.2s, transform 0.2s, border-color 0.2s;
    letter-spacing: 0.03em;
}}
.btn-secondary:hover {{
    background: {C['accent1']}22;
    border-color: {C['accent1']}66;
    transform: translateY(-2px);
}}

/* ── Resume button — JS blob opener ── */
.resume-btn {{
    display: inline-flex; align-items: center; gap: 0.45rem;
    background: {C['grad1']};
    color: #fff !important;
    -webkit-text-fill-color: #fff !important;
    padding: 0.6rem 1.5rem;
    border-radius: 999px;
    font-weight: 600;
    font-size: 0.88rem;
    font-family: 'DM Sans', sans-serif;
    letter-spacing: 0.03em;
    cursor: pointer;
    border: none;
    outline: none;
    box-shadow: 0 4px 20px {C['accent1']}44;
    transition: opacity 0.2s, transform 0.2s, box-shadow 0.2s;
    text-decoration: none !important;
}}
.resume-btn:hover {{
    opacity: 0.88;
    transform: translateY(-2px);
    box-shadow: 0 8px 30px {C['accent1']}66;
}}

/* ── Section title ── */
.section-title {{
    font-family: 'Syne', sans-serif !important;
    font-size: 2.1rem !important;
    font-weight: 800 !important;
    color: {C['text']} !important;
    margin-bottom: 0.3rem !important;
    display: block !important;
    line-height: 1.2 !important;
}}
.section-title span {{
    background: {C['grad1']};
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}}
.section-divider {{
    height: 3px;
    width: 60px;
    background: {C['grad1']};
    border-radius: 4px;
    margin-bottom: 1.2rem;
}}

/* ── Skill pills ── */
.skill-pill {{
    display: inline-block;
    background: {C['glass']};
    border: 1px solid {C['border']};
    border-radius: 999px;
    padding: 0.38rem 0.9rem;
    font-size: 0.82rem;
    color: {C['text']};
    margin: 0.25rem;
    font-family: 'JetBrains Mono', monospace;
    transition: background 0.2s, transform 0.2s, border-color 0.2s;
    cursor: default;
}}
.skill-pill:hover {{
    background: {C['accent1']}22;
    border-color: {C['accent1']}66;
    transform: translateY(-2px);
    color: {C['accent2']};
}}
.skill-cat-title {{
    font-family: 'Syne', sans-serif;
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: {C['accent1']};
    margin-bottom: 0.5rem;
}}

/* ── Progress bars ── */
.progress-wrap {{ margin-bottom: 1rem; }}
.progress-label {{
    display: flex; justify-content: space-between;
    font-size: 0.88rem; color: {C['text']};
    margin-bottom: 0.4rem;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
}}
.progress-track {{
    height: 7px;
    background: {C['glass']};
    border-radius: 999px;
    overflow: hidden;
    border: 1px solid {C['border']};
}}
.progress-fill {{
    height: 100%;
    border-radius: 999px;
    background: {C['grad1']};
    animation: fadeInLeft 1s ease both;
}}

/* ── Project cards ── */
.project-card {{
    background: {C['card']};
    backdrop-filter: blur(20px);
    border: 1px solid {C['border']};
    border-radius: 20px;
    padding: 1.5rem;
    height: 100%;
    transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
    position: relative;
    overflow: hidden;
    animation: fadeInUp 0.7s ease both;
}}
.project-card::after {{
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: {C['grad1']};
    opacity: 0;
    transition: opacity 0.3s ease;
}}
.project-card:hover {{
    transform: translateY(-6px);
    box-shadow: 0 24px 70px rgba(108,99,255,0.22);
    border-color: {C['accent1']}55;
}}
.project-card:hover::after {{ opacity: 1; }}
.project-title {{
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: {C['text']};
    margin-bottom: 0.55rem;
    line-height: 1.35;
}}
.project-desc {{
    font-size: 0.9rem;
    color: {C['subtext']};
    line-height: 1.7;
    margin-bottom: 0.8rem;
}}
.project-impact {{
    font-size: 0.82rem;
    color: {C['accent3']};
    font-weight: 600;
    margin-bottom: 0.75rem;
    font-family: 'DM Sans', sans-serif;
}}
.tech-tag {{
    display: inline-block;
    background: {C['accent1']}18;
    border: 1px solid {C['accent1']}33;
    border-radius: 6px;
    padding: 0.2rem 0.55rem;
    font-size: 0.72rem;
    color: {C['accent2']};
    margin: 0.15rem;
    font-family: 'JetBrains Mono', monospace;
}}

/* ── Project filter buttons ── */
[data-testid="stMainBlockContainer"] .stButton > button {{
    background: {C['glass']} !important;
    color: {C['text']} !important;
    border: 1.5px solid {C['border']} !important;
    border-radius: 999px !important;
    padding: 0.5rem 1.4rem !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    font-family: 'DM Sans', sans-serif !important;
    transition: all 0.2s !important;
    box-shadow: none !important;
    letter-spacing: 0.02em !important;
    min-width: 80px !important;
}}
[data-testid="stMainBlockContainer"] .stButton > button:hover {{
    background: {C['accent1']}22 !important;
    border-color: {C['accent1']}66 !important;
    color: {C['text']} !important;
    transform: translateY(-1px) !important;
}}
[data-testid="stMainBlockContainer"] .stButton > button:focus:not(:active),
[data-testid="stMainBlockContainer"] .stButton > button:active {{
    background: linear-gradient(135deg,#7c74ff 0%,#38d9fa 100%) !important;
    color: #ffffff !important;
    border-color: transparent !important;
    box-shadow: 0 4px 16px {C['accent1']}55 !important;
}}

/* ── Timeline ── */
.timeline-role {{
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: {C['text']};
}}
.timeline-company {{
    font-size: 0.92rem;
    color: {C['accent2']};
    font-weight: 600;
    margin: 0.2rem 0;
}}
.timeline-period {{
    font-size: 0.8rem;
    color: {C['muted']};
    font-family: 'JetBrains Mono', monospace;
    margin-bottom: 0.7rem;
}}

/* ── Cert badge ── */
.cert-badge {{
    background: {C['card']};
    border: 1px solid {C['border']};
    border-radius: 14px;
    padding: 1rem 1.2rem;
    text-align: center;
    transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
    animation: fadeInUp 0.7s ease both;
}}
.cert-badge:hover {{
    transform: translateY(-4px);
    box-shadow: 0 12px 40px {C['accent1']}22;
    border-color: {C['accent1']}66;
}}
.cert-icon {{ font-size: 1.8rem; margin-bottom: 0.4rem; display: block; }}
.cert-name {{ font-size: 0.88rem; font-weight: 700; font-family: 'Syne', sans-serif; }}
.cert-issuer {{
    font-size: 0.75rem;
    color: {C['muted']};
    margin-top: 0.2rem;
    font-family: 'JetBrains Mono', monospace;
}}

/* ── Achievement card ── */
.achievement-card {{
    background: {C['card']};
    border: 1px solid {C['border']};
    border-radius: 16px;
    padding: 1.2rem 1.4rem;
    display: flex;
    align-items: center;
    gap: 1rem;
    transition: transform 0.2s, box-shadow 0.2s;
    animation: fadeInUp 0.7s ease both;
    margin-bottom: 0.75rem;
}}
.achievement-card:hover {{
    transform: translateX(6px);
    box-shadow: 0 8px 30px {C['accent1']}1a;
    border-color: {C['accent1']}44;
}}
.ach-icon {{ font-size: 1.8rem; flex-shrink: 0; }}
.ach-title {{ font-family: 'Syne', sans-serif; font-weight: 700; font-size: 1rem; color: {C['text']}; }}
.ach-sub {{ font-size: 0.85rem; color: {C['subtext']}; margin-top: 0.15rem; line-height: 1.6; }}

/* ── Contact links ── */
.contact-link {{
    display: flex; align-items: center; gap: 0.9rem;
    background: {C['glass']};
    border: 1px solid {C['border']};
    border-radius: 14px;
    padding: 1.05rem 1.4rem;
    color: {C['text']} !important;
    text-decoration: none !important;
    transition: background 0.2s, transform 0.2s, border-color 0.2s;
    font-size: 0.9rem;
    font-weight: 500;
    margin-bottom: 0.8rem;
}}
.contact-link:hover {{
    background: {C['accent1']}22;
    border-color: {C['accent1']}55;
    transform: translateX(5px);
}}
.contact-icon {{ font-size: 1.4rem; flex-shrink: 0; line-height: 1; }}

/* ── Sidebar nav ── */
.nav-logo {{
    font-family: 'Syne', sans-serif;
    font-size: 1.15rem;
    font-weight: 800;
    background: {C['grad1']};
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    padding: 1.5rem 1.2rem 0.5rem;
    display: block;
}}
.nav-sub {{
    font-size: 0.72rem;
    color: {C['muted']};
    padding: 0 1.2rem 1.2rem;
    font-family: 'JetBrains Mono', monospace;
    display: block;
    border-bottom: 1px solid {C['border']};
    margin-bottom: 0.8rem;
}}

/* ── Learning card ── */
.learning-card {{
    background: linear-gradient(135deg, {C['accent1']}12 0%, {C['accent2']}08 100%);
    border: 1px solid {C['accent1']}28;
    border-radius: 16px;
    padding: 1.2rem 1.4rem;
    margin-bottom: 0.6rem;
    transition: transform 0.2s;
    animation: fadeInUp 0.7s ease both;
}}
.learning-card:hover {{ transform: translateX(4px); }}

/* ── Footer ── */
.footer {{
    text-align: center;
    padding: 1.5rem;
    margin-top: 2rem;
    border-top: 1px solid {C['border']};
    color: {C['muted']};
    font-size: 0.82rem;
    font-family: 'JetBrains Mono', monospace;
}}

/* ── Sidebar buttons ── */
[data-testid="stSidebar"] .stButton > button {{
    background: transparent !important;
    color: {C['subtext']} !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.6rem 1rem !important;
    font-weight: 500 !important;
    font-size: 0.93rem !important;
    font-family: 'DM Sans', sans-serif !important;
    text-align: left !important;
    justify-content: flex-start !important;
    box-shadow: none !important;
    transition: background 0.18s, color 0.18s !important;
    width: 100% !important;
    margin: 1px 0 !important;
}}
[data-testid="stSidebar"] .stButton > button:hover {{
    background: {C['accent1']}20 !important;
    color: {C['text']} !important;
    transform: none !important;
    box-shadow: none !important;
}}
[data-testid="stSidebar"] .stButton > button:focus:not(:active) {{
    background: {C['accent1']}28 !important;
    color: {C['accent1']} !important;
    box-shadow: none !important;
    border-left: 3px solid {C['accent1']} !important;
    border-radius: 0 10px 10px 0 !important;
}}

.stTextInput > div > div > input,
.stTextArea > div > div > textarea {{
    background: {C['card']} !important;
    border: 1px solid {C['border']} !important;
    border-radius: 12px !important;
    color: {C['text']} !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.95rem !important;
}}
label[data-testid="stWidgetLabel"] {{
    color: {C['subtext']} !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.9rem !important;
}}
div[data-testid="stMetricValue"] {{
    color: {C['accent1']} !important;
    font-family: 'Syne', sans-serif !important;
}}
[data-testid="column"] {{ padding: 0 0.5rem; }}
.element-container {{ animation: fadeInUp 0.5s ease both; }}
.stMarkdown p {{
    color: {C['subtext']} !important;
    font-size: 0.98rem !important;
    line-height: 1.75 !important;
    font-family: 'DM Sans', sans-serif !important;
}}
</style>
""", unsafe_allow_html=True)


# ── Sidebar ───────────────────────────────────────────────────────────────────
def render_sidebar():
    with st.sidebar:
        st.markdown("""
        <span class="nav-logo">Priyanka Pal</span>
        <span class="nav-sub">Data Scientist · AI/ML Engineer</span>
        """, unsafe_allow_html=True)

        sections = [
            ("🏠", "Home"),
            ("👤", "About"),
            ("🛠️", "Technical Skills"),
            ("🚀", "Projects"),
            ("💼", "Experience"),
            ("📜", "Certifications & Achievements"),
            ("🎓", "Education & Currently Exploring"),
            ("📬", "Contact"),
        ]

        for icon, name in sections:
            if st.button(f"{icon}  {name}", key=f"nav_{name}", use_container_width=True):
                st.session_state.active_section = name
                st.rerun()

        st.markdown("---")
        is_dark = st.session_state.theme == "dark"
        if st.button(f"{'☀️  Light Mode' if is_dark else '🌙  Dark Mode'}", key="theme_toggle", use_container_width=True):
            st.session_state.theme = "light" if is_dark else "dark"
            st.rerun()


# ── Build resume button HTML ──────────────────────────────────────────────────
def render_resume_button():
    pdf_bytes = None
    for path in [
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "updatedResume.pdf"),
        os.path.join(os.getcwd(), "updatedResume.pdf"),
        "updatedResume.pdf",
    ]:
        if os.path.isfile(path):
            with open(path, "rb") as fh:
                pdf_bytes = fh.read()
            break

    if pdf_bytes:
        b64 = base64.b64encode(pdf_bytes).decode()

        # Build HTML using string concatenation — NO f-string for the JS block
        # This avoids {{ }} escaping issues that corrupt the onclick handler.
        html_top = """
        <style>
          @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@600&display=swap');
          * { box-sizing: border-box; margin: 0; padding: 0; }
          body { background: transparent; overflow: hidden; }
          .row {
            display: flex;
            gap: 0.75rem;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
            padding: 4px 0;
          }
          .btn {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 10px 22px;
            border-radius: 999px;
            font-weight: 600;
            font-size: 14px;
            font-family: 'DM Sans', sans-serif;
            letter-spacing: 0.4px;
            cursor: pointer;
            text-decoration: none;
            transition: opacity .2s, transform .2s, box-shadow .2s;
            white-space: nowrap;
          }
          .btn-primary {
            background: linear-gradient(135deg, #7c74ff 0%, #38d9fa 100%);
            color: #fff;
            border: none;
            box-shadow: 0 4px 20px rgba(124,116,255,.45);
          }
          .btn-primary:hover { opacity: .88; transform: translateY(-2px); }
          .btn-secondary {
            background: rgba(255,255,255,0.07);
            border: 1px solid rgba(130,140,255,0.28);
            color: #f0f0ff;
          }
          .btn-secondary {
            background: linear-gradient(135deg, #7c74ff 0%, #38d9fa 100%);
            color: #fff;
            border: none;
            box-shadow: 0 4px 20px rgba(124,116,255,.45);
          }
          .btn-secondary:hover { opacity: .88; transform: translateY(-2px); }
        </style>

        <div class="row">
          <button class="btn btn-primary" id="viewBtn">&#128196; View Resume
          </button>

          <a class="btn btn-secondary"
             href="https://github.com/priyanka297-tech" target="_blank">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57
                0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695
                -.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99
                .105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225
                -.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405
                c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225
                0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3
                0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/>
            </svg>
            GitHub
          </a>

          <a class="btn btn-secondary"
             href="https://www.linkedin.com/in/priyanka-pal-8a34171a8/" target="_blank">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="#128196">
              <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136
                1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85
                3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065
                2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771
                C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227
                24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
            </svg>
            LinkedIn
          </a>
        </div>

        <script>
          var PDF_B64 = '"""

        html_bottom = """';
          document.getElementById('viewBtn').addEventListener('click', function() {
            var binary = atob(PDF_B64);
            var bytes = new Uint8Array(binary.length);
            for (var i = 0; i < binary.length; i++) {
              bytes[i] = binary.charCodeAt(i);
            }
            var blob = new Blob([bytes], { type: 'application/pdf' });
            var url = URL.createObjectURL(blob);
            var newWin = window.open('', '_blank');
            if (newWin) {
              newWin.document.write(
                '<html><head><title>Resume - Priyanka Pal</title>' +
                '<style>*{margin:0;padding:0;}body{background:#1a1a2e;width:100%;height:100vh;overflow:hidden;}' +
                'iframe{width:100%;height:100vh;border:none;display:block;}</style></head>' +
                '<body><iframe src="' + url + '#toolbar=0&navpanes=0"></iframe></body></html>'
              );
              newWin.document.close();
            }
          });
        </script>
        """

        full_html = html_top + b64 + html_bottom
        components.html(full_html, height=60)

    else:
        st.warning("Resume PDF not found. Place `updatedResume.pdf` next to `app.py`.", icon="⚠️")

def section_hero():
    profile_b64 = get_base64_file("profile.png")
    if profile_b64:
        avatar_html = (
            '<div class="hero-avatar">'
            f'<img src="data:image/png;base64,{profile_b64}" alt="Priyanka Pal">'
            "</div>"
        )
    else:
        avatar_html = '<div class="hero-avatar-fallback">👩‍💻</div>'

    st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="hero-container">
      {avatar_html}
      <h1 class="hero-name">Hii.. I am Priyanka Pal</h1>
      <div class="hero-role">Data Analyst &nbsp;·&nbsp; Data Scientist &nbsp;·&nbsp; AI/ML Engineer</div>
      <div class="hero-tagline">
        Building intelligent systems that turn raw data into real-world impact —
        from ML pipelines to conversational AI and beyond.
      </div>
      <div style="margin-bottom:0.5rem;">
        <span class="hero-badge">🐍 Python</span>
        <span class="hero-badge">📈 Power BI</span>
        <span class="hero-badge">📊 Data Science</span>
        <span class="hero-badge">🤖 Machine Learning</span>
        <span class="hero-badge">💬 NLP</span>
        <span class="hero-badge">🔗 RAG Systems</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # All three buttons in ONE components.html — perfectly aligned
    render_resume_button()

    st.markdown("<br>", unsafe_allow_html=True)
    # ... rest of stats cards unchanged
    
    c1, c2, c3, c4 = st.columns(4)
    for col, icon, val, label in [
        (c1, "🚀", "10+", "Projects"),
        (c2, "🏆", "3+",  "Awards"),
        (c3, "📜", "5+",  "Certifications"),
        (c4, "⭐", "8.4", "CGPA"),
    ]:
        col.markdown(f"""
        <div class="glass-card" style="text-align:center; padding:1.2rem 1rem;">
          <div style="font-size:1.5rem; margin-bottom:0.2rem;">{icon}</div>
          <div style="font-family:'Syne',sans-serif; font-size:1.7rem; font-weight:800;
               background:{C['grad1']}; -webkit-background-clip:text; -webkit-text-fill-color:transparent;
               background-clip:text;">{val}</div>
          <div style="font-size:0.75rem; color:{C['muted']}; font-family:'JetBrains Mono',monospace;
               text-transform:uppercase; letter-spacing:0.08em;">{label}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

def section_about():
    st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)
    st.markdown(f"""
    <h2 class="section-title">About <span>Me</span></h2>
    <div class="section-divider"></div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2], gap="large")
    with col1:
        st.markdown(f"""
        <div class="glass-card">
          <p style="font-size:1rem; line-height:1.85; color:{C['text']}; margin-bottom:1.2rem;">
            Hi! I'm <strong style="color:{C['accent1']}">Priyanka Pal</strong>, a passionate Data Scientist and AI/ML Engineer
            based in Gurugram, Haryana. With a strong foundation in Computer Science and hands-on experience
            building end-to-end machine learning solutions, I thrive at the intersection of data and intelligence.
          </p>
          <p style="font-size:0.92rem; line-height:1.8; color:{C['subtext']}; margin-bottom:1.2rem;">
            My journey spans predictive analytics, NLP systems, RAG-powered assistants, and business intelligence
            dashboards. I believe great AI is not just technically sound — it solves real problems for real people.
            Every model I build, every pipeline I engineer, is driven by that philosophy.
          </p>
          <p style="font-size:0.92rem; line-height:1.8; color:{C['subtext']};">
            When I'm not training models, you'll find me exploring the latest in LLM research, contributing to
            open-source projects, or mentoring fellow learners in the AI/ML community.
          </p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        for icon, title, desc in [
            ("🧠", "Problem Solving",   "Translating complex business problems into elegant ML solutions"),
            ("⚙️", "ML Pipelines",      "End-to-end pipelines from data ingestion to model deployment"),
            ("🌍", "Real-world Impact", "Focused on applications that drive measurable business value"),
            ("📡", "Fast Learner",      "Rapidly adopting cutting-edge frameworks and techniques"),
        ]:
            st.markdown(f"""
            <div style="background:{C['glass']}; border:1px solid {C['border']}; border-radius:14px;
                 padding:0.9rem 1rem; margin-bottom:0.6rem;">
              <div style="display:flex; align-items:center; gap:0.7rem;">
                <span style="font-size:1.4rem;">{icon}</span>
                <div>
                  <div style="font-family:'Syne',sans-serif; font-weight:700; font-size:0.9rem;
                       color:{C['text']};">{title}</div>
                  <div style="font-size:0.78rem; color:{C['subtext']}; margin-top:0.1rem;">{desc}</div>
                </div>
              </div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def section_skills():
    st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)
    st.markdown(f"""
    <h2 class="section-title">Technical <span>Skills</span></h2>
    <div class="section-divider"></div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="glass-card" style="margin-bottom:1.4rem; text-align:center;">
      <div class="skill-cat-title" style="margin-bottom:0.8rem;">🏷️ Full Tech Stack</div>
      {"".join([f'<span class="skill-pill">{s}</span>' for s in [
        "Python","SQL","Pandas","NumPy","Feature Engineering","EDA","Scikit-learn","TensorFlow","Keras",
        "LSTM","GRU","NLP","RAG","LangChain","Streamlit","Power BI","Git","Jupyter","VS Code",
        "Matplotlib","Seaborn","FastAPI","Machine Learning","Deep Learning","OpenAI API",
        "FAISS","ChromaDB","BERT","XGBoost",
      ]])}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="font-family:'Syne',sans-serif; font-size:1rem; font-weight:700;
         color:{C['text']}; margin-bottom:0.8rem;">📊 Proficiency — Top 10 Skills</div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    left_skills  = [("Python", 92), ("Machine Learning", 88), ("NLP", 84), ("Power BI", 82), ("Deep Learning", 80), ("LangChain", 75)]

    for col, skills in [(col1, left_skills)]:
        with col:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            for skill, pct in skills:
                st.markdown(f"""
                <div class="progress-wrap">
                  <div class="progress-label">
                    <span style="color:{C['text']}">{skill}</span>
                    <span style="color:{C['accent1']}">{pct}%</span>
                  </div>
                  <div class="progress-track">
                    <div class="progress-fill" style="width:{pct}%;"></div>
                  </div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


def section_projects():
    st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)
    st.markdown(f"""
    <h2 class="section-title">Featured <span>Projects</span></h2>
    <div class="section-divider"></div>
    """, unsafe_allow_html=True)

    projects = [
        {"title": "Rossmann Sales Forecasting & AI Dashboard",
         "desc": "End-to-end time-series forecasting system predicting store-level sales for Rossmann pharmacies. Features an interactive Streamlit dashboard with AI-powered business recommendations.",
         "impact": "⚡ 94% forecast accuracy · Reduced inventory waste by ~18%",
         "tags": ["Python","EDA","Streamlit","Feature Engineering","LLM","Scikit-learn","LangChain","MistralAI"],
         "cat": "ML", "emoji": "📈"},
        {"title": "Customer Churn Prediction System",
         "desc": "ML classification pipeline predicting telecom customer churn with advanced feature engineering, SMOTE balancing, and a business-ready dashboard for retention teams.",
         "impact": "⚡ 92% AUC-ROC · Identified top 3 churn drivers",
         "tags": ["Python","XGBoost","Scikit-learn","SMOTE","EDA","Streamlit"],
         "cat": "ML", "emoji": "📉"},
        {"title": "Amazon Review Sentiment Analysis",
         "desc": "NLP pipeline performing multi-class sentiment classification on Amazon product reviews using transformer models with an interactive sentiment explorer UI.",
         "impact": "⚡ 91% accuracy · Real-time sentiment scoring dashboard",
         "tags": ["Python","NLP","Transformers","TF-IDF","Streamlit","LSTM","GRU"],
         "cat": "NLP", "emoji": "💬"},
        {"title": "Weather & News Intelligence Assistant",
         "desc": "RAG-powered conversational assistant combining real-time weather APIs and live news feeds with LLM reasoning to deliver context-aware, actionable intelligence.",
         "impact": "⚡ Sub-2s response · Multi-source RAG fusion",
         "tags": ["Python","RAG","LangChain","OpenAI API","Streamlit","MistralAI"],
         "cat": "RAG", "emoji": "🌤️"},
        {"title": "Movie Info Extractor (RAG System)",
         "desc": "Retrieval-Augmented Generation system that extracts structured movie information from unstructured text corpora, enabling natural language Q&A over large movie databases.",
         "impact": "⚡ 87% retrieval precision · Handles 10K+ movie corpus",
         "tags": ["Python","RAG","LangChain","FAISS","GPT","ChromaDB","Groq API"],
         "cat": "RAG", "emoji": "🎬"},
        {"title": "AI Story Generator (LLM + Groq)",
         "desc": "AI-powered storytelling application generating creative, context-aware stories using LLMs via Groq API with dynamic prompt engineering and an interactive Streamlit UI.",
         "impact": "⚡ Real-time generation · Context-aware narratives · Interactive UI",
         "tags": ["Python","LLM","Groq API","Streamlit","Prompt Engineering","NLP"],
         "cat": "NLP", "emoji": "📖"},
        {"title": "Next Word Prediction System (LSTM)",
         "desc": "Deep learning NLP model predicting the next word in a sequence using LSTM networks, with text preprocessing, tokenization, and a Streamlit interface.",
         "impact": "⚡ Sequence learning with LSTM · Real-time predictions · NLP pipeline",
         "tags": ["Python","LSTM","GRU","TensorFlow","Keras","NLP","Streamlit"],
         "cat": "NLP", "emoji": "🔮"},
    ]

    filters = ["All", "ML", "NLP", "RAG"]
    cols_f = st.columns(len(filters))
    for i, f in enumerate(filters):
        label = f"● {f}" if st.session_state.project_filter == f else f"○ {f}"
        if cols_f[i].button(label, key=f"filter_{f}", use_container_width=True):
            st.session_state.project_filter = f
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    visible = [p for p in projects
               if st.session_state.project_filter == "All" or p["cat"] == st.session_state.project_filter]

    cols = st.columns(2, gap="large")
    for i, proj in enumerate(visible):
        with cols[i % 2]:
            tags_html = "".join([f'<span class="tech-tag">{t}</span>' for t in proj["tags"]])
            st.markdown(f"""
            <div class="project-card">
              <div style="font-size:1.8rem; margin-bottom:0.4rem;">{proj['emoji']}</div>
              <div class="project-title">{proj['title']}</div>
              <div class="project-desc">{proj['desc']}</div>
              <div class="project-impact">{proj['impact']}</div>
              <div style="margin-bottom:0.8rem;">{tags_html}</div>
              <a class="btn-secondary" href="https://github.com/priyanka297-tech" target="_blank"
                 style="font-size:0.78rem; padding:0.32rem 0.9rem; display:inline-flex; align-items:center; gap:0.4rem;">
                {GH_LOGO_SM} GitHub
              </a>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


def section_experience():
    st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)
    st.markdown(f"""
    <h2 class="section-title">Work <span>Experience</span></h2>
    <div class="section-divider"></div>
    """, unsafe_allow_html=True)

    for exp in [
        {"role": "Applied AI Trainee", "company": "Edunet Foundation",
         "period": "Sep 2023 – Jan 2024", "emoji": "🤖",
         "bullets": ["Developed end-to-end AI/ML projects under mentorship of industry professionals",
                     "Built and deployed many AI applications using OpenAI",
                     "Contributed to curriculum development for AI training programs",
                     "Presented project demos and technical walkthroughs to evaluation panels"]},
        {"role": "iOS Developer Intern", "company": "SKLZTECT LLP",
         "period": "Mar 2024 – Dec 2025", "emoji": "📱",
         "bullets": ["Designed and developed user-facing iOS app features using Swift & Xcode",
                     "Collaborated with UI/UX team to implement pixel-perfect interface designs",
                     "Analyzed user interaction data using Python to identify behavioral patterns",
                     "Participated in code reviews and agile sprint planning sessions"]},
    ]:
        st.markdown(f"""
        <div class="glass-card" style="margin-bottom:1.2rem;">
          <div style="display:flex; align-items:flex-start; gap:1.2rem;">
            <div style="font-size:2.2rem; flex-shrink:0;">{exp['emoji']}</div>
            <div style="flex:1;">
              <div class="timeline-role">{exp['role']}</div>
              <div class="timeline-company">{exp['company']}</div>
              <div class="timeline-period">📅 {exp['period']}</div>
              <ul style="padding-left:1.2rem; margin-top:0.5rem;">
                {"".join([f'<li style="font-size:0.87rem;color:{C["subtext"]};line-height:1.7;margin-bottom:0.3rem;">{b}</li>' for b in exp['bullets']])}
              </ul>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def section_education_and_learning():
    st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)
    st.markdown(f"""
    <h2 class="section-title">🎓 Education & <span>Currently Exploring</span></h2>
    <div class="section-divider"></div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="glass-card" style="margin-bottom:1.5rem;">
      <div style="display:flex; align-items:flex-start; gap:1.4rem;">
        <div style="font-size:2.6rem; line-height:1; padding-top:0.05rem; flex-shrink:0;">🏛️</div>
        <div style="flex:1; min-width:0;">
          <div style="font-family:'Syne',sans-serif; font-size:1.22rem; font-weight:800;
               color:{C['text']}; line-height:1.3; margin-bottom:0.28rem;">
            B.Tech — Computer Science &amp; Engineering
          </div>
          <div style="font-size:0.97rem; color:{C['accent1']}; font-weight:600; margin-bottom:0.25rem;">
            World College of Technology &amp; Management
          </div>
          <div style="font-size:0.79rem; color:{C['muted']}; font-family:'JetBrains Mono',monospace; margin-bottom:0.85rem;">
            📅 2020 — 2024 &nbsp;·&nbsp; 📍 Haryana, India
          </div>
          <div style="display:inline-flex; align-items:center; gap:0.55rem;
               background:{C['glass']}; border:1px solid {C['border']}; border-radius:12px;
               padding:0.45rem 1rem;">
            <span style="font-family:'Syne',sans-serif; font-size:1.5rem; font-weight:800;
                 background:{C['grad1']}; -webkit-background-clip:text; -webkit-text-fill-color:transparent;
                 background-clip:text; line-height:1;">8.4</span>
            <span style="font-size:0.7rem; color:{C['muted']}; text-transform:uppercase;
                 letter-spacing:0.1em; font-family:'JetBrains Mono',monospace; line-height:1.3;">CGPA</span>
          </div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="font-family:'Syne',sans-serif; font-size:1.05rem; font-weight:700;
         color:{C['text']}; margin-bottom:0.8rem;">📚 Currently Learning</div>
    """, unsafe_allow_html=True)

    for icon, title, desc in [
        ("🦙", "Large Language Models & Fine-tuning",
         "Exploring LoRA/QLoRA fine-tuning strategies on open-source LLMs like LLaMA & Mistral for domain-specific applications."),
        ("🔗", "Advanced RAG Architectures",
         "Studying agentic RAG, multi-hop retrieval, and re-ranking strategies for production-grade AI assistants."),
        ("☁️", "MLOps & Cloud Deployment",
         "Learning AWS SageMaker, MLflow experiment tracking, and CI/CD pipelines for ML models."),
        ("📐", "Graph Neural Networks",
         "Exploring GNNs for recommendation systems and knowledge graph applications."),
    ]:
        st.markdown(f"""
        <div class="learning-card">
          <div style="display:flex; align-items:flex-start; gap:0.8rem;">
            <span style="font-size:1.5rem; flex-shrink:0;">{icon}</span>
            <div>
              <div style="font-family:'Syne',sans-serif; font-weight:700; font-size:0.95rem;
                   color:{C['text']};">{title}</div>
              <div style="font-size:0.83rem; color:{C['subtext']}; margin-top:0.2rem; line-height:1.6;">{desc}</div>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def section_certs_and_achievements():
    st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)
    st.markdown(f"""
    <h2 class="section-title">📜 Certifications & <span>Achievements</span></h2>
    <div class="section-divider"></div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="font-family:'Syne',sans-serif; font-size:1.05rem; font-weight:700;
         color:{C['text']}; margin-bottom:0.8rem;">🎓 Certifications</div>
    """, unsafe_allow_html=True)

    certs = [
        ("🎓", "Data Science",   "Ducat Institute",   "#6c63ff"),
        ("🔵", "IBM Data Tools", "IBM / Coursera",    "#0099cc"),
        ("🧠", "ML Workshop",    "Intel Corporation", "#00d4ff"),
        ("📊", "Power BI",       "Microsoft",         "#ff6b9d"),
        ("🤖", "AI Program",     "Edunet Foundation", "#00ffa3"),
    ]
    cols = st.columns(len(certs))
    for col, (icon, name, issuer, color) in zip(cols, certs):
        col.markdown(f"""
        <div class="cert-badge">
          <span class="cert-icon">{icon}</span>
          <div class="cert-name" style="color:{color}">{name}</div>
          <div class="cert-issuer">{issuer}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="font-family:'Syne',sans-serif; font-size:1.05rem; font-weight:700;
         color:{C['text']}; margin-bottom:0.8rem; margin-top:1.8rem;">🏆 Achievements</div>
    """, unsafe_allow_html=True)

    for icon, title, sub in [
        ("🏆", "Hackathon Winner",          "1st place in a national-level hackathon — built an AI-powered solution under 24 hrs"),
        ("🇮🇳", "Smart India Hackathon 2025", "Selected participant in SIH 2025 — one of India's largest innovation challenges"),
        ("🔬", "Intel Unnati Nomination",    "Nominated for Intel Unnati Industrial Training Program for outstanding AI project work"),
        ("🎓", "DLF Scholarship",            "Recipient of DLF Scholarship for academic excellence throughout B.Tech program"),
    ]:
        st.markdown(f"""
        <div class="achievement-card">
          <span class="ach-icon">{icon}</span>
          <div>
            <div class="ach-title">{title}</div>
            <div class="ach-sub">{sub}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def section_contact():
    st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)
    st.markdown(f"""
    <h2 class="section-title">📬 Get In <span>Touch</span></h2>
    <div class="section-divider"></div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(f"""
        <div class="glass-card" style="height:100%;">
          <div style="font-family:'Syne',sans-serif; font-size:1.3rem; font-weight:800;
               color:{C['text']}; margin-bottom:0.6rem;">Let's connect! 🤝</div>
          <p style="font-size:0.93rem; color:{C['subtext']}; line-height:1.8; margin-bottom:1.5rem;">
            I'm actively looking for opportunities in Data Science, AI/ML Engineering,
            and Data Analytics. Whether you have a role, a project, or just want to talk AI —
            my inbox is always open.
          </p>
          <a class="contact-link" href="mailto:priyankapal29702@gmail.com">
            <span class="contact-icon">📧</span>
            <div>
              <div style="font-weight:700; color:{C['text']}; font-size:0.95rem;">Email</div>
              <div style="font-size:0.8rem; color:{C['muted']};">priyankapal29702@gmail.com</div>
            </div>
          </a>
          <a class="contact-link" href="tel:+917428654147">
            <span class="contact-icon">📞</span>
            <div>
              <div style="font-weight:700; color:{C['text']}; font-size:0.95rem;">Phone</div>
              <div style="font-size:0.8rem; color:{C['muted']};">+91 7428654147</div>
            </div>
          </a>
          <div style="margin-top:0.5rem; display:flex; align-items:center; gap:0.6rem;">
            <span style="width:9px; height:9px; border-radius:50%; background:#00ffa3;
                 display:inline-block; flex-shrink:0;"></span>
            <span style="font-size:0.8rem; color:{C['muted']}; font-family:'JetBrains Mono',monospace;">
              Open to remote &amp; hybrid opportunities
            </span>
          </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="glass-card" style="height:100%;">
          <div style="font-family:'Syne',sans-serif; font-size:1.3rem; font-weight:800;
               color:{C['text']}; margin-bottom:0.6rem;">Find me online 🌐</div>
          <p style="font-size:0.93rem; color:{C['subtext']}; line-height:1.8; margin-bottom:1.5rem;">
            Connect with me on LinkedIn for professional networking, or explore my projects
            on GitHub. Always open to collaborating on interesting AI challenges.
          </p>
          <a class="contact-link" href="https://www.linkedin.com/in/priyanka-pal-8a34171a8/" target="_blank">
            <span class="contact-icon">{LI_LOGO_CONTACT}</span>
            <div>
              <div style="font-weight:700; color:{C['text']}; font-size:0.95rem;">LinkedIn</div>
              <div style="font-size:0.8rem; color:{C['muted']};">priyanka-pal-8a34171a8</div>
            </div>
          </a>
          <a class="contact-link" href="https://github.com/priyanka297-tech" target="_blank">
            <span class="contact-icon" style="color:{C['text']};">{GH_LOGO_CONTACT}</span>
            <div>
              <div style="font-weight:700; color:{C['text']}; font-size:0.95rem;">GitHub</div>
              <div style="font-size:0.8rem; color:{C['muted']};">priyanka297-tech</div>
            </div>
          </a>
          <div style="margin-top:0.6rem; padding:0.8rem 1rem;
               background:{C['glass']}; border:1px solid {C['border']}; border-radius:12px;
               display:flex; align-items:center; gap:0.6rem;">
            <span style="font-size:1rem;">📍</span>
            <span style="font-size:0.8rem; color:{C['muted']}; font-family:'JetBrains Mono',monospace;">
              Gurugram, Haryana, India
            </span>
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


def render_footer():
    st.markdown(f"""
    <div class="footer">
      <div style="margin-bottom:0.4rem;">
        <span style="background:{C['grad1']}; -webkit-background-clip:text;
             -webkit-text-fill-color:transparent; background-clip:text;
             font-family:'Syne',sans-serif; font-size:1rem; font-weight:700;">
          ✦ Priyanka Pal
        </span>
      </div>
      <div>Data Scientist · AI/ML Engineer · Gurugram, India</div>
      <div style="margin-top:0.4rem; font-size:0.75rem;">
        Built with ❤️ using Python &amp; Streamlit &nbsp;·&nbsp; © 2025 Priyanka Pal
      </div>
    </div>
    """, unsafe_allow_html=True)


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    inject_css()
    render_sidebar()

    with st.container():
        section = st.session_state.active_section

        if section == "Home":
            section_hero()
        elif section == "About":
            section_about()
        elif section == "Technical Skills":
            section_skills()
        elif section == "Projects":
            section_projects()
        elif section == "Experience":
            section_experience()
        elif section == "Education & Currently Exploring":
            section_education_and_learning()
        elif section == "Certifications & Achievements":
            section_certs_and_achievements()
        elif section == "Contact":
            section_contact()

        render_footer()


if __name__ == "__main__":
    main()