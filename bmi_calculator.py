import streamlit as st

# BMI Calculation Function
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

# Streamlit Web App
st.title("BMI Calculator")
st.write("Enter your details below:")

# User Inputs for BMI Calculation
weight = st.number_input("Enter your weight (kg):", min_value=1.0, value=60.0, step=0.1)
height = st.number_input("Enter your height (m):", min_value=0.5, value=1.75, step=0.01)

# Calculate BMI
if weight and height:
    bmi = calculate_bmi(weight, height)
    st.write(f"Your BMI is: {bmi}")

    # BMI Category
    if bmi < 18.5:
        st.write("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.write("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.write("You are overweight.")
    else:
        st.write("You are obese.")
