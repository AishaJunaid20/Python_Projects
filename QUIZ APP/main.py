import streamlit as st
import time

# Quiz questions with options and correct answers
questions = [
    {"question": "What is the output of 2 ** 3 in Python?", "options": ["6", "8", "9", "10"], "answer": "8"},
    {"question": "Which keyword is used to define a function in Python?", "options": ["func", "define", "def", "lambda"], "answer": "def"},
    {"question": "What does the 'len()' function return?", "options": ["Size of memory", "Length of an object", "Number of elements", "None"], "answer": "Length of an object"},
    {"question": "Which module in Python is used for regular expressions?", "options": ["regex", "re", "reg", "rex"], "answer": "re"},
    {"question": "What is the correct file extension for Python files?", "options": [".py", ".python", ".pyt", ".px"], "answer": ".py"},
    {"question": "Which keyword is used to create a loop that repeats a block of code?", "options": ["while", "repeat", "for", "loop"], "answer": "for"},
    {"question": "Which function is used to read user input in Python?", "options": ["get_input", "read", "input", "scan"], "answer": "input"},
    {"question": "What is the output of 10 // 3?", "options": ["3.33", "3", "4", "10"], "answer": "3"},
    {"question": "Which data type is immutable in Python?", "options": ["List", "Dictionary", "Tuple", "Set"], "answer": "Tuple"},
    {"question": "What is the default return value of a function that does not return anything?", "options": ["0", "None", "Empty String", "Undefined"], "answer": "None"}
]

st.set_page_config(page_title="Python MCQ Quiz", page_icon="🐍", layout="centered")
st.markdown("""
    <style>
        .title { text-align: center; font-size: 36px; font-weight: bold; }
        .footer { text-align: center; margin-top: 20px; font-size: 14px; color: gray; }
        .options-container { display: flex; justify-content: center; }
        .stRadio > div { display: flex; flex-direction: row; gap: 20px; }
        .result-box { text-align: center; padding: 10px; margin-top: 10px; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>Python Quiz App 🐍</div>", unsafe_allow_html=True)

# Session state for question index, score, and timer
if 'q_index' not in st.session_state:
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.start_time = time.time()
    st.session_state.timer_running = True

TIME_LIMIT = 20  # 20 seconds per question
remaining_time = TIME_LIMIT - (time.time() - st.session_state.start_time)

if remaining_time <= 0:
    st.session_state.q_index += 1
    st.session_state.start_time = time.time()
    remaining_time = TIME_LIMIT
    st.session_state.timer_running = True
    st.rerun()

if st.session_state.q_index < len(questions):
    q_data = questions[st.session_state.q_index]
    st.subheader(f"Question {st.session_state.q_index + 1}: {q_data['question']}")
    
    col1, col2 = st.columns([2, 3])
    with col1:
        st.write(f"⏳ Time Remaining: **{int(remaining_time)} seconds**")
    with col2:
        selected_option = st.radio("Select an option:", q_data['options'], key=f"q_{st.session_state.q_index}")
    
    if st.button("Submit"):
        if selected_option == q_data['answer']:
            st.session_state.score += 2
            st.markdown("<div class='result-box' style='background-color: lightgreen; color: black;'>✅ Correct!</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='result-box' style='background-color: lightcoral; color: white;'>❌ Wrong! The correct answer is: {q_data['answer']}</div>", unsafe_allow_html=True)
        
        time.sleep(1.5)  # Short delay before moving to next question
        st.session_state.q_index += 1
        st.session_state.start_time = time.time()
        st.session_state.timer_running = True
        st.rerun()
else:
    st.subheader("🎉 Quiz Completed!")
    st.write(f"Your Final Score: **{st.session_state.score} / 20**")
    if st.button("Restart Quiz"):
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.session_state.start_time = time.time()
        st.session_state.timer_running = True
        st.rerun()

st.markdown("<div class='footer'>Developed with ❤️ using Streamlit</div>", unsafe_allow_html=True)

