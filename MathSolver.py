import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="MathSolver")

st.title("MathSolver using Gemini AI")

# Get API key from user input
api_key = st.sidebar.text_input("Enter your Google AI API key", type="password")

if not api_key:
    st.warning("Please enter your API key.")
    st.stop()

# Configure Gemini API
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Maintain chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm an AI chatbot that can solve mathematical problems."}
    ]

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
question = st.text_area("", placeholder="Ask any math-related question...")

if st.button("Assist"):
    if question:
        with st.spinner("Generating response..."):
            st.session_state.messages.append({"role": "user", "content": question})
            st.chat_message("user").write(question)

            # Generate response using Gemini API
            response = model.generate_content(question).text

            st.session_state.messages.append({"role": "assistant", "content": response})
            st.write("Response:")
            st.success(response)
    else:
        st.warning("Please provide a question.")
