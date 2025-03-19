import streamlit as st
import random

# List of Growth Mindset Challenges
challenges = [
    "Learn something new about a topic that challenges you.",
    "Turn a mistake into a learning opportunity today.",
    "Give constructive feedback to someone and ask for some in return.",
    "Set a small goal for yourself and accomplish it by the end of the day.",
    "Spend 10 minutes practicing a skill you find difficult.",
    "Read about a successful person who overcame challenges through persistence.",
    "Step out of your comfort zone and try something new today.",
    "Reframe a negative thought into a positive one.",
    "Write down three things you learned this week and how they helped you grow."
]

# Function to get a random challenge
def get_random_challenge():
    return random.choice(challenges)

# Streamlit UI
st.title("🌱 Growth Mindset Challenge")
st.subheader("Develop a growth mindset by taking on daily challenges!")

if st.button("Get a Challenge 🎯"):
    challenge = get_random_challenge()
    st.write(f"### ✨ Your Challenge: \n➡️ **{challenge}**")

    if st.button("Accept Challenge ✅"):
        with open("challenges.txt", "a") as file:
            file.write(challenge + "\n")
        st.success("✅ Challenge Accepted! Keep growing! 💪")
