import pandas as pd

def load_skills(path="data/skills.csv"):
    df = pd.read_csv(path)
    return set(df['skill'].str.lower())

def skill_gap(resume_text, jd_text, skills_set):
    resume_words = set(resume_text.split())
    jd_words = set(jd_text.split())
    
    resume_skills = resume_words.intersection(skills_set)
    jd_skills = jd_words.intersection(skills_set)
    
    missing = jd_skills - resume_skills
    
    return list(missing)
