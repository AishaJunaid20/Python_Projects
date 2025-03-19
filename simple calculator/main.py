import streamlit as st

# Streamlit App Title
st.title("🧮 Simple Calculator")

# User Inputs
num1 = st.number_input("Enter first number", value=0.0, step=1.0)
num2 = st.number_input("Enter second number", value=0.0, step=1.0)

# Operation Selection
operation = st.selectbox("Choose an operation", ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"])

# Perform Calculation
result = None
if st.button("Calculate"):
    if operation == "Addition (+)":
        result = num1 + num2
    elif operation == "Subtraction (-)":
        result = num1 - num2
    elif operation == "Multiplication (×)":
        result = num1 * num2
    elif operation == "Division (÷)":
        if num2 == 0:
            st.error("❌ Cannot divide by zero!")
        else:
            result = num1 / num2

    # Display Result
    if result is not None:
        st.success(f"✅ Result: {result}")

