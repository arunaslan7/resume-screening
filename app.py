import streamlit as st
from utils.parser import extract_text_from_pdf
from utils.preprocess import clean_text
from utils.model import match_score
# from utils.model import bert_score  # optional
from utils.skills import load_skills, skill_gap

st.set_page_config(page_title="Resume Screening System")

st.title("📄 Smart Resume Screening System")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd_text = st.text_area("Paste Job Description")

if "skills" not in st.session_state:
    st.session_state.skills = load_skills()

if st.button("Analyze"):
    if resume_file and jd_text:
        with st.spinner("Processing..."):
            
            resume_text = extract_text_from_pdf(resume_file)
            
            resume_clean = clean_text(resume_text)
            jd_clean = clean_text(jd_text)
            
            score = match_score(resume_clean, jd_clean)
            # score = bert_score(resume_clean, jd_clean)  # upgrade
            
            gaps = skill_gap(resume_clean, jd_clean, st.session_state.skills)
            
            st.success(f"Match Score: {score}%")
            
            st.subheader("❌ Missing Skills")
            if gaps:
                st.write(gaps)
            else:
                st.write("No major skill gaps 🎉")
    else:
        st.warning("Please upload resume and enter job description")
