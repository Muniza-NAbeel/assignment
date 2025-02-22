#streamlit
import streamlit as st

st.set_page_config(page_title= "growth mindset challenge", project_icon="🌈")

st.title("Growth Mindset Challenge")

st.header("🚀 Welcome to Your Growth Journey!")
st.write("Embrace challenges,learn from mistakes, and unlock your full potential. This AL-powered app helps you build a growth mindset with reflection, challenges, and achievements! 🌟 ")

#quote section

st.header("💡 Today's Growth Mindset Quote")
st.write('"A comfort zone is a beautiful place, but nothing ever grows there." – Unknown')

st.header("🤔 What's Your Challenge Today??")
user_input = st.text_input("Describe a challenge you're facing:")

#condition

if user_input: 
    st.success(f"🎯 You're facing: {user_input}. Aim high, stay focused, and never give up! 🚀")
else:
    st.warning("Tell us about your challenge to get started!")

#reflexing
st.header("✍️ Reflect on Your Learning")
reflection = st.text_area("Write your reflections here")

if reflection:
    st.success(f"🌱 Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experience help your to grow! Share your difficulities")

#acheivements
st.header("Celebrate Your Wins!")
acheivement = st.text_input("Share something you're recently accomplished:")

if acheivement:
    st.success(f" Amazing! You achieved: {acheivement}")
else:
    st.info("Big or small , every acheivement counts! Share one now!")


#footer
st.write("- - -")
st.write("©2025 Streamlit App. All Rights Reserved. Made By Muniza Nabeel")

