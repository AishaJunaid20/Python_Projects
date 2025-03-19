import streamlit as st
import re

def check_password_strength(password):
    """Returns a score based on password strength"""
    strength = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("🔴 Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("🟠 Use both uppercase and lowercase letters.")

    # Numbers Check
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("🟠 Add at least one number (0-9).")

    # Special Characters Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("🟠 Include a special character (!@#$%^&*).")

    # Determine Strength Level
    if strength == 4:
        return "🟢 Strong Password ✅", "Your password is strong! 💪"
    elif strength == 3:
        return "🟡 Medium Password ⚠️", "Almost there! Add more complexity."
    else:
        return "🔴 Weak Password ❌", "\n".join(feedback)

# Streamlit UI
st.title("🔐 Password Strength Meter")
st.subheader("Check how strong your password is!")

password = st.text_input("Enter your password:", type="password")

if password:
    strength_label, feedback = check_password_strength(password)
    st.markdown(f"### {strength_label}")
    st.write(feedback)
