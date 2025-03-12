


import time
import streamlit as st
import random

# Custom CSS for teal gradient background & white text
custom_css = """
    <style>
        body {
            background: linear-gradient(135deg, #004d40, #26a69a);
            color: black;
        }
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #004d40, #26a69a);
            color: black;
        }
        [data-testid="stHeader"] {
            background: rgba(0, 0, 0, 0);  /* Transparent header */
        }
        [data-testid="stSidebar"] {
            background: linear-gradient(135deg, #00332E, #1E888A);
            color: black;
        }
        h1, h2, h3, h4, h5, h6, p, label {
            color: black !important;
        }



    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

st.title("📔 Quiz Application")

questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Karachi", "Lahore", "Islamabad", "Peshawar"],
        "answer": "Islamabad"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Saturn", "Jupiter", "Mars"],
        "answer": "Jupiter"
    },
    {
        "question": "What is the smallest country in the world?",
        "options": ["Vatican City", "Monaco", "Nauru", "Tuvalu"],
        "answer": "Vatican City"
    },
    {
        "question": "What is the largest living species of lizard?",
        "options": ["Komodo dragon", "Saltwater crocodile", "Black mamba", "Green mamba"],
        "answer": "Komodo dragon"
    },
    {
        "question": "What is the currency of Pakistan?",
        "options": ["USD", "EUR", "PKR", "GBP"],
        "answer": "PKR"
    }
]

# Store current question in session state
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

question = st.session_state.current_question

st.subheader(question["question"])

# Use radio buttons instead of selectbox for better usability
selected_option = st.radio(" 📝 Choose your answer:", question["options"], key="answer")

if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.success("✅ Correct answer!")
    else:
        st.error(f"❌ Incorrect answer! The correct answer is {question['answer']}")

    time.sleep(2)  # Pause to show feedback
    st.session_state.current_question = random.choice(questions)  # Load a new question
    st.rerun()




