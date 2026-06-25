import streamlit as st
import requests
import re
import os
from dotenv import load_dotenv

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="TalentScout AI",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Modern CSS
# -----------------------------
st.markdown("""
<style>

.stApp{
    background-color:#f5f7fb;
}

/* Header */
.header-box{
    background:linear-gradient(135deg,#2563eb,#1e40af);
    padding:25px;
    border-radius:15px;
    text-align:center;
    margin-bottom:20px;
}

.header-box h1,
.header-box p{
    color:white !important;
}

/* Form Card */
.form-box{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0 2px 10px rgba(0,0,0,0.08);
}

/* Question Card */
.question-box{
    background:white;
    color:#111827 !important;
    padding:20px;
    border-radius:15px;
    box-shadow:0 2px 10px rgba(0,0,0,0.08);
}

/* Text */
label,
p,
span,
h1,h2,h3,h4,h5,h6{
    color:#111827 !important;
}

/* Inputs */
.stTextInput input,
.stTextArea textarea,
.stNumberInput input{
    color:#111827 !important;
    background:white !important;
}

/* Buttons */
.stButton button{
    width:100%;
    border-radius:10px;
    font-weight:bold;
    height:3em;
}

/* Metrics */
[data-testid="metric-container"]{
    background:white;
    border-radius:10px;
    padding:15px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div class="header-box">
    <h1>🤖 TalentScout AI Hiring Assistant</h1>
    <p>AI Powered Technical Interview Simulator</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Groq API Function
# -----------------------------
def ask_groq(prompt):

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7,
        "max_tokens": 1500
    }

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        json=payload
    )

    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]

# -----------------------------
# Generate Questions
# -----------------------------
def generate_questions(role, exp, tech):

    prompt = f'''
Generate exactly 3 technical interview questions and answers.

Role: {role}
Experience: {exp} years
Tech Stack: {tech}

Format:

Q1. Question
Answer: Answer

Q2. Question
Answer: Answer

Q3. Question
Answer: Answer
'''

    output = ask_groq(prompt)

    questions = re.findall(
        r"Q\d+\.\s*(.*?)\nAnswer:\s*(.*?)(?=\nQ\d+\.|\Z)",
        output,
        re.DOTALL
    )

    if not questions:
        raise ValueError(
            "No interview questions could be parsed from the AI response. "
            "Please try again or verify the API output format."
        )

    return questions[:3]
# -----------------------------
# Evaluate Answer
# -----------------------------
def evaluate_answer(question, ideal_answer, user_answer):

    prompt = f"""
Evaluate the candidate answer.

Question:
{question}

Ideal Answer:
{ideal_answer}

Candidate Answer:
{user_answer}

Provide:

1. Score out of 10
2. Strengths
3. Areas for Improvement
4. Final Feedback

"""

    return ask_groq(prompt)

# -----------------------------
# Session State
# -----------------------------
defaults = {
    "started": False,
    "questions": [],
    "current": 0,
    "attempts": [],
    "candidate_name": "",
    "role": "",
    "experience": 0,
    "tech_stack": ""
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# -----------------------------
# Candidate Form
# -----------------------------
if not st.session_state.started:

    st.markdown('<div class="form-box">', unsafe_allow_html=True)

    st.subheader("👤 Candidate Information")

    with st.form("candidate_form"):

        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Full Name")
            experience = st.number_input(
                "Years of Experience",
                min_value=0,
                step=1
            )

        with col2:
            role = st.text_input("Desired Position")
            tech_stack = st.text_input(
                "Tech Stack (Python, SQL, ML, etc.)"
            )

        submitted = st.form_submit_button(
            "🚀 Start Interview"
        )

    st.markdown("</div>", unsafe_allow_html=True)

    if submitted:

        if not GROQ_API_KEY:
            st.error(
                "Groq API Key not found. Add it to your .env file."
            )

        elif not name or not tech_stack:
            st.warning(
                "Please fill all required fields."
            )

        else:

            with st.spinner(
                "Generating Interview Questions..."
            ):

                try:

                    questions = generate_questions(
                        role,
                        experience,
                        tech_stack
                    )

                    st.session_state.started = True
                    st.session_state.questions = questions
                    st.session_state.current = 0
                    st.session_state.attempts = []

                    st.session_state.candidate_name = name
                    st.session_state.role = role
                    st.session_state.experience = experience
                    st.session_state.tech_stack = tech_stack

                    st.rerun()

                except Exception as e:
                    st.error(
                        f"Error: {str(e)}"
                    )

# -----------------------------
# Interview Questions
# -----------------------------
else:

    total_questions = len(
        st.session_state.questions
    )

    if st.session_state.current < total_questions:

        question, ideal_answer = (
            st.session_state.questions[
                st.session_state.current
            ]
        )

        progress = (
            st.session_state.current + 1
        ) / total_questions

        st.progress(progress)

        st.markdown(
            f"### Question {st.session_state.current + 1} of {total_questions}"
        )

        st.markdown(
            f"""
            <div class="question-box">
                <h3 style="color:#111827;">
                    {question}
                </h3>
            </div>
            """,
            unsafe_allow_html=True
        )

        user_answer = st.text_area(
            "Your Answer",
            height=200
        )

        if st.button(
            "Submit Answer"
        ):

            if not user_answer.strip():

                st.warning(
                    "Please enter your answer."
                )

            else:

                with st.spinner(
                    "Evaluating your answer..."
                ):

                    evaluation = evaluate_answer(
                        question,
                        ideal_answer,
                        user_answer
                    )

                st.session_state.attempts.append({
                    "question": question,
                    "ideal_answer": ideal_answer,
                    "user_answer": user_answer,
                    "evaluation": evaluation
                })

                st.session_state.current += 1

                st.rerun()
                    # -----------------------------
    # Interview Completed
    # -----------------------------
    else:

        st.balloons()

        st.success(
            f"🎉 Interview Completed, {st.session_state.candidate_name}!"
        )

        st.markdown("## 📊 Interview Summary")

        # Show balloons again when the result summary appears
        st.balloons()

        total_score = 0

        for index, item in enumerate(
            st.session_state.attempts,
            start=1
        ):

            st.markdown("---")

            st.markdown(
                f"### 🔹 Question {index}"
            )

            st.markdown(
                f"**Question:** {item['question']}"
            )

            st.markdown(
                f"**Your Answer:**"
            )

            st.write(
                item["user_answer"]
            )

            with st.expander(
                "📘 View Ideal Answer"
            ):
                st.write(
                    item["ideal_answer"]
                )

            st.markdown(
                "**AI Evaluation:**"
            )

            st.info(
                item["evaluation"]
            )

            # Extract score from evaluation
            score_match = re.search(
                r'(\d+)\s*/\s*10',
                item["evaluation"]
            )

            if score_match:

                score = int(
                    score_match.group(1)
                )

                total_score += score

        st.markdown("---")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Questions",
                len(
                    st.session_state.attempts
                )
            )

        with col2:

            st.metric(
                "Total Score",
                f"{total_score}/30"
            )

        with col3:

            percentage = round(
                (total_score / 30) * 100,
                2
            )

            st.metric(
                "Percentage",
                f"{percentage}%"
            )

        # -----------------------------
        # Performance Message
        # -----------------------------
        if percentage >= 80:

            st.success(
                "🌟 Excellent Performance!"
            )

        elif percentage >= 60:

            st.info(
                "👍 Good Performance. Keep Practicing!"
            )

        else:

            st.warning(
                "📚 More practice recommended."
            )

        st.markdown("---")

        col_a, col_b = st.columns(2)

        # -----------------------------
        # Restart
        # -----------------------------
        with col_a:

            if st.button(
                "🔄 Restart Interview"
            ):

                for key in list(
                    st.session_state.keys()
                ):
                    del st.session_state[key]

                st.rerun()

        # -----------------------------
        # Practice Again
        # -----------------------------
        with col_b:

            if st.button(
                "🎯 Generate New Questions"
            ):

                try:

                    new_questions = generate_questions(
                        st.session_state.role,
                        st.session_state.experience,
                        st.session_state.tech_stack
                    )

                    st.session_state.questions = (
                        new_questions
                    )

                    st.session_state.current = 0

                    st.session_state.attempts = []

                    st.rerun()

                except Exception as e:

                    st.error(
                        f"Error: {str(e)}"
                    )