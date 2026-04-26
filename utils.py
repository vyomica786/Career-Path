#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Required skills for each role
job_skills = {
    "Data Analyst": ["python", "sql", "excel", "powerbi", "statistics"],
    "Frontend Developer": ["html", "css", "javascript", "react"],
    "ML Engineer": ["python", "machine learning", "tensorflow", "deep learning"],
    "Backend Developer": ["java", "spring", "sql"]
}

# Recommendations
recommendations = {
    "python": "Practice Python projects on data handling",
    "sql": "Learn joins, queries, and database design",
    "excel": "Master formulas, pivot tables",
    "powerbi": "Build dashboards and reports",
    "statistics": "Learn probability & hypothesis testing",
    "react": "Build frontend projects using React",
    "tensorflow": "Work on deep learning models",
}

def get_skill_gap(user_skills, predicted_role):
    required = job_skills.get(predicted_role, [])
    user_skills = user_skills.lower().split()

    missing = [skill for skill in required if skill not in user_skills]
    return missing


def get_recommendations(missing_skills):
    recs = []
    for skill in missing_skills:
        if skill in recommendations:
            recs.append(f"{skill}: {recommendations[skill]}")
    return recs


# In[2]:


job_skills


# In[3]:


recommendations

