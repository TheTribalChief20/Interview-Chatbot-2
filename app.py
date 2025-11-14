import streamlit as st
from utils import ask_gemini

# --------------------- PAGE CONFIG ---------------------
st.set_page_config(
    page_title="Interview Coach AI",
    page_icon="🎤",
    layout="centered",
)

# --------------------- HEADER ---------------------
st.markdown("""
# 🎤 Interview Coach AI  
Your personal assistant for interview prep, resume help, HR questions, and placement guidance.
""")

# --------------------- CHAT INTERFACE ---------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask me anything (Interview, Resume, HR, Placement)...", "")

if st.button("Send") and user_input.strip():
    # Add user's query
    st.session_state.chat_history.append(("You", user_input))

    # Get Gemini Response
    bot_response = ask_gemini(user_input)
    st.session_state.chat_history.append(("AI", bot_response))

# --------------------- DISPLAY CHAT ---------------------
st.write("### 💬 Chat History")
for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑‍💻 You:** {msg}")
    else:
        st.markdown(f"**🤖 AI:** {msg}")
