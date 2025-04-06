import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Website Title
st.title("🌟 My First Streamlit Website 🌟")

# Website Header
st.header("👋 Welcome to the Streamlit Website! 👋")

# Website Description
st.write("""
    This is a simple Streamlit website that showcases how to build a web app in Python. 
    You can add many elements like charts, maps, forms, and more! 🎉
""")

# Example of Input Widgets
name = st.text_input("What's your name? 🤔")
if name:
    st.write(f"Hello, {name}! 😊")

# Example of a Button
if st.button('Say Hello 👋'):
    st.write("Hello, Welcome to Streamlit! 🚀")

# Example of Displaying a Plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
st.pyplot(plt)

# Displaying a fun message
st.write("Thanks for visiting! 😎")
