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

# Initialize session state for challenge and accepted status
if "challenge" not in st.session_state:
    st.session_state.challenge = None
if "accepted" not in st.session_state:
    st.session_state.accepted = False

# Streamlit UI
st.title("🌱 Growth Mindset Challenge")
st.subheader("Develop a growth mindset by taking on daily challenges!")

# Button to get a new challenge
if st.button("Get a Challenge 🎯"):
    st.session_state.challenge = random.choice(challenges)
    st.session_state.accepted = False  # Reset accepted status

# Show challenge if selected
if st.session_state.challenge:
    st.write(f"### ✨ Your Challenge: \n➡️ **{st.session_state.challenge}**")

    # Accept Challenge button
    if st.button("Accept Challenge ✅"):
        with open("challenges.txt", "a") as file:
            file.write(st.session_state.challenge + "\n")
        st.session_state.accepted = True  # Store acceptance status

# Show confirmation after accepting
if st.session_state.accepted:
    st.success("✅ Challenge Accepted! Keep growing! 💪")
