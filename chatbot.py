import streamlit as st

st.title(" AI-Powered Chatbot")
st.write("Ask me simple questions!")

user_input = st.text_input("You:")

if user_input:

    user_input = user_input.lower()

    if "hello" in user_input:
        response = "Hi! How can I help you today?"

    elif "how are you" in user_input:
        response = "I'm doing great! Thanks for asking."

    elif "what is python" in user_input:
        response = "Python is a popular programming language used in AI, web development, and data science."

    elif "what is ai" in user_input:
        response = "AI stands for Artificial Intelligence. It enables machines to perform tasks that normally require human intelligence."

    elif "bye" in user_input:
        response = "Goodbye! Have a nice day."

    else:
        response = "Sorry, I don't understand that question yet."

    st.success(response)