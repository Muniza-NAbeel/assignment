#streamlit
import streamlit as st
import random

st.set_page_config(page_title= "growth mindset challenge", page_icon="🌈")

st.title("✨ Growth Mindset Challenge 🌱")

st.header("🚀 Welcome to Your Growth Journey!")
st.write("Embrace challenges,learn from mistakes, and unlock your full potential. This AL-powered app helps you build a growth mindset with reflection, challenges, and achievements! 🌟 ")

# List of Growth Mindset Quotes
quotes = [
    "Mistakes are proof that you are trying.",
    "A comfort zone is a beautiful place, but nothing ever grows there.",
    "Every day is a new beginning. Take a deep breath, smile, and start again.",
    "Push yourself, because no one else is going to do it for you.",
    "Growth begins at the end of your comfort zone.",
    "The best way to predict your future is to create it.",
    "Dream big, work hard, and stay consistent.",
    "Believe you can, and you're halfway there.",
]

# Select a Random Quote
selected_quote = random.choice(quotes)

# Display Quotes Section
st.markdown("## 💡 **Today's Growth Mindset Quotes**")
st.write("Here are some motivational quotes to inspire you on your growth journey:")

# Display All Quotes (Highlight the Random One)
for quote in quotes:
    if quote == selected_quote:
        st.header(f"🌟 **{quote}**")  
    else:
        st.write(f"- {quote}")  




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
    st.info("💭 Reflecting on past experiences helps you to grow! 🌱 Share your difficulties.")

# Achievements Section
st.header("🎉 Celebrate Your Wins!")
achievement = st.text_input("✨ Share something you've recently accomplished:")

if achievement: 
    st.success(f"🏆 Amazing! You achieved: {achievement} 🎊 Keep going!")
else: 
    st.info("🌟 Big or small, every achievement counts! 💬 Share one now!")

# Footer
st.write("- - -")
st.write("©2025 Streamlit App. All Rights Reserved. 🚀 Made By **Muniza Nabeel** ✨")
