"""
Streamlit app for the LinkedIn Post Generator (AI Trend Radar Crew).
Run from project root: uv run streamlit run app.py
"""

import os
import sys


_root = os.path.dirname(os.path.abspath(__file__))
_src = os.path.join(_root, "src")
if _src not in sys.path:
    sys.path.insert(0, _src)

import streamlit as st
from dotenv import load_dotenv

load_dotenv()
os.makedirs("Output", exist_ok=True)


from linkedin_post_generator.crew import AITrendRadarCrew


def generate_post(focus_area: str) -> str:
    """Run the crew and return the generated LinkedIn post."""
    crew_instance = AITrendRadarCrew()
    result = crew_instance.crew().kickoff(inputs={"focus_area": focus_area})
    return str(result)

def main():
    st.set_page_config(
        page_title="LinkedIn Post Generator",
        page_icon="📢",
        layout="centered",
    )

    st.title("📢 LinkedIn Post Generator")
    st.caption("AI Trend Radar → ready-to-publish LinkedIn posts")

    focus_area = st.text_area(
        "Focus area",
        value="Latest AI trends in LLMs, startups, and AI regulation",
        height=100,
        help="Describe the AI/tech focus for trend research and the post.",
        placeholder="e.g. AI agents, enterprise AI, or AI regulation in the EU",
    ).strip()

    if not focus_area:
        st.warning("Please enter a focus area.")
        st.stop()

    if st.button("Generate LinkedIn post", type="primary", use_container_width=True):
        with st.spinner("Researching trends and writing your post…"):
            try:
                result = generate_post(focus_area)
                st.success("Post generated.")
                st.divider()
                st.subheader("Generated post")
                st.markdown(result)
                st.divider()
                # Save to file for consistency with CLI
                out_path = "Output/linkedin_post.md"
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(result)
                st.caption(f"Saved to `{out_path}`")
            except Exception as e:
                st.error(f"Generation failed: {e}")
                if st.checkbox("Show full error"):
                    st.exception(e)


if __name__ == "__main__":
    main()
