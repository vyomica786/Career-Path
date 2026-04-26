#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import pickle
import sys
import os



# In[4]:


sys.path.append(r"D:\Career Path")

from utils import get_skill_gap, get_recommendations

# Load model
model = pickle.load(open(r"D:\Career Path\model.pkl", "rb"))
vectorizer = pickle.load(open(r"D:\Career Path\vectorizer.pkl", "rb"))



# In[5]:


st.title("💼 AI Career Predictor & Skill Gap Analyzer")

st.write("Enter your skills (comma separated):")

user_input = st.text_input("Example: python, sql, excel")

if st.button("Predict Career"):

    if user_input:
        # Preprocess input
        input_data = vectorizer.transform([user_input])

        # Prediction
        prediction = model.predict(input_data)[0]
        confidence = model.predict_proba(input_data).max()

        st.success(f"🎯 Predicted Role: {prediction}")
        st.info(f"📊 Confidence Score: {confidence:.2f}")

        # Skill gap
        missing_skills = get_skill_gap(user_input, prediction)

        if missing_skills:
            st.warning("⚠️ Missing Skills:")
            for skill in missing_skills:
                st.write(f"- {skill}")
        else:
            st.success("✅ You have all required skills!")

        # Recommendations
        recs = get_recommendations(missing_skills)

        if recs:
            st.subheader("📚 Recommendations:")
            for r in recs:
                st.write(f"- {r}")

    else:
        st.error("Please enter your skills!")


# In[ ]:




