import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
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
        return "🟢 Strong Password ✅", "Your password is strong! 💪", 100
    elif strength == 3:
        return "🟡 Medium Password ⚠️", "Almost there! Add more complexity.", 70
    elif strength == 2:
        return "🟠 Weak Password ❌", "Password is weak. Try adding more complexity.", 40
    else:
        return "🔴 Very Weak Password ❌", "\n".join(feedback), 10

# Streamlit UI
st.title("🔐 Advanced Password Strength Meter")
st.subheader("Check the strength of your password in real-time!")

if password:
    strength_label, feedback, strength_score = check_password_strength(password)
    
    # Display Strength Label
    st.markdown(f"### {strength_label}")

    # Strength Bar
    st.progress(strength_score / 100)

    # Feedback for Improvement
    st.write(feedback)

