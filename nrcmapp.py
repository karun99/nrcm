import streamlit as st
import openai

# Set your OpenAI GPT-3 API key
openai.api_key = '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'

# Streamlit app title
st.title('NRCM GPT')

# User input text box
user_input = st.text_input('You:', '')

# Button to submit user input
if st.button('Ask'):
    # Request to OpenAI GPT-3 API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"You: {user_input}\nAI:",
        max_tokens=150000
    )
    
    # Extract and display the AI response
    ai_response = response.choices[0].text.strip()
    st.text_area('AI:', value=ai_response, height=100)

# Add a footer or any additional information if needed
st.markdown('This is a simple NRCM GPT app using Streamlit and OpenAI GPT-3.')

