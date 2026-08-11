import streamlit as st
from config.app_config import PRIMARY_COLOR
import requests


def get_github_stars():
    try:
        response = requests.get(
            "https://api.github.com/repos/nidhidhameliya/HIA-Health-Insights-Agent"
        )
        if response.status_code == 200:
            return response.json()["stargazers_count"]
        return None
    except Exception:
        return None


def show_footer(in_sidebar=False):

    @st.cache_data(ttl=3600)
    def get_cached_stars():
        return get_github_stars()

    stars_count = get_cached_stars()
    github_url = "https://github.com/nidhidhameliya/HIA-Health-Insights-Agent"
    star_text = f" ⭐ {stars_count}" if stars_count is not None else ""

    footer_style = f"""
        text-align: center;
        padding: 0.7rem 0.75rem;
        margin-top: {'0' if in_sidebar else '2rem'};
        border-top: 1px solid rgba(100, 181, 246, 0.15);
        background: rgba(25, 118, 210, 0.02);
        color: #64B5F6;
        font-size: 0.75rem;
        line-height: 1.5;
    """

    st.markdown(
        f"""
        <div style='{footer_style}'>
            <span style='display:inline-flex; align-items:center; justify-content:center; gap:6px; flex-wrap:wrap; color:#64B5F6;'>
                Built with ❤️ for HIA
                <a href='{github_url}' target='_blank' style='color:#64B5F6; text-decoration:none; font-weight:600;'>
                    GitHub{star_text}
                </a>
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )